# Jetson Xavier NX 悟空机器学习集成环境搭建指南

本指南提供了为悟空机器学习集成项目搭建Nvidia Jetson Xavier NX开发环境的详细步骤。

## 1. 硬件要求

- Nvidia Jetson Xavier NX开发套件
- 电源适配器（19V）
- MicroSD卡（推荐64GB+）
- USB键盘和鼠标
- HDMI显示器
- 以太网电缆或Wi-Fi连接
- 可选：USB网络摄像头或兼容的工业相机用于测试

## 2. 初始系统设置

### 2.1 刷写JetPack 5.1.4

1. **在主机电脑上：**
   - 下载并安装[NVIDIA SDK Manager](https://developer.nvidia.com/nvidia-sdk-manager)
   - 将主机电脑连接到互联网
   - 启动SDK Manager并使用您的NVIDIA开发者账户登录

2. **选择以下选项：**
   - 产品类别：Jetson
   - 硬件配置：Jetson Xavier NX
   - 目标操作系统：JetPack 5.1.4 (L4T 35.4.1)

3. **按照SDK Manager的指示：**
   - 下载所需组件
   - 刷写Jetson Xavier NX
   - 安装选定的组件

4. **在Jetson上完成初始设置：**
   - 创建用户名和密码
   - 配置系统设置
   - 连接到Wi-Fi或以太网

### 2.2 系统配置

1. **更新系统：**
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **安装基本开发工具：**
   ```bash
   sudo apt install -y build-essential git cmake python3-dev python3-pip
   sudo apt install -y libopencv-dev libopenblas-dev
   ```

3. **配置电源模式以获得最佳性能：**
   ```bash
   sudo nvpmodel -m 2  # 15W 6核模式
   sudo jetson_clocks   # 将时钟设置为最大
   ```

4. **设置交换空间（推荐用于ML训练）：**
   ```bash
   sudo fallocate -l 8G /var/swapfile
   sudo chmod 600 /var/swapfile
   sudo mkswap /var/swapfile
   sudo swapon /var/swapfile
   echo '/var/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab
   ```

## 3. PaddlePaddle安装

### 3.1 安装PaddlePaddle依赖项

1. **安装所需软件包：**
   ```bash
   sudo apt install -y python3-pip python3-dev python3-matplotlib
   sudo apt install -y libatlas-base-dev libopenblas-dev libblas-dev
   sudo apt install -y liblapack-dev patchelf gfortran
   ```

2. **升级pip并安装额外的Python包：**
   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install numpy protobuf==3.20.3 wheel setuptools
   python3 -m pip install decorator attrs six psutil Pillow
   ```

### 3.2 安装PaddlePaddle GPU版本

1. **安装CUDA工具包和cuDNN（应包含在JetPack中）：**
   ```bash
   # 验证CUDA安装
   nvcc --version
   
   # 验证cuDNN安装
   dpkg -l | grep cudnn
   ```

2. **安装PaddlePaddle 3.0.0-rc GPU版本：**
   ```bash
   python3 -m pip install paddlepaddle-gpu==3.0.0rc0.post110 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
   ```

3. **验证PaddlePaddle安装：**
   ```bash
   python3 -c "import paddle; print(paddle.__version__); print(paddle.device.is_compiled_with_cuda())"
   ```

## 4. PaddleX安装

1. **安装PaddleX 3.0.0-rc：**
   ```bash
   python3 -m pip install paddlex==3.0.0rc
   ```

2. **验证PaddleX安装：**
   ```bash
   python3 -c "import paddlex; print(paddlex.__version__)"
   ```

## 5. 安装额外的库

1. **安装支持CUDA的OpenCV（如果尚未安装）：**
   ```bash
   # OpenCV应该包含在JetPack中，使用以下命令验证：
   python3 -c "import cv2; print(cv2.__version__); print(cv2.getBuildInformation())"
   ```

2. **安装可视化和实用工具库：**
   ```bash
   python3 -m pip install matplotlib scikit-learn pandas
   python3 -m pip install visualdl tensorboard
   ```

3. **安装额外的PaddlePaddle生态系统包：**
   ```bash
   python3 -m pip install paddleslim  # 用于模型优化
   python3 -m pip install paddle2onnx  # 用于模型转换
   ```

## 6. 设置项目环境

### 6.1 创建项目目录

```bash
mkdir -p ~/wukong-ml
cd ~/wukong-ml
```

### 6.2 克隆必要的代码库

```bash
# 克隆PaddleDetection用于目标检测模型
git clone https://github.com/PaddlePaddle/PaddleDetection.git
cd PaddleDetection
git checkout release/2.6
pip install -r requirements.txt
python setup.py install
cd ..

# 克隆PaddleClas用于分类模型
git clone https://github.com/PaddlePaddle/PaddleClas.git
cd PaddleClas
git checkout release/2.5
pip install -r requirements.txt
python setup.py install
cd ..
```

### 6.3 设置虚拟环境（可选）

如果您更喜欢使用虚拟环境：

```bash
sudo apt install -y python3-venv
python3 -m venv wukong-env
source wukong-env/bin/activate

# 在虚拟环境中安装所有包
# （重复上述安装步骤）
```

## 7. 测试环境

### 7.1 基本PaddlePaddle测试

创建一个名为`test_paddle.py`的文件：

```python
import paddle
import numpy as np

# 创建一个简单的神经网络
class SimpleNet(paddle.nn.Layer):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = paddle.nn.Linear(10, 1)
        
    def forward(self, x):
        return self.fc(x)

# 使用随机数据测试
model = SimpleNet()
x = paddle.randn([5, 10], dtype='float32')
y = model(x)

print("模型输出形状:", y.shape)
print("Paddle是否使用GPU:", paddle.device.is_compiled_with_cuda())
print("当前设备:", paddle.device.get_device())
```

运行测试：

```bash
python3 test_paddle.py
```

### 7.2 使用预训练模型测试

创建一个名为`test_pretrained.py`的文件：

```python
import paddlex as pdx
import cv2
import numpy as np

# 下载预训练模型
model = pdx.load_model('https://bj.bcebos.com/paddlex/models/xiaoduxiong_epoch_12.pdx')

# 使用样本图像测试
img = cv2.imread('path/to/test/image.jpg')
if img is None:
    # 如果没有可用的测试图像，创建一个测试图像
    img = np.random.randint(0, 255, (640, 480, 3), dtype=np.uint8)
    cv2.imwrite('test_image.jpg', img)
    img = cv2.imread('test_image.jpg')

# 执行推理
result = model.predict(img)
print("推理结果:", result)
```

运行测试：

```bash
python3 test_pretrained.py
```

## 8. 性能基准测试

### 8.1 GPU性能测试

创建一个名为`benchmark_gpu.py`的文件：

```python
import paddle
import time
import numpy as np

def benchmark_matmul(size=1000, iterations=100):
    # 创建随机矩阵
    a = paddle.randn([size, size], dtype='float32')
    b = paddle.randn([size, size], dtype='float32')
    
    # 预热
    for _ in range(10):
        c = paddle.matmul(a, b)
    
    # 基准测试
    start_time = time.time()
    for _ in range(iterations):
        c = paddle.matmul(a, b)
        paddle.device.cuda.synchronize()
    end_time = time.time()
    
    elapsed = end_time - start_time
    return elapsed / iterations

# 运行基准测试
avg_time = benchmark_matmul(size=2000, iterations=50)
print(f"平均矩阵乘法时间: {avg_time*1000:.2f} ms")
```

运行基准测试：

```bash
python3 benchmark_gpu.py
```

### 8.2 推理速度测试

创建一个名为`benchmark_inference.py`的文件：

```python
import paddle
import paddlex as pdx
import time
import numpy as np

# 创建一个简单的测试模型
class TestModel(paddle.nn.Layer):
    def __init__(self):
        super(TestModel, self).__init__()
        self.conv1 = paddle.nn.Conv2D(3, 64, kernel_size=3, padding=1)
        self.conv2 = paddle.nn.Conv2D(64, 64, kernel_size=3, padding=1)
        self.pool = paddle.nn.MaxPool2D(kernel_size=2, stride=2)
        self.flatten = paddle.nn.Flatten()
        self.fc1 = paddle.nn.Linear(64 * 120 * 160, 512)
        self.fc2 = paddle.nn.Linear(512, 10)
        
    def forward(self, x):
        x = self.pool(paddle.nn.functional.relu(self.conv1(x)))
        x = self.pool(paddle.nn.functional.relu(self.conv2(x)))
        x = self.flatten(x)
        x = paddle.nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 创建模型和测试数据
model = TestModel()
model.eval()
test_input = paddle.randn([1, 3, 480, 640], dtype='float32')

# 预热
for _ in range(10):
    _ = model(test_input)
    paddle.device.cuda.synchronize()

# 基准测试
iterations = 100
start_time = time.time()
for _ in range(iterations):
    _ = model(test_input)
    paddle.device.cuda.synchronize()
end_time = time.time()

avg_time = (end_time - start_time) / iterations
print(f"平均推理时间: {avg_time*1000:.2f} ms")
```

运行推理基准测试：

```bash
python3 benchmark_inference.py
```

## 9. 故障排除

### 9.1 常见问题和解决方案

1. **CUDA内存不足**
   - 减小批量大小
   - 使用参数更少的模型
   - 启用内存优化：`paddle.device.cuda.empty_cache()`

2. **推理速度慢**
   - 检查电源模式：`sudo nvpmodel -q`
   - 启用JetPack时钟：`sudo jetson_clocks`
   - 使用TensorRT优化

3. **包安装失败**
   - 尝试从源代码安装
   - 检查兼容版本
   - 必要时使用`--no-deps`标志

### 9.2 监控工具

1. **监控GPU使用情况：**
   ```bash
   sudo tegrastats
   ```

2. **监控系统资源：**
   ```bash
   sudo apt install -y htop
   htop
   ```

3. **监控温度：**
   ```bash
   cat /sys/devices/virtual/thermal/thermal_zone*/temp
   ```

## 10. 后续步骤

成功设置Jetson Xavier NX环境后：

1. **克隆悟空项目代码库**
2. **设置数据库和Web服务器**
3. **为Java和Vue.js配置开发环境**
4. **根据机器学习集成计划开始实施ML集成**

## 11. 参考资料

- [Jetson Xavier NX开发套件文档](https://developer.nvidia.com/embedded/jetson-xavier-nx-developer-kit)
- [PaddlePaddle文档](https://www.paddlepaddle.org.cn/documentation/docs/zh/guides/index_cn.html)
- [PaddleX文档](https://github.com/PaddlePaddle/PaddleX)
- [JetPack文档](https://docs.nvidia.com/jetson/jetpack/introduction/index.html)
- [CUDA文档](https://docs.nvidia.com/cuda/)
