from ultralytics import YOLO
import cv2

# 加载预训练的YOLO模型
model = YOLO('yolov8n.pt')  # 基础模型，也可以使用更大的模型如yolov8m.pt

# 或者使用专门的车牌检测模型
# model = YOLO('license_plate_detector.pt')

# 读取图像
image = cv2.imread('car_image.jpg')

# 进行检测
results = model(image)

# 处理检测结果
for result in results:
    for box in result.boxes:
        # 筛选出车辆类别 (YOLO中车辆类别包括car, truck等)
        if box.cls in [2, 3, 5, 7]:  # 这些是YOLO中车辆相关的类别ID
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 对车辆区域进行二次检测寻找车牌
            # 这里可以添加更专门的车牌检测逻辑

# 显示结果
cv2.imshow('License Plate Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
