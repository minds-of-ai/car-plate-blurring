import cv2
import torch

class ImageBlur:
    MIN_MODEL_CONF = 0.6  # Minimum detection confidence

    def __init__(self, model_path: str = './model/best.pt') -> None:
        self.__model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=False)
        self.__model.conf = 0.25  # NMS confidence threshold
        self.__model.iou = 0.45  # NMS IoU threshold
        self.__model.agnostic = False  # NMS class-agnostic
        self.__model.multi_label = False  # NMS multiple labels per box
        self.__model.max_det = 20  # Maximum number of detections per image

    def blurLicencePlate(self, srcPath: str, dstPath: str) -> int:
        image = cv2.imread(srcPath)
        if image is None:
            raise FileNotFoundError(f"Image not found or cannot be loaded: {srcPath}")

        height, width = image.shape[:2]

        results = self.__model(srcPath)
        predictions = results.pred[0]

        if predictions.shape[0] == 0:
            print("No license plates detected.")
            cv2.imwrite(dstPath, image)
            return 0

        scores = predictions[:, 4]
        boxes = predictions[:, :4]  # x1, y1, x2, y2

        plates_blurred = 0

        for i in range(len(boxes)):
            # Skip low-confidence detections
            if scores[i] < ImageBlur.MIN_MODEL_CONF:
                continue

            x1, y1, x2, y2 = [int(e) for e in boxes[i]]
            
            # Ensure coordinates are within image bounds
            x1 = max(0, min(x1, width - 1))
            y1 = max(0, min(y1, height - 1))
            x2 = max(0, min(x2, width - 1))
            y2 = max(0, min(y2, height - 1))

            # Check if box has valid area
            if x2 <= x1 or y2 <= y1:
                continue

            plate = image[y1:y2, x1:x2]

            # Dynamically calculate blur kernel size based on plate size (optional)
            blur_width = max(15, (x2 - x1) // 3 | 1)  # Ensure odd number
            blur_height = max(15, (y2 - y1) // 3 | 1)
            blurred_plate = cv2.blur(plate, (blur_width, blur_height))

            # Replace the plate area with blurred version
            image[y1:y2, x1:x2] = blurred_plate
            plates_blurred += 1

        cv2.imwrite(dstPath, image)
        print(f"Blurred {plates_blurred} license plates.")
        return plates_blurred
