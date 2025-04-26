# Wukong Code Structure

## Directory Structure
<!-- Provide an overview of the directory structure -->

Wukong项目的代码结构分为服务端和客户端两部分：

### 服务端 (WK-1500)

```bash
wukong-server/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── com/
│   │   │   │   ├── wukong/
│   │   │   │   │   ├── api/            # REST API控制器
│   │   │   │   │   ├── config/         # 系统配置
│   │   │   │   │   ├── model/          # 数据模型
│   │   │   │   │   ├── service/        # 业务逻辑服务
│   │   │   │   │   ├── repository/     # 数据访问层
│   │   │   │   │   ├── util/           # 工具类
│   │   │   │   │   ├── ai/             # AI模型集成
│   │   │   │   │   └── Application.java # 应用入口
│   │   ├── resources/
│   │   │   ├── application.properties  # 应用配置
│   │   │   ├── static/                 # 静态资源
│   │   │   └── templates/              # 模板文件
│   ├── test/                           # 测试代码
├── web/                                # 前端代码 (Vue.js)
│   ├── src/
│   │   ├── components/                 # Vue组件
│   │   ├── views/                      # 页面视图
│   │   ├── router/                     # 路由配置
│   │   ├── store/                      # Vuex状态管理
│   │   └── main.js                     # 前端入口
├── ai/                                 # AI模型训练和推理
│   ├── models/                         # 预训练模型
│   ├── training/                       # 训练脚本
│   └── inference/                      # 推理脚本
└── scripts/                            # 部署和维护脚本
```

### 客户端 (WK-T20)

```bash
wukong-client/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   ├── com/
│   │   │   │   │   ├── wukong/
│   │   │   │   │   │   ├── activity/   # Android活动
│   │   │   │   │   │   ├── service/    # 后台服务
│   │   │   │   │   │   ├── model/      # 数据模型
│   │   │   │   │   │   ├── util/       # 工具类
│   │   │   │   │   │   ├── camera/     # 相机控制
│   │   │   │   │   │   ├── detection/  # 图像检测
│   │   │   │   │   │   └── webrtc/     # WebRTC通信
│   │   │   ├── res/                    # 资源文件
│   │   │   └── AndroidManifest.xml     # 应用配置
│   │   ├── test/                       # 测试代码
├── libs/                               # 第三方库
└── assets/                             # 资源文件
```

## Core Modules
<!-- List and describe the core modules -->

### 服务端核心模块

1. **API模块**
   * 提供RESTful API接口
   * 处理客户端请求
   * 实现设备管理、作业流程管理等功能

2. **服务模块**
   * 实现业务逻辑
   * 处理作业流程的创建、更新、发布等操作
   * 管理设备连接和状态

3. **数据模块**
   * 定义数据模型
   * 实现数据持久化
   * 提供数据访问接口

4. **AI模块**
   * 集成深度学习模型
   * 提供模型训练和推理功能
   * 处理图像识别和检测

5. **前端模块**
   * 实现管理界面
   * 提供作业流程设计工具
   * 显示设备状态和作业记录

### 客户端核心模块

1. **相机模块**
   * 控制USB相机
   * 获取图像数据
   * 处理图像预处理

2. **检测模块**
   * 实现基于OpenCV的模板匹配
   * 集成TensorFlow Lite模型
   * 执行图像特征提取和比对

3. **WebRTC模块**
   * 与服务端建立实时通信
   * 传输图像数据
   * 接收AI处理结果

4. **UI模块**
   * 显示实时相机画面
   * 绘制检测框和提示信息
   * 提供用户交互界面

5. **作业执行模块**
   * 管理作业流程的执行
   * 处理基准点搜索和检测点检测
   * 记录作业结果

## Class Hierarchy
<!-- Document the class hierarchy and relationships -->

### 服务端类层次结构

```text
BaseEntity
├── Device
├── JobProcess
│   ├── JobInstruction
│   │   ├── JobItem
│   │   │   ├── BaseSearchArea
│   │   │   ├── BasePoint
│   │   │   └── CheckPoint
└── JobProcessLog
```

### 客户端类层次结构

```text
BaseActivity
├── MainActivity
├── SettingsActivity
└── JobExecutionActivity

BaseService
├── CameraService
├── DetectionService
└── WebRTCService

BaseDetector
├── TemplateDetector
└── TFLiteDetector
```

## Important Files
<!-- List and describe important files in the codebase -->

### 服务端重要文件

1. **Application.java**
   * 应用入口点
   * 配置Spring Boot应用

2. **DeviceController.java**
   * 设备管理API
   * 处理设备绑定、解绑、同步等操作

3. **JobProcessController.java**
   * 作业流程管理API
   * 处理作业流程的创建、更新、发布等操作

4. **JobProcessService.java**
   * 作业流程业务逻辑
   * 实现作业流程的核心功能

5. **AIModelService.java**
   * AI模型服务
   * 管理模型加载和推理

### 客户端重要文件

1. **MainActivity.java**
   * 主界面活动
   * 显示相机预览和检测结果

2. **CameraManager.java**
   * 相机管理器
   * 控制相机操作和图像获取

3. **DetectionManager.java**
   * 检测管理器
   * 协调不同检测方法的使用

4. **WebRTCClient.java**
   * WebRTC客户端
   * 管理与服务端的通信

5. **JobExecutor.java**
   * 作业执行器
   * 控制作业流程的执行逻辑

## Code Conventions
<!-- Document coding conventions and patterns used -->

### 命名约定

* **类名**：使用PascalCase，如`JobProcess`、`BaseSearchArea`
* **方法名**：使用camelCase，如`createJobProcess`、`findBasePoint`
* **变量名**：使用camelCase，如`deviceId`、`jobItemList`
* **常量名**：使用UPPER_SNAKE_CASE，如`MAX_TIMEOUT`、`DEFAULT_IP`
* **包名**：使用小写，如`com.wukong.api`、`com.wukong.service`

### 设计模式

* **MVC模式**：分离模型、视图和控制器
* **依赖注入**：使用Spring框架的依赖注入
* **单例模式**：用于全局服务和管理器
* **工厂模式**：创建检测器和处理器
* **观察者模式**：处理事件和通知

### 代码风格

* 使用4空格缩进
* 方法和类应有JavaDoc注释
* 遵循阿里巴巴Java开发手册规范
* 使用lombok简化getter/setter
* 使用统一的异常处理机制

## Build Process
<!-- Explain the build process and tools used -->

### 服务端构建

* **构建工具**：Maven
* **打包格式**：JAR
* **构建命令**：`mvn clean package`
* **部署方式**：将JAR文件部署到Jetson Xavier NX设备

### 前端构建

* **构建工具**：npm/yarn
* **打包工具**：Webpack
* **构建命令**：`npm run build`
* **部署方式**：将构建产物复制到服务端静态资源目录

### 客户端构建

* **构建工具**：Gradle
* **打包格式**：APK
* **构建命令**：`./gradlew assembleRelease`
* **部署方式**：通过ADB安装到WK-T20设备

## Testing
<!-- Describe the testing approach and framework -->

### 服务端测试

* **单元测试**：JUnit 5
* **Mock框架**：Mockito
* **API测试**：Spring Test
* **测试覆盖率工具**：JaCoCo

### 客户端测试

* **单元测试**：JUnit 4
* **UI测试**：Espresso
* **性能测试**：Android Profiler
* **集成测试**：自定义测试框架

### AI模型测试

* **准确性测试**：使用标注数据集
* **性能测试**：测量推理时间和资源占用
* **稳定性测试**：长时间运行测试

## Dependencies
<!-- List external dependencies and their purposes -->

### 服务端依赖

* **Spring Boot**：应用框架
* **Spring Data JPA**：数据访问
* **H2/MySQL**：数据库
* **PaddlePaddle**：深度学习框架
* **PaddleX**：视觉模型工具集
* **WebRTC**：实时通信

### 客户端依赖

* **AndroidX**：Android支持库
* **OpenCV**：计算机视觉库
* **TensorFlow Lite**：移动端深度学习框架
* **WebRTC**：实时通信
* **Retrofit**：HTTP客户端
* **Glide**：图像加载和缓存

## Extension Points
<!-- Document how to extend the system -->

### 扩展AI模型

1. **添加新模型**
   * 在`ai/models`目录下添加新模型文件
   * 在`AIModelService`中注册新模型
   * 实现模型加载和推理接口

2. **自定义训练流程**
   * 修改`ai/training`目录下的训练脚本
   * 配置数据预处理和增强
   * 调整模型参数和训练策略

### 扩展检测功能

1. **添加新检测器**
   * 继承`BaseDetector`类
   * 实现检测方法
   * 在`DetectionManager`中注册新检测器

2. **自定义检测参数**
   * 在检测点配置中添加新参数
   * 在检测逻辑中使用新参数
   * 更新UI以支持新参数配置

### 扩展设备支持

1. **添加新设备类型**
   * 在`Device`模型中添加新设备类型
   * 实现设备特定的通信协议
   * 更新设备管理UI

## Code Examples
<!-- Provide examples of common code patterns -->

### 服务端示例：创建作业流程

```java
@Service
public class JobProcessService {

    @Autowired
    private JobProcessRepository jobProcessRepository;

    @Autowired
    private DeviceService deviceService;

    public JobProcess createJobProcess(JobProcessDTO dto) {
        // 验证设备
        Device device = deviceService.findById(dto.getDeviceId())
            .orElseThrow(() -> new DeviceNotFoundException(dto.getDeviceId()));

        // 创建作业流程
        JobProcess jobProcess = new JobProcess();
        jobProcess.setName(dto.getName());
        jobProcess.setDescription(dto.getDescription());
        jobProcess.setDevice(device);
        jobProcess.setStatus(JobProcessStatus.DRAFT);

        // 保存并返回
        return jobProcessRepository.save(jobProcess);
    }

    // 其他方法...
}
```

### 客户端示例：基准点检测

```java
public class BasePointDetector {

    private final Context context;
    private final TFLiteInterpreter interpreter;

    public BasePointDetector(Context context) {
        this.context = context;
        this.interpreter = new TFLiteInterpreter(context, "base_point_model.tflite");
    }

    public Point detectBasePoint(Mat image, Rect searchArea) {
        // 裁剪搜索区域
        Mat roi = new Mat(image, searchArea);

        // 预处理图像
        Mat processed = preprocess(roi);

        // 执行模型推理
        float[] result = interpreter.run(processed);

        // 解析结果
        Point point = parseResult(result, searchArea);

        // 释放资源
        roi.release();
        processed.release();

        return point;
    }

    // 其他方法...
}
```
