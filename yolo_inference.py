from ultralytics import YOLO

model = YOLO('/Users/tylerklimas/Desktop/landslide/best.pt')

md = YOLO('yolov8s')

results = model.track('/Users/tylerklimas/Desktop/landslide/input_video.mp4', save=True)


results = md.track('/Users/tylerklimas/Desktop/landslide/input_video.mp4', save=True)

print(results[0]) # prints first frame

for box in results[0].boxes:
    print(box)

# !pip install roboflow

# from roboflow import Roboflow
# rf = Roboflow(api_key="PTO9J5nMBYNNpj4SWYDi")
# project = rf.workspace("viren-dhanwani").project("tennis-ball-detection")
# version = project.version(6)
# dataset = version.download("yolov5")

# import shutil
# shutil.move('tennis-ball-detection-6/train',
#             'tennis-ball-detection-6/tennis-ball-detection-6/train')

# shutil.move('tennis-ball-detection-6/test',
#             'tennis-ball-detection-6/tennis-ball-detection-6/test')

# shutil.move('tennis-ball-detection-6/valid',
#             'tennis-ball-detection-6/tennis-ball-detection-6/valid')