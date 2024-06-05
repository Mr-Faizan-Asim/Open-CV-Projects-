import cv2

from ultralytics import YOLO


model = YOLO('yolov8n.pt')

image = cv2.imread(r"A:/University/Summer 24/KICS/YoloWork/ByClickDetection/a.jpg")

result = model(image)

bounding_boxes = result[0].boxes.xyxy.tolist()
class_names = result[0].names


# Define the click event handler
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for box, cls_idx in zip (bounding_boxes, result[0].boxes.cls.tolist()):
            x_min,y_min,x_max,y_max= box[:4]
            if x_min <= x <= x_max and y_min <= y <= y_max:
                class_label = class_names[int(cls_idx)]
                print("clicked {class_label}")
                cv2.rectangle(image,(int(x_min),int(y_min),int(x_max),int(y_max)),(0,255,0),2)
                cv2.rectangle(image,(int(x_min),int(y_min)-20), (int(x_min)+50,int(y_min)),(0,255,0),-1)
                text = f"{class_label}"
                cv2.putText(image,text,(int(x_min),int(y_min) - 5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                cv2.imshow("image",image)
                cv2.waitKey(0)
                break
                



cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click_event)
cv2.imshow("Image", image)

# Set the mouse callback function

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
