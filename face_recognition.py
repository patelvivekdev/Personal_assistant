"""All function of face recognition."""
import os
import cv2
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import load_img, save_img, img_to_array
from keras.applications.imagenet_utils import preprocess_input
from keras.preprocessing import image

# Load Model


def create_model():
    """Load Model with keras load_model function."""
    model = load_model("./model/model.h5")
    print("Model Loaded...")

    return model


# Preprocess Image
def preprocess_image(image_path):
    """Loads image from path and resizes it"""
    img = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.imagenet_utils.preprocess_input(img)

    return img


# FindSimilarity
def findCosineSimilarity(source_representation, test_representation):
    """Find CosinesSimilarity"""
    a = np.matmul(np.transpose(source_representation), test_representation)
    b = np.sum(np.multiply(source_representation, source_representation))
    c = np.sum(np.multiply(test_representation, test_representation))

    return 1 - (a / (np.sqrt(b) * np.sqrt(c)))


# Load Detector
def load_detector():
    """Load Face Detector"""
    prototxt = "./model/deploy.prototxt"
    caff_model = "./model/res10_300x300_ssd_iter_140000.caffemodel"
    detector = cv2.dnn.readNetFromCaffe(prototxt, caff_model)

    return detector


# Detect Face
def detect_face(img):
    """Detect face from image using ssd."""
    original_size = img.shape
    target_size = (300, 300)
    img = cv2.resize(img, target_size)  # Resize to target_size
    aspect_ratio_x = original_size[1] / target_size[1]
    aspect_ratio_y = original_size[0] / target_size[0]
    imageBlob = cv2.dnn.blobFromImage(image=img)
    detector = load_detector()
    detector.setInput(imageBlob)
    detections = detector.forward()

    return detections, aspect_ratio_x, aspect_ratio_y


# Predict Using Webcam
def predict_persion(model):
    """Predict on webcam and return name of detected person if it's already addded to list """

    found = 0
    final_name = ""

    mypath = "./group_of_faces/"  # Change according to your folder
    all_people_faces = dict()

    for file in os.listdir(mypath):
        person_face = file.split(".")[0]
        all_people_faces[person_face] = model.predict(
            preprocess_image("./group_of_faces/%s.jpg" % (person_face))
        )[0, :]

    print("Face representations retrieved successfully")
    # Open Webcam
    cap = cv2.VideoCapture(
        0, cv2.CAP_DSHOW
    )  # change number with according to your camera config
    print("Start Recogintion.....")
    while True:
        try:
            ret, img = cap.read()
            base_img = img.copy()
            detections, aspect_ratio_x, aspect_ratio_y = detect_face(img)
            detections_df = pd.DataFrame(
                detections[0][0],
                columns=[
                    "img_id",
                    "is_face",
                    "confidence",
                    "left",
                    "top",
                    "right",
                    "bottom",
                ],
            )
            detections_df = detections_df[detections_df["is_face"] == 1]
            detections_df = detections_df[detections_df["confidence"] >= 0.95]
            if len(detections_df) != 0:
                for i, instance in detections_df.iterrows():
                    left = int(instance["left"] * 300)
                    bottom = int(instance["bottom"] * 300)
                    right = int(instance["right"] * 300)
                    top = int(instance["top"] * 300)
                    # drow rectangle to main image
                    cv2.rectangle(
                        img,
                        (int(left * aspect_ratio_x), int(top * aspect_ratio_y)),
                        (int(right * aspect_ratio_x),
                         int(bottom * aspect_ratio_y)),
                        (255, 0, 0),
                        2,
                    )
                    confidence_score = str(
                        round(100 * instance["confidence"], 2)) + " %"
                    detected_face = base_img[
                        int(top * aspect_ratio_y)
                        - 100: int(bottom * aspect_ratio_y)
                        + 100,
                        int(left * aspect_ratio_x)
                        - 100: int(right * aspect_ratio_x)
                        + 100,
                    ]
                    if len(detected_face) != 0:
                        try:
                            detected_face = cv2.resize(
                                detected_face, (224, 224)
                            )  # resize to 224x224
                            img_pixels = image.img_to_array(detected_face)
                            img_pixels = np.expand_dims(img_pixels, axis=0)
                            img_pixels /= 255
                            captured_representation = model.predict(img_pixels)[
                                0, :]
                            for i in all_people_faces:
                                person_name = i
                                representation = all_people_faces[i]
                                similarity = findCosineSimilarity(
                                    representation, captured_representation
                                )
                                if similarity < 0.30:
                                    print(similarity)
                                    final_name = person_name[5:]
                                    found = 1
                                    break
                            if found == 0:
                                final_name = "unknown"
                                cv2.putText(
                                    img,
                                    "unknown",
                                    (
                                        int((left * aspect_ratio_x) + 15),
                                        int((top * aspect_ratio_y) - 12),
                                    ),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    1,
                                    (255, 0, 0),
                                    2,
                                )
                        except Exception as e:
                            pass
                    else:
                        pass
                cv2.imshow("img", img)
                if "vivek" in final_name:
                    final_name = 'vivek'
                    break
                if "smit" in final_name:
                    final_name - 'smit'
                    break
                if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                    break
            else:
                pass
        except Exception as e:
            print(e)

    cap.release()
    cv2.destroyAllWindows()

    return final_name
