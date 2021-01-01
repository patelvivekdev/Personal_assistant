# import tools
# from Face_Detection import face_detection
from Face_Recognition import create_model, predict_persion

# print('_____Start collecting image from directory_____')
# face_detection()

print("_____Start loading model_____")
model = create_model()

predict_persion(model=model)
