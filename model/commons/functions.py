import os
import numpy as np
import pandas as pd
from keras.preprocessing.image import load_img, save_img, img_to_array
from keras.applications.imagenet_utils import preprocess_input
from keras.preprocessing import image
import cv2
from pathlib import Path
import gdown
import hashlib
import math
from PIL import Image
import copy
import base64
import multiprocessing
import subprocess
import tensorflow as tf
import keras


def loadBase64Img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def distance(a, b):
    x1 = a[0];
    y1 = a[1]
    x2 = b[0];
    y2 = b[1]

    return math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))


def findFileHash(file):
    BLOCK_SIZE = 65536  # The size of each read from the file

    file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f:  # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE)  # Read from the file. Take in the amount declared above
        while len(fb) > 0:  # While there is still data being read from the file
            file_hash.update(fb)  # Update the hash
            fb = f.read(BLOCK_SIZE)  # Read the next block from the file

    return file_hash.hexdigest()


def initializeFolder():
    home = str(Path.home())

    if not os.path.exists(home + "/.faceAnalytics"):
        os.mkdir(home + "/.faceAnalytics")
        print("Directory ", home, "/.faceAnalytics created")

    if not os.path.exists(home + "/.faceAnalytics/weights"):
        os.mkdir(home + "/.faceAnalytics/weights")
        print("Directory ", home, "/.faceAnalytics/weights created")
    if not os.path.exists(home + "/.faceAnalytics/YoklamaKayitlari"):
        os.mkdir(home + "/.faceAnalytics/YoklamaKayitlari")
        print("Directory ", home, "/.faceAnalytics/YoklamaKayitlari created")
    # ----------------------------------

# ----------------------------------

def findThreshold(model_name, distance_metric):
    threshold = 0.40

    if model_name == 'VGG-Face':
        if distance_metric == 'cosine':
            threshold = 0.40
        elif distance_metric == 'euclidean':
            threshold = 0.55
        elif distance_metric == 'euclidean_l2':
            threshold = 0.75

    elif model_name == 'OpenFace':
        if distance_metric == 'cosine':
            threshold = 0.10
        elif distance_metric == 'euclidean':
            threshold = 0.55
        elif distance_metric == 'euclidean_l2':
            threshold = 0.55

    elif model_name == 'Facenet':
        if distance_metric == 'cosine':
            threshold = 0.40
        elif distance_metric == 'euclidean':
            threshold = 10
        elif distance_metric == 'euclidean_l2':
            threshold = 0.80

    elif model_name == 'DeepFace':
        if distance_metric == 'cosine':
            threshold = 0.23
        elif distance_metric == 'euclidean':
            threshold = 64
        elif distance_metric == 'euclidean_l2':
            threshold = 0.64

    return threshold




def detectFace(img, target_size=(224, 224), grayscale=False):
    # -----------------------

    exact_image = False
    if type(img).__module__ == np.__name__:
        exact_image = True

    base64_img = False
    if len(img) > 11 and img[0:11] == "data:image/":
        base64_img = True

    # -----------------------

    # --------------------------------

    face_detector = cv2.CascadeClassifier("model/commons/haarcascade_frontalface_default.xml")
    eye_detector = cv2.CascadeClassifier("model/commons/haarcascade_eye.xml")

    if base64_img == True:
        img = loadBase64Img(img)

    elif exact_image != True:  # image path passed as input

        if os.path.isfile(img) != True:
            raise ValueError("Confirm that ", img, " exists")

        img = cv2.imread(img)

    img_raw = img.copy()

    # --------------------------------

    faces = face_detector.detectMultiScale(img, 1.3, 5)

    # print("found faces in ",image_path," is ",len(faces))

    if len(faces) > 0:
        x, y, w, h = faces[0]
        detected_face = img[int(y):int(y + h), int(x):int(x + w)]
        detected_face_gray = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)

        # ---------------------------
        # face alignment

        eyes = eye_detector.detectMultiScale(detected_face_gray)

        if len(eyes) >= 2:
            # find the largest 2 eye
            base_eyes = eyes[:, 2]

            items = []
            for i in range(0, len(base_eyes)):
                item = (base_eyes[i], i)
                items.append(item)

            df = pd.DataFrame(items, columns=["length", "idx"]).sort_values(by=['length'], ascending=False)

            eyes = eyes[df.idx.values[0:2]]

            # -----------------------
            # decide left and right eye

            eye_1 = eyes[0];
            eye_2 = eyes[1]

            if eye_1[0] < eye_2[0]:
                left_eye = eye_1
                right_eye = eye_2
            else:
                left_eye = eye_2
                right_eye = eye_1

            # -----------------------
            # find center of eyes

            left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
            left_eye_x = left_eye_center[0];
            left_eye_y = left_eye_center[1]

            right_eye_center = (int(right_eye[0] + (right_eye[2] / 2)), int(right_eye[1] + (right_eye[3] / 2)))
            right_eye_x = right_eye_center[0];
            right_eye_y = right_eye_center[1]

            # -----------------------
            # find rotation direction

            if left_eye_y > right_eye_y:
                point_3rd = (right_eye_x, left_eye_y)
                direction = -1  # rotate same direction to clock
            else:
                point_3rd = (left_eye_x, right_eye_y)
                direction = 1  # rotate inverse direction of clock

            # -----------------------
            # find length of triangle edges

            a = distance(left_eye_center, point_3rd)
            b = distance(right_eye_center, point_3rd)
            c = distance(right_eye_center, left_eye_center)

            # -----------------------
            # apply cosine rule

            cos_a = (b * b + c * c - a * a) / (2 * b * c)
            angle = np.arccos(cos_a)  # angle in radian
            angle = (angle * 180) / math.pi  # radian to degree

            # -----------------------
            # rotate base image

            if direction == -1:
                angle = 90 - angle

            img = Image.fromarray(img_raw)
            img = np.array(img.rotate(direction * angle))

            # you recover the base image and face detection disappeared. apply again.
            faces = face_detector.detectMultiScale(img, 1.3, 5)
            if len(faces) > 0:
                x, y, w, h = faces[0]
                detected_face = img[int(y):int(y + h), int(x):int(x + w)]

        # -----------------------

        # face alignment block end
        # ---------------------------

        # face alignment block needs colorful images. that's why, converting to gray scale logic moved to here.
        if grayscale:
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY)

        detected_face = cv2.resize(detected_face, target_size)

        img_pixels = image.img_to_array(detected_face)
        img_pixels = np.expand_dims(img_pixels, axis=0)

        # normalize input in [0, 1]
        img_pixels /= 255

        return img_pixels

    else:

        if exact_image:

            if grayscale:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            img = cv2.resize(img, target_size)
            img_pixels = image.img_to_array(img)
            img_pixels = np.expand_dims(img_pixels, axis=0)
            img_pixels /= 255
            return img_pixels
        else:
            raise ValueError("Face could not be detected in  Please confirm that the picture is a face photo.")


def allocateMemory():
    # find allocated memories
    gpu_indexes = []
    memory_usage_percentages = []
    available_memories = []
    total_memories = []
    utilizations = []
    power_usages = []
    power_capacities = []

    try:
        result = subprocess.check_output(['nvidia-smi'])

        dashboard = result.decode("utf-8").split("=|")

        dashboard = dashboard[1].split("\n")

        gpu_idx = 0
        for line in dashboard:
            if "MiB" in line:
                power_info = line.split("|")[1]
                power_capacity = int(power_info.split("/")[-1].replace("W", ""))
                power_usage = int((power_info.split("/")[-2]).strip().split(" ")[-1].replace("W", ""))

                power_usages.append(power_usage)
                power_capacities.append(power_capacity)

                # ----------------------------

                memory_info = line.split("|")[2].replace("MiB", "").split("/")
                utilization_info = int(line.split("|")[3].split("%")[0])

                allocated = int(memory_info[0])
                total_memory = int(memory_info[1])
                available_memory = total_memory - allocated

                total_memories.append(total_memory)
                available_memories.append(available_memory)
                memory_usage_percentages.append(round(100 * int(allocated) / int(total_memory), 4))
                utilizations.append(utilization_info)
                gpu_indexes.append(gpu_idx)

                gpu_idx = gpu_idx + 1

        gpu_count = gpu_idx * 1

    except Exception as err:
        gpu_count = 0
        print(str(err))

    # ------------------------------

    df = pd.DataFrame(gpu_indexes, columns=["gpu_index"])
    df["total_memories_in_mb"] = total_memories
    df["available_memories_in_mb"] = available_memories
    df["memory_usage_percentage"] = memory_usage_percentages
    df["utilizations"] = utilizations
    df["power_usages_in_watts"] = power_usages
    df["power_capacities_in_watts"] = power_capacities

    df = df.sort_values(by=["available_memories_in_mb"], ascending=False).reset_index(drop=True)

    # ------------------------------

    required_memory = 10000  # All face models require 9016 MiB

    if df.shape[0] > 0:  # has gpu
        if df.iloc[0].available_memories_in_mb > required_memory:
            my_gpu = str(int(df.iloc[0].gpu_index))
            os.environ["CUDA_VISIBLE_DEVICES"] = my_gpu

            # ------------------------------
            # tf allocates all memory by default
            # this block avoids greedy approach

            config = tf.compat.v1.ConfigProto()
            config.gpu_options.allow_growth = True
            session = tf.compat.v1.Session(config=config)
            keras.backend.set_session(session)

            print("Face Analysis will run on GPU (gpu_", my_gpu, ")")
            print("GPU Çalışıyor...")
        else:
            # this case has gpu but no enough memory to allocate
            os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # run it on cpu
            # print("Even though the system has GPUs, there is no enough space in memory to allocate.")
            print("Face Analysis will run on CPU")
    else:
        print("Face Analysis will run on CPU")

# ------------------------------
