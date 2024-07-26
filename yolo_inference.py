from ultralytics import YOLO

model = YOLO('yolov8n')

# results = model.predict('/Users/tylerklimas/Desktop/landslide/input_video.mp4', save=True)

# print(results[0]) # prints first frame

# for box in results[0].boxes:
#     print(box)

# !pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="PTO9J5nMBYNNpj4SWYDi")
project = rf.workspace("viren-dhanwani").project("tennis-ball-detection")
version = project.version(6)
dataset = version.download("yolov5")