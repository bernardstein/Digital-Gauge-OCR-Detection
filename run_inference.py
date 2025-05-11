#https://inference.roboflow.com/quickstart/run_model_on_image/#run-inference-on-a-v1-route

import requests
import base64
from PIL import Image
from io import BytesIO

project_id = "PROJECT_ID"
model_version = 1
confidence = 0.5
iou_thresh = 0.5
api_key = "YOUR_ROBOFLOW_API_KEY"

# URL Image
image_url = "https://.../image.jpg"

res = requests.post(
    f"http://localhost:9001/{project_id}/{model_version}?api_key={api_key}&confidence={confidence}&overlap={iou_thresh}&image={image_url}",
)

# Base64 Image
#file_name = "path/to/local/image.jpg"

#image = Image.open(file_name)

#buffered = BytesIO()

#image.save(buffered, quality=100, format="JPEG")

#img_str = base64.b64encode(buffered.getvalue())
#img_str = img_str.decode("ascii")

#res = requests.post(
#    f"https://detect.roboflow.com/{project_id}/{model_version}?api_key={api_key}&confidence={confidence}&overlap={iou_thresh}",
#    data=img_str,
#    headers={"Content-Type": "application/json"},
#)

#NumPy Array
#file_name = "path/to/local/image.jpg"

#image = cv2.imread(file_name)
#numpy_data = pickle.dumps(image)

#res = requests.post(
#    f"http://localhost:9001/{project_id}/{model_version}?api_key={api_key}&image_type=numpy",
#    data=numpy_data,
#    headers={"Content-Type": "application/json"},
#)

predictions = res.json()
print(predictions)
