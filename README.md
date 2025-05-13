# Roboflow Inference on YOLOv8s/m, FR-DETR and Edge Deployment

This project demonstrates how to deploy and run a computer vision model on the edge using [Roboflow Inference](https://inference.roboflow.com/), an open-source inference server that can be run via Docker or Python.

Combined-Dataset-V1: https://universe.roboflow.com/bernards-workspace-ahsqq/combined-dataset-gauge-digital-7-segment-voltmeter/dataset/1
Combined-Dataset-V2: https://universe.roboflow.com/bernards-workspace-ahsqq/combined-dataset-v2/dataset/1
YOLOv8s Model: https://universe.roboflow.com/bernards-workspace-ahsqq/combined-dataset-gauge-digital-7-segment-voltmeter/model/1
YOLOv8m Model: https://universe.roboflow.com/bernards-workspace-ahsqq/combined-dataset-v2/model/2
RF-DETR Model: https://universe.roboflow.com/bernards-workspace-ahsqq/combined-dataset-v2/model/1
GitHub Repository: https://github.com/bernardstein/Digital-Gauge-OCR-Detection

---
📓 Train Your Model in Google Colab
We provide a Google Colab notebook for training a YOLOv8 object detection model on a custom dataset with Roboflow:

👉 Open Colab Notebook

Features:
Load datasets directly from Roboflow.

Train and validate a YOLOv8 model using Ultralytics.

Export trained weights for deployment.

Optionally evaluate and visualize predictions in-line.

Instructions:
Open the notebook in Google Colab.

Follow the cells step-by-step to configure your dataset and model.

Once training is complete, download your weights (e.g., best.pt) for deployment.

---

🐳 Docker Deployment

To deploy the Roboflow Inference server with GPU support:

```bash
docker pull roboflow/roboflow-inference-server-gpu
docker run --gpus all -p 9001:9001 roboflow/roboflow-inference-server-gpu
```

> If you're deploying on a device without a GPU, use the appropriate CPU/ARM image, such as `roboflow/roboflow-inference-server-cpu`.

---
🐍 Python Inference Script

Install the required dependencies:

```bash
pip install requests pillow
```

Run the script:

```bash
python run_inference.py
```

This script supports:

* Inference using image URLs.
* (Commented) Support for base64 image input.
* (Commented) Support for NumPy image input.

### 🔧 Configuration

Edit the following variables in `run_inference.py`:

```python
project_id = "YOUR_PROJECT_ID"         # Your Roboflow project/workspace ID
model_version = 1                      # The version number of your model
confidence = 0.5                       # Confidence threshold for predictions
iou_thresh = 0.5                       # IOU threshold
api_key = "YOUR_ROBOFLOW_API_KEY"      # Your Roboflow API key
image_url = "https://.../image.jpg"    # Publicly accessible image URL
```

Optional inputs (uncomment one of the following sections):

* Base64 encoded local image
* NumPy image array (requires OpenCV and pickle)

---

## 📤 Output

The script returns predictions in JSON format, containing bounding boxes, class labels, and confidence scores.

Example output:

```json
{
  "predictions": [
    {
      "x": 123,
      "y": 234,
      "width": 50,
      "height": 60,
      "class": "object",
      "confidence": 0.87
    }
  ]
}
```
---

## 🧠 Resources

* [Roboflow Inference Quickstart](https://inference.roboflow.com/quickstart)
* [Roboflow Docs](https://docs.roboflow.com/inference/hosted-api)
