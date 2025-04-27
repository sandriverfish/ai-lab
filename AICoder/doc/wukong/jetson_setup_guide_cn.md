# Jetson Xavier NX 悟空机器学习集成环境搭建指南

本指南提供了为悟空机器学习集成项目搭建Nvidia Jetson Xavier NX开发环境的详细步骤。

> **注意**：本指南基于实际环境搭建经验编写，详细的原始环境搭建过程记录可参考：[wukong.paddlex环境搭建.md](../ref_materials/edge_server/wukong.paddlex环境搭建.md)

注意：在Jetson Xavier NX上安装PaddlePaddle-GPU的唯一可靠方法是源码编译，直接使用x86预编译包会导致架构和CUDA版本冲突。

## 1. 硬件要求

- Nvidia Jetson Xavier NX开发套件
- 电源适配器（19V）
- NvME SSD卡（推荐256GB+）
- USB键盘和鼠标
- HDMI显示器
- 以太网电缆或Wi-Fi连接
- 可选：USB网络摄像头或兼容的工业相机用于测试

```bash
ssh nvidia@192.168.1.91 "cat /etc/nv_tegra_release"

# R35 (release), REVISION: 6.1, GCID: 39721438, BOARD: t186ref, EABI: aarch64, DATE: Tue Mar  4 10:13:09 UTC 2025
```



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

2. **安装PaddlePaddle 3.0.0 GPU版本：**

   > **注意**：对于Jetson Xavier NX，我们需要使用预编译的wheel包，而不是通过pip直接安装。

   从百度网盘下载预编译的wheel包：

   ```bash
   # 下载链接
   # 链接: https://pan.baidu.com/s/1Baw19iZv5N_9kih4i8vtbA?pwd=geaa 提取码: geaa

   # 升级pip和相关工具
   python3 -m pip install --upgrade pip setuptools wheel

   # 安装下载的wheel包
   pip install paddlepaddle_gpu-3.0.0-cp38-cp38-linux_aarch64.whl

   # 可能需要安装的额外依赖
   pip install onnx
   ```

3. **修复numpy.bool兼容性问题：**

   ```bash
   # 如果运行时出现np.bool错误，需要进行以下修复
   sudo vi /usr/lib/python3/dist-packages/pandas/util/testing.py

   # 在import numpy as np行后添加：
   np.bool = np.bool_
   ```

4. **验证PaddlePaddle安装：**

   ```bash
   python3 -c "import paddle; print(paddle.__version__); print(paddle.device.is_compiled_with_cuda())"
   ```

## 4. PaddleX安装

1. **安装PaddleX：**

   同样，我们需要使用预编译的wheel包：

   ```bash
   # 使用从百度网盘下载的wheel包
   pip install paddlex-3.0.0-py3-none-any.whl
   ```

2. **验证PaddleX安装：**

   ```bash
   python3 -c "import paddlex; print(paddlex.__version__)"
   ```

3. **测试PaddleX功能：**

   ```bash
   # 上传测试图片后运行
   paddlex --pipeline OCR --input 测试图片.png --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False --device gpu:0 --save_path ./output
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
python3 -m venv venv
source venv/bin/activate

# 升级pip和工具
pip install --upgrade pip setuptools wheel

# 安装基本依赖
pip install numpy matplotlib pillow opencv-python-headless

# 安装PaddlePaddle和PaddleX
# 注意：这里需要使用之前下载的wheel包
# 假设wheel包已下载到~/Downloads目录
pip install ~/Downloads/paddlepaddle_gpu-3.0.0-cp38-cp38-linux_aarch64.whl
# pip install paddlepaddle_gpu-3.0.0-cp38-cp38-linux_aarch64.whl

pip install ~/Downloads/paddlex-3.0.0-py3-none-any.whl

# 安装其他有用的工具
pip install tqdm pyyaml scikit-learn

# 创建项目目录结构
mkdir -p data/{raw,processed,annotations}
mkdir -p models/{pretrained,trained}
mkdir -p scripts
mkdir -p utils
mkdir -p configs
mkdir -p logs

# 创建验证脚本
cat > scripts/verify_env.py << 'EOF'
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
print("GPU数量:", paddle.device.get_device_count())

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
EOF

# 运行验证脚本
python scripts/verify_env.py

```
创建项目配置文件
```bash
# 创建配置目录和文件
cat > configs/config.yaml << 'EOF'
# 悟空机器学习集成项目配置

# 路径配置
paths:
  data:
    raw: data/raw
    processed: data/processed
    annotations: data/annotations
  models:
    pretrained: models/pretrained
    trained: models/trained
  logs: logs

# 模型配置
models:
  detection:
    name: "pp-picodet-s-320"
    input_shape: [320, 320]
  classification:
    name: "mobilenetv3_small"
    input_shape: [224, 224]

# 训练配置
training:
  batch_size: 8
  learning_rate: 0.001
  epochs: 50
  early_stopping: 10

# 推理配置
inference:
  detection_threshold: 0.5
  classification_threshold: 0.7
  template_matching_threshold: 0.8
  hybrid_mode: true
EOF

```
工具函数
```bash
# 创建工具模块
cat > utils/__init__.py << 'EOF'
# 工具函数包
EOF

cat > utils/config.py << 'EOF'
import os
import yaml

def load_config(config_path):
    """加载YAML配置文件"""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def get_project_root():
    """获取项目根目录"""
    # 假设此文件位于 project_root/utils/config.py
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    return project_root
EOF

cat > utils/visualization.py << 'EOF'
import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_detection(image, bbox, label=None, score=None, color=(0, 255, 0), thickness=2):
    """在图像上绘制检测框"""
    x1, y1, x2, y2 = map(int, bbox)
    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    
    if label:
        text = label
        if score is not None:
            text += f": {score:.2f}"
        cv2.putText(image, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return image

def visualize_results(image, results, save_path=None):
    """可视化检测结果"""
    vis_image = image.copy()
    
    for result in results:
        bbox = result['bbox']
        label = result.get('category', '')
        score = result.get('score', None)
        draw_detection(vis_image, bbox, label, score)
    
    if save_path:
        cv2.imwrite(save_path, vis_image)
    
    return vis_image
EOF
```
模板匹配基准测试脚本
```bash
# 创建基准测试脚本
cat > scripts/benchmark_template_matching.py << 'EOF'
import os
import time
import cv2
import numpy as np
import argparse
from tqdm import tqdm
import sys
import json

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import load_config, get_project_root

def template_matching(image, template, method=cv2.TM_CCOEFF_NORMED):
    """执行模板匹配"""
    start_time = time.time()
    result = cv2.matchTemplate(image, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    elapsed_time = time.time() - start_time
    
    # 根据匹配方法确定最佳位置
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        best_loc = min_loc
        best_val = 1 - min_val  # 转换为相似度
    else:
        best_loc = max_loc
        best_val = max_val
    
    h, w = template.shape[:2]
    bbox = (best_loc[0], best_loc[1], best_loc[0] + w, best_loc[1] + h)
    
    return {
        'bbox': bbox,
        'similarity': best_val,
        'time': elapsed_time
    }

def run_benchmark(image_dir, template_dir, output_file=None):
    """运行模板匹配基准测试"""
    # 加载图像和模板
    images = []
    templates = []
    image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) 
                  if f.endswith(('.jpg', '.jpeg', '.png'))]
    template_paths = [os.path.join(template_dir, f) for f in os.listdir(template_dir) 
                     if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    print(f"找到 {len(image_paths)} 张图像和 {len(template_paths)} 个模板")
    
    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is not None:
            images.append((os.path.basename(img_path), img))
    
    for tmpl_path in template_paths:
        tmpl = cv2.imread(tmpl_path)
        if tmpl is not None:
            templates.append((os.path.basename(tmpl_path), tmpl))
    
    # 运行基准测试
    results = []
    total_time = 0
    total_matches = 0
    
    for img_name, img in tqdm(images, desc="处理图像"):
        for tmpl_name, tmpl in templates:
            # 确保模板不大于图像
            if tmpl.shape[0] > img.shape[0] or tmpl.shape[1] > img.shape[1]:
                continue
            
            # 执行模板匹配
            result = template_matching(img, tmpl)
            
            # 记录结果
            match_info = {
                'image': img_name,
                'template': tmpl_name,
                'bbox': result['bbox'],
                'similarity': float(result['similarity']),
                'time': float(result['time'])
            }
            results.append(match_info)
            
            total_time += result['time']
            total_matches += 1
    
    # 计算统计信息
    avg_time = total_time / total_matches if total_matches > 0 else 0
    avg_similarity = sum(r['similarity'] for r in results) / len(results) if results else 0
    
    summary = {
        'total_images': len(images),
        'total_templates': len(templates),
        'total_matches': total_matches,
        'average_time': avg_time,
        'average_similarity': avg_similarity,
        'results': results
    }
    
    # 保存结果
    if output_file:
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)
    
    print(f"基准测试完成!")
    print(f"平均匹配时间: {avg_time*1000:.2f} ms")
    print(f"平均相似度: {avg_similarity:.4f}")
    
    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="模板匹配基准测试")
    parser.add_argument("--image_dir", type=str, help="图像目录")
    parser.add_argument("--template_dir", type=str, help="模板目录")
    parser.add_argument("--output", type=str, default="benchmark_results.json", help="输出文件")
    args = parser.parse_args()
    
    # 如果未指定目录，使用配置中的默认目录
    project_root = get_project_root()
    config_path = os.path.join(project_root, "configs", "config.yaml")
    config = load_config(config_path)
    
    image_dir = args.image_dir or os.path.join(project_root, config['paths']['data']['raw'])
    template_dir = args.template_dir or os.path.join(project_root, config['paths']['data']['processed'])
    output_file = os.path.join(project_root, args.output)
    
    run_benchmark(image_dir, template_dir, output_file)
EOF
```

混合识别方法原型
```bash
# 创建混合识别方法原型脚本
cat > scripts/hybrid_detection.py << 'EOF'
import os
import sys
import cv2
import numpy as np
import paddle
import paddlex as pdx
import time
import argparse

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import load_config, get_project_root
from utils.visualization import visualize_results

class HybridDetector:
    """混合检测器：结合模板匹配和深度学习"""
    
    def __init__(self, config_path=None):
        """初始化混合检测器"""
        project_root = get_project_root()
        if config_path is None:
            config_path = os.path.join(project_root, "configs", "config.yaml")
        
        self.config = load_config(config_path)
        self.template_matching_threshold = self.config['inference']['template_matching_threshold']
        self.detection_threshold = self.config['inference']['detection_threshold']
        self.hybrid_mode = self.config['inference']['hybrid_mode']
        
        # 模型路径
        self.model = None
        self.model_path = os.path.join(
            project_root, 
            self.config['paths']['models']['pretrained'],
            "model.pdx"  # 假设模型文件名为model.pdx
        )
        
        # 如果模型文件存在，加载模型
        if os.path.exists(self.model_path):
            try:
                self.model = pdx.load_model(self.model_path)
                print(f"已加载模型: {self.model_path}")
            except Exception as e:
                print(f"加载模型失败: {e}")
                self.model = None
    
    def template_matching(self, image, template, method=cv2.TM_CCOEFF_NORMED):
        """执行模板匹配"""
        # 确保图像和模板是灰度图
        if len(image.shape) == 3:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            image_gray = image
            
        if len(template.shape) == 3:
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        else:
            template_gray = template
        
        # 执行模板匹配
        result = cv2.matchTemplate(image_gray, template_gray, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # 根据匹配方法确定最佳位置
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            best_loc = min_loc
            similarity = 1 - min_val
        else:
            best_loc = max_loc
            similarity = max_val
        
        h, w = template.shape[:2]
        bbox = [best_loc[0], best_loc[1], best_loc[0] + w, best_loc[1] + h]
        
        return {
            'bbox': bbox,
            'similarity': similarity,
            'category': 'template_match',
            'score': similarity
        }
    
    def deep_learning_detection(self, image):
        """执行深度学习检测"""
        if self.model is None:
            return []
        
        try:
            # 执行推理
            results = self.model.predict(image)
            
            # 过滤低置信度结果
            filtered_results = []
            for result in results:
                if result['score'] >= self.detection_threshold:
                    filtered_results.append(result)
            
            return filtered_results
        except Exception as e:
            print(f"深度学习检测失败: {e}")
            return []
    
    def analyze_image(self, image):
        """分析图像质量，决定使用哪种方法"""
        # 计算图像模糊度
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur_metric = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # 计算亮度
        brightness = np.mean(gray)
        
        # 根据图像质量决定方法
        if blur_metric < 100:  # 模糊图像
            return 'deep_learning'
        elif brightness < 50 or brightness > 200:  # 亮度异常
            return 'deep_learning'
        else:
            return 'hybrid'
    
    def detect(self, image, template=None):
        """执行混合检测"""
        results = []
        method = self.analyze_image(image) if self.hybrid_mode else 'template_matching'
        
        if method == 'template_matching' or method == 'hybrid':
            if template is not None:
                tm_result = self.template_matching(image, template)
                if tm_result['similarity'] >= self.template_matching_threshold:
                    results.append(tm_result)
        
        if method == 'deep_learning' or method == 'hybrid':
            if self.model is not None:
                dl_results = self.deep_learning_detection(image)
                results.extend(dl_results)
        
        # 如果是混合模式，可能需要合并结果或选择最佳结果
        if method == 'hybrid' and len(results) > 1:
            # 这里可以实现更复杂的结果融合逻辑
            # 简单起见，我们按置信度排序并选择最佳结果
            results = sorted(results, key=lambda x: x['score'], reverse=True)
        
        return results

def main():
    parser = argparse.ArgumentParser(description="混合检测演示")
    parser.add_argument("--image", type=str, required=True, help="输入图像路径")
    parser.add_argument("--template", type=str, help="模板图像路径")
    parser.add_argument("--output", type=str, help="输出图像路径")
    parser.add_argument("--config", type=str, help="配置文件路径")
    args = parser.parse_args()
    
    # 加载图像
    image = cv2.imread(args.image)
    if image is None:
        print(f"无法加载图像: {args.image}")
        return
    
    # 加载模板（如果提供）
    template = None
    if args.template:
        template = cv2.imread(args.template)
        if template is None:
            print(f"无法加载模板: {args.template}")
    
    # 创建检测器
    detector = HybridDetector(args.config)
    
    # 执行检测
    start_time = time.time()
    results = detector.detect(image, template)
    elapsed_time = time.time() - start_time
    
    # 打印结果
    print(f"检测完成! 耗时: {elapsed_time*1000:.2f} ms")
    print(f"检测到 {len(results)} 个对象:")
    for i, result in enumerate(results):
        print(f"  结果 {i+1}:")
        print(f"    类别: {result.get('category', 'unknown')}")
        print(f"    置信度: {result.get('score', 0):.4f}")
        print(f"    边界框: {result.get('bbox', [0, 0, 0, 0])}")
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
# 平均矩阵乘法时间: 30.26 ms
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

# 平均推理时间: 73.14 ms
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
下一步计划
现在您的环境已经完全设置好了，您可以开始实施机器学习集成计划的第一阶段：

收集和准备训练数据：
从V1.0系统中导出现有产品图像和模板
创建标注数据
基准测试：
创建模板匹配基准测试脚本
测量当前模板匹配方法的性能
下载预训练模型：
下载PaddleDetection中的轻量级模型（如PP-PicoDet）
下载PaddleClas中的分类模型（如MobileNetV3）
开发混合识别方法原型：
实现模板匹配模块
实现深度学习推理模块
实现决策引擎
您的环境设置非常成功！现在您可以开始实际的开发工作了。

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
