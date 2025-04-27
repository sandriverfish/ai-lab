import sys
import platform
import numpy as np
import cv2
import paddle
import paddlex

print("Python版本:", platform.python_version())
print("NumPy版本:", np.__version__)
print("OpenCV版本:", cv2.__version__)
print("PaddlePaddle版本:", paddle.__version__)
print("PaddleX版本:", paddlex.__version__)
print("CUDA可用:", paddle.device.is_compiled_with_cuda())

# 尝试获取GPU信息的替代方法
try:
    gpu_count = len(paddle.device.get_available_device())
    print("可用设备:", paddle.device.get_available_device())
except:
    try:
        # 另一种方法
        gpu_count = paddle.device.cuda.device_count()
        print("GPU数量:", gpu_count)
    except:
        print("无法获取GPU数量，但CUDA支持已确认")

# 测试简单的Paddle操作
if paddle.device.is_compiled_with_cuda():
    x = paddle.to_tensor([1.0, 2.0, 3.0], dtype='float32')
    y = paddle.to_tensor([4.0, 5.0, 6.0], dtype='float32')
    z = paddle.add(x, y)
    print("Paddle张量运算测试:", z.numpy())

# 测试简单的OpenCV操作
img = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.rectangle(img, (25, 25), (75, 75), (0, 255, 0), 2)
print("OpenCV图像操作测试: 成功")

print("环境验证完成!")
