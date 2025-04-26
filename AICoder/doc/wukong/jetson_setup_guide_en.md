# Jetson Xavier NX Setup Guide for Wukong ML Integration

This guide provides step-by-step instructions for setting up the Nvidia Jetson Xavier NX development environment for the Wukong ML integration project.

## 1. Hardware Requirements

- Nvidia Jetson Xavier NX Developer Kit
- Power adapter (19V)
- MicroSD card (64GB+ recommended)
- USB keyboard and mouse
- HDMI display
- Ethernet cable or Wi-Fi connection
- Optional: USB webcam or compatible industrial camera for testing

## 2. Initial System Setup

### 2.1 Flash JetPack 5.1.4

1. **On a host computer:**
   - Download and install [NVIDIA SDK Manager](https://developer.nvidia.com/nvidia-sdk-manager)
   - Connect the host computer to the internet
   - Launch SDK Manager and log in with your NVIDIA developer account

2. **Select the following options:**
   - Product Category: Jetson
   - Hardware Configuration: Jetson Xavier NX
   - Target Operating System: JetPack 5.1.4 (L4T 35.4.1)

3. **Follow the SDK Manager instructions to:**
   - Download the required components
   - Flash the Jetson Xavier NX
   - Install the selected components

4. **Complete the initial setup on the Jetson:**
   - Create a username and password
   - Configure system settings
   - Connect to Wi-Fi or Ethernet

### 2.2 System Configuration

1. **Update the system:**
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Install essential development tools:**
   ```bash
   sudo apt install -y build-essential git cmake python3-dev python3-pip
   sudo apt install -y libopencv-dev libopenblas-dev
   ```

3. **Configure power mode for optimal performance:**
   ```bash
   sudo nvpmodel -m 2  # 15W 6-core mode
   sudo jetson_clocks   # Set clocks to maximum
   ```

4. **Set up swap space (recommended for ML training):**
   ```bash
   sudo fallocate -l 8G /var/swapfile
   sudo chmod 600 /var/swapfile
   sudo mkswap /var/swapfile
   sudo swapon /var/swapfile
   echo '/var/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab
   ```

## 3. PaddlePaddle Installation

### 3.1 Install PaddlePaddle Dependencies

1. **Install required packages:**
   ```bash
   sudo apt install -y python3-pip python3-dev python3-matplotlib
   sudo apt install -y libatlas-base-dev libopenblas-dev libblas-dev
   sudo apt install -y liblapack-dev patchelf gfortran
   ```

2. **Upgrade pip and install additional Python packages:**
   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install numpy protobuf==3.20.3 wheel setuptools
   python3 -m pip install decorator attrs six psutil Pillow
   ```

### 3.2 Install PaddlePaddle GPU Version

1. **Install CUDA toolkit and cuDNN (should be included in JetPack):**
   ```bash
   # Verify CUDA installation
   nvcc --version
   
   # Verify cuDNN installation
   dpkg -l | grep cudnn
   ```

2. **Install PaddlePaddle 3.0.0-rc GPU version:**
   ```bash
   python3 -m pip install paddlepaddle-gpu==3.0.0rc0.post110 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
   ```

3. **Verify PaddlePaddle installation:**
   ```bash
   python3 -c "import paddle; print(paddle.__version__); print(paddle.device.is_compiled_with_cuda())"
   ```

## 4. PaddleX Installation

1. **Install PaddleX 3.0.0-rc:**
   ```bash
   python3 -m pip install paddlex==3.0.0rc
   ```

2. **Verify PaddleX installation:**
   ```bash
   python3 -c "import paddlex; print(paddlex.__version__)"
   ```

## 5. Install Additional Libraries

1. **Install OpenCV with CUDA support (if not already installed):**
   ```bash
   # OpenCV should be included in JetPack, verify with:
   python3 -c "import cv2; print(cv2.__version__); print(cv2.getBuildInformation())"
   ```

2. **Install visualization and utility libraries:**
   ```bash
   python3 -m pip install matplotlib scikit-learn pandas
   python3 -m pip install visualdl tensorboard
   ```

3. **Install additional PaddlePaddle ecosystem packages:**
   ```bash
   python3 -m pip install paddleslim  # For model optimization
   python3 -m pip install paddle2onnx  # For model conversion
   ```

## 6. Set Up Project Environment

### 6.1 Create Project Directory

```bash
mkdir -p ~/wukong-ml
cd ~/wukong-ml
```

### 6.2 Clone Necessary Repositories

```bash
# Clone PaddleDetection for object detection models
git clone https://github.com/PaddlePaddle/PaddleDetection.git
cd PaddleDetection
git checkout release/2.6
pip install -r requirements.txt
python setup.py install
cd ..

# Clone PaddleClas for classification models
git clone https://github.com/PaddlePaddle/PaddleClas.git
cd PaddleClas
git checkout release/2.5
pip install -r requirements.txt
python setup.py install
cd ..
```

### 6.3 Set Up Virtual Environment (Optional)

If you prefer to use a virtual environment:

```bash
sudo apt install -y python3-venv
python3 -m venv wukong-env
source wukong-env/bin/activate

# Install all packages in the virtual environment
# (Repeat the installation steps above)
```

## 7. Test the Environment

### 7.1 Basic PaddlePaddle Test

Create a file named `test_paddle.py`:

```python
import paddle
import numpy as np

# Create a simple neural network
class SimpleNet(paddle.nn.Layer):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = paddle.nn.Linear(10, 1)
        
    def forward(self, x):
        return self.fc(x)

# Test with random data
model = SimpleNet()
x = paddle.randn([5, 10], dtype='float32')
y = model(x)

print("Model output shape:", y.shape)
print("Paddle is using GPU:", paddle.device.is_compiled_with_cuda())
print("Current device:", paddle.device.get_device())
```

Run the test:

```bash
python3 test_paddle.py
```

### 7.2 Test with a Pre-trained Model

Create a file named `test_pretrained.py`:

```python
import paddlex as pdx
import cv2
import numpy as np

# Download a pre-trained model
model = pdx.load_model('https://bj.bcebos.com/paddlex/models/xiaoduxiong_epoch_12.pdx')

# Test with a sample image
img = cv2.imread('path/to/test/image.jpg')
if img is None:
    # Create a test image if none is available
    img = np.random.randint(0, 255, (640, 480, 3), dtype=np.uint8)
    cv2.imwrite('test_image.jpg', img)
    img = cv2.imread('test_image.jpg')

# Perform inference
result = model.predict(img)
print("Inference result:", result)
```

Run the test:

```bash
python3 test_pretrained.py
```

## 8. Performance Benchmarking

### 8.1 GPU Performance Test

Create a file named `benchmark_gpu.py`:

```python
import paddle
import time
import numpy as np

def benchmark_matmul(size=1000, iterations=100):
    # Create random matrices
    a = paddle.randn([size, size], dtype='float32')
    b = paddle.randn([size, size], dtype='float32')
    
    # Warm-up
    for _ in range(10):
        c = paddle.matmul(a, b)
    
    # Benchmark
    start_time = time.time()
    for _ in range(iterations):
        c = paddle.matmul(a, b)
        paddle.device.cuda.synchronize()
    end_time = time.time()
    
    elapsed = end_time - start_time
    return elapsed / iterations

# Run benchmark
avg_time = benchmark_matmul(size=2000, iterations=50)
print(f"Average matrix multiplication time: {avg_time*1000:.2f} ms")
```

Run the benchmark:

```bash
python3 benchmark_gpu.py
```

### 8.2 Inference Speed Test

Create a file named `benchmark_inference.py`:

```python
import paddle
import paddlex as pdx
import time
import numpy as np

# Create a simple test model
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

# Create model and test data
model = TestModel()
model.eval()
test_input = paddle.randn([1, 3, 480, 640], dtype='float32')

# Warm-up
for _ in range(10):
    _ = model(test_input)
    paddle.device.cuda.synchronize()

# Benchmark
iterations = 100
start_time = time.time()
for _ in range(iterations):
    _ = model(test_input)
    paddle.device.cuda.synchronize()
end_time = time.time()

avg_time = (end_time - start_time) / iterations
print(f"Average inference time: {avg_time*1000:.2f} ms")
```

Run the inference benchmark:

```bash
python3 benchmark_inference.py
```

## 9. Troubleshooting

### 9.1 Common Issues and Solutions

1. **CUDA Out of Memory**
   - Reduce batch size
   - Use model with fewer parameters
   - Enable memory optimization: `paddle.device.cuda.empty_cache()`

2. **Slow Inference**
   - Check power mode: `sudo nvpmodel -q`
   - Enable JetPack clocks: `sudo jetson_clocks`
   - Use TensorRT optimization

3. **Package Installation Failures**
   - Try installing from source
   - Check for compatible versions
   - Use `--no-deps` flag if necessary

### 9.2 Monitoring Tools

1. **Monitor GPU usage:**
   ```bash
   sudo tegrastats
   ```

2. **Monitor system resources:**
   ```bash
   sudo apt install -y htop
   htop
   ```

3. **Monitor temperature:**
   ```bash
   cat /sys/devices/virtual/thermal/thermal_zone*/temp
   ```

## 10. Next Steps

After successfully setting up the Jetson Xavier NX environment:

1. **Clone the Wukong project repository**
2. **Set up the database and web server**
3. **Configure the development environment for Java and Vue.js**
4. **Begin implementing the ML integration according to the ML integration plan**

## 11. References

- [Jetson Xavier NX Developer Kit Documentation](https://developer.nvidia.com/embedded/jetson-xavier-nx-developer-kit)
- [PaddlePaddle Documentation](https://www.paddlepaddle.org.cn/documentation/docs/en/guides/index_en.html)
- [PaddleX Documentation](https://github.com/PaddlePaddle/PaddleX)
- [JetPack Documentation](https://docs.nvidia.com/jetson/jetpack/introduction/index.html)
- [CUDA Documentation](https://docs.nvidia.com/cuda/)
