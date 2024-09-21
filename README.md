# 🚗 License Plate Blurring using YOLOv5

This project automatically detects and blurs license plates from car images using a YOLOv5 model. It processes all images in a folder and saves the blurred versions in a target directory.  

---

## 📁 Project Structure

```
.
├── images/                # Input images to be processed
│   ├── car1.jpg
│   ├── car2.png
│   └── ...               
├── images/blurred/       # Output folder where blurred images will be saved
├── model/
│   └── best.pt           # YOLOv5 trained model for license plate detection
├── blur.py               # Class for license plate detection and blurring
├── main.py               # Main script to process all images in bulk
└── README.md             # Project documentation
```

---

## ✅ Features

- Detects license plates using a YOLOv5 model.
- Automatically applies a blur effect on detected license plates.
- Processes all images in the `images/` directory.
- Saves output images to `images/blurred/`.
- Supports multiple image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`).

---

## ⚙️ Requirements

- Python 3.8+
- OpenCV
- yolov5 (with all dependencies like PyTorch)

---

## 📦 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/minds-of-ai/car-plate-blurring.git
cd car-plate-blurring
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

> **Note:** You should have a trained YOLOv5 model (`best.pt`) placed in the `model/` directory.

---

## 🚀 Usage

1. **Place all your car images in the `images/` folder.**

2. **Run the script:**
```bash
python main.py
```

3. **Find all processed (blurred) images in `images/blurred/`.**

---

## 📝 Example

- **Input Image:**
  - `images/car1.jpg`

- **Output Image (with blurred license plate):**
  - `images/blurred/car1.jpg`

---

## 🛐 Error Handling

- If no plates are detected, the image will be saved as-is to the output directory.
- If an image is unreadable or corrupt, an error will be logged, and processing will continue with the next file.

---

## 🔧 Configuration

- **Confidence Threshold:** You can adjust the detection confidence in `blur.py`:
```python
MIN_MODEL_CONF = 0.6  # Default confidence threshold
```

- **Model Path:** Set model path when initializing `blur` in `main.py`:
```python
blur_tool = ImageBlur('./model/best.pt')
```

---

## 📷 Supported Formats

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.tiff`
- `.webp`

---

## 🙌 Acknowledgments

- Built using [YOLOv5](https://github.com/ultralytics/yolov5) for license plate detection.
- OpenCV for image processing and blurring.
