from roboflow import Roboflow
import datetime

rf = Roboflow(api_key="PTO9J5nMBYNNpj4SWYDi")

# Debugging: Print workspace data
workspace = rf.workspace("tennis-mivzb")
print(workspace)

# Attempt to load project data
try:
    project_data = workspace.project("skipper-proj")
    print(project_data)
    
    # Handle NoneType for the created field
    if project_data['created'] is None:
        project_data['created'] = datetime.datetime.now().timestamp()  # or any default timestamp
    
    # Proceed with the project initialization
    project = rf.workspace("tennis-mivzb").project("skipper-proj")
    version = project.version(2)
    dataset = version.download("yolov5")
