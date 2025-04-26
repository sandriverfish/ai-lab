# 悟空系统 V1.5 数据库设计

本文档描述了悟空系统V1.5版本的数据库设计，基于V1.0版本的数据库结构进行扩展，主要增加了对机器学习模型和数据集的支持。

## 1. 设计概述

### 1.1 设计目标

- 保留V1.0版本的核心功能和数据结构
- 添加对机器学习模型和数据集的支持
- 简化系统架构，适应单一设备部署模式
- 优化数据存储和访问效率
- 支持模型训练和推理的数据需求

### 1.2 主要变更

相比V1.0版本，V1.5版本的数据库设计主要有以下变更：

1. **添加机器学习相关表**
   - 模型表：存储机器学习模型信息
   - 数据集表：存储训练和测试数据集信息
   - 特征表：存储产品和组件的特征向量

2. **简化设备相关表**
   - 移除多终端设计，适应单一设备部署模式
   - 保留设备配置和状态信息

3. **增强作业流程表**
   - 添加对混合识别方法的支持
   - 增加模型选择和配置字段

4. **优化校验点表**
   - 添加对深度学习特征的支持
   - 增加置信度和阈值设置

## 2. 数据库表结构

### 2.1 保留的V1.0核心表

以下表结构基本保留V1.0版本的设计，仅做少量调整：

- `wukong_user`：用户表
- `job_process`：作业流程表
- `job_instruction`：作业指示表
- `job_item`：作业项目表
- `job_item_point`：校验点表
- `job_process_log`：作业流程日志表
- `job_item_log`：作业项目日志表
- `job_item_point_log`：校验点日志表
- `config`：配置表

### 2.2 新增的机器学习相关表

#### 2.2.1 AI模型表 (ai_model)

```sql
CREATE TABLE IF NOT EXISTS ai_model (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 模型名称
    type ENUM('DETECTION', 'CLASSIFICATION', 'FEATURE_EXTRACTION', 'HYBRID') NOT NULL, -- 模型类型
    framework ENUM('PADDLEPADDLE', 'OPENCV', 'HYBRID') NOT NULL DEFAULT 'PADDLEPADDLE', -- 框架类型
    version VARCHAR(20) NOT NULL,                       -- 模型版本
    file_path VARCHAR(255) NOT NULL,                    -- 模型文件路径
    file_size BIGINT DEFAULT 0,                         -- 模型文件大小
    file_checksum VARCHAR(64),                          -- 模型文件校验值
    config_json TEXT,                                   -- 模型配置（JSON格式）
    description TEXT,                                   -- 描述
    is_active TINYINT(1) DEFAULT 0,                     -- 是否激活
    accuracy DECIMAL(5,2),                              -- 准确率
    inference_time INT,                                 -- 推理时间（毫秒）
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0                        -- 删除标记
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### 2.2.2 数据集表 (dataset)

```sql
CREATE TABLE IF NOT EXISTS dataset (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 数据集名称
    type ENUM('TRAINING', 'VALIDATION', 'TEST') NOT NULL, -- 数据集类型
    directory_path VARCHAR(255) NOT NULL,               -- 数据集目录路径
    total_images INT DEFAULT 0,                         -- 图像总数
    annotated_images INT DEFAULT 0,                     -- 已标注图像数
    format ENUM('VOC', 'COCO', 'CUSTOM') NOT NULL,      -- 数据集格式
    config_json TEXT,                                   -- 数据集配置（JSON格式）
    description TEXT,                                   -- 描述
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0                        -- 删除标记
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### 2.2.3 产品模板表 (product_template)

```sql
CREATE TABLE IF NOT EXISTS product_template (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 产品名称
    job_process_id BIGINT,                              -- 关联的作业流程ID
    feature_vector MEDIUMBLOB,                          -- 特征向量（二进制格式）
    feature_json TEXT,                                  -- 特征描述（JSON格式）
    thumbnail VARCHAR(255),                             -- 缩略图路径
    description TEXT,                                   -- 描述
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,                       -- 删除标记
    FOREIGN KEY (job_process_id) REFERENCES job_process(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### 2.2.4 组件模板表 (component_template)

```sql
CREATE TABLE IF NOT EXISTS component_template (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 组件名称
    product_template_id BIGINT,                         -- 关联的产品模板ID
    job_item_point_id BIGINT,                           -- 关联的校验点ID
    feature_vector MEDIUMBLOB,                          -- 特征向量（二进制格式）
    feature_json TEXT,                                  -- 特征描述（JSON格式）
    thumbnail VARCHAR(255),                             -- 缩略图路径
    description TEXT,                                   -- 描述
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,                       -- 删除标记
    FOREIGN KEY (product_template_id) REFERENCES product_template(id) ON DELETE CASCADE,
    FOREIGN KEY (job_item_point_id) REFERENCES job_item_point(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### 2.2.5 训练任务表 (training_job)

```sql
CREATE TABLE IF NOT EXISTS training_job (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 训练任务名称
    model_id BIGINT,                                    -- 关联的模型ID（如果是新模型则为NULL）
    dataset_id BIGINT NOT NULL,                         -- 关联的数据集ID
    status ENUM('PENDING', 'RUNNING', 'COMPLETED', 'FAILED') NOT NULL DEFAULT 'PENDING', -- 任务状态
    config_json TEXT,                                   -- 训练配置（JSON格式）
    result_json TEXT,                                   -- 训练结果（JSON格式）
    start_time DATETIME,                                -- 开始时间
    end_time DATETIME,                                  -- 结束时间
    log_file VARCHAR(255),                              -- 日志文件路径
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES ai_model(id) ON DELETE SET NULL,
    FOREIGN KEY (dataset_id) REFERENCES dataset(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### 2.3 修改的表结构

#### 2.3.1 设备表 (device)

简化设备表，适应单一设备部署模式：

```sql
CREATE TABLE IF NOT EXISTS device (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 设备名称
    hardware_code VARCHAR(50),                          -- 硬件编码
    device_type ENUM('JETSON_XAVIER_NX', 'OTHER') NOT NULL DEFAULT 'JETSON_XAVIER_NX', -- 设备类型
    ip_address VARCHAR(45),                             -- IP地址
    mac_address VARCHAR(17),                            -- MAC地址
    status ENUM('ACTIVE', 'INACTIVE', 'MAINTENANCE') NOT NULL DEFAULT 'ACTIVE', -- 设备状态
    system_version VARCHAR(50),                         -- 系统版本
    app_version VARCHAR(50),                            -- 应用版本
    config_json TEXT,                                   -- 设备配置（JSON格式）
    last_heartbeat DATETIME,                            -- 最后心跳时间
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0                        -- 删除标记
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### 2.3.2 相机表 (camera)

新增相机表，管理直接连接的USB相机：

```sql
CREATE TABLE IF NOT EXISTS camera (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100) NOT NULL,                         -- 相机名称
    device_id BIGINT NOT NULL,                          -- 关联的设备ID
    camera_index INT NOT NULL,                          -- 相机索引
    camera_type VARCHAR(50),                            -- 相机类型
    resolution_width INT DEFAULT 3840,                  -- 分辨率宽度
    resolution_height INT DEFAULT 2160,                 -- 分辨率高度
    fps INT DEFAULT 30,                                 -- 帧率
    config_json TEXT,                                   -- 相机配置（JSON格式）
    status ENUM('CONNECTED', 'DISCONNECTED', 'ERROR') NOT NULL DEFAULT 'DISCONNECTED', -- 相机状态
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### 2.3.3 作业流程表 (job_process)

扩展作业流程表，添加对机器学习模型的支持：

```sql
ALTER TABLE job_process
ADD COLUMN detection_mode ENUM('TEMPLATE_MATCHING', 'AI_MODEL', 'HYBRID') NOT NULL DEFAULT 'TEMPLATE_MATCHING' AFTER is_published,
ADD COLUMN ai_model_id BIGINT AFTER detection_mode,
ADD COLUMN detection_config_json TEXT AFTER ai_model_id,
ADD FOREIGN KEY (ai_model_id) REFERENCES ai_model(id) ON DELETE SET NULL;
```

#### 2.3.4 校验点表 (job_item_point)

扩展校验点表，添加对深度学习特征的支持：

```sql
ALTER TABLE job_item_point
ADD COLUMN detection_mode ENUM('TEMPLATE_MATCHING', 'AI_MODEL', 'HYBRID') NOT NULL DEFAULT 'TEMPLATE_MATCHING' AFTER similarity,
ADD COLUMN feature_vector MEDIUMBLOB AFTER detection_mode,
ADD COLUMN confidence_threshold DECIMAL(3,2) DEFAULT 0.70 AFTER feature_vector,
ADD COLUMN detection_config_json TEXT AFTER confidence_threshold;
```

#### 2.3.5 校验点日志表 (job_item_point_log)

扩展校验点日志表，记录AI检测结果：

```sql
ALTER TABLE job_item_point_log
ADD COLUMN detection_mode ENUM('TEMPLATE_MATCHING', 'AI_MODEL', 'HYBRID') NOT NULL DEFAULT 'TEMPLATE_MATCHING' AFTER similarity,
ADD COLUMN confidence_score DECIMAL(3,2) AFTER detection_mode,
ADD COLUMN detection_result_json TEXT AFTER confidence_score;
```

## 3. 数据关系图

```
+---------------+       +---------------+       +---------------+
| wukong_user   |       | device        |       | camera        |
+---------------+       +---------------+       +---------------+
| id            |       | id            |       | id            |
| username      |       | name          |       | device_id     |
| password      |       | hardware_code |       | camera_index  |
| ...           |       | ...           |       | ...           |
+---------------+       +---------------+       +---------------+
       |                       |                       |
       |                       |                       |
       v                       v                       |
+---------------+       +---------------+              |
| job_process   |       | ai_model      |              |
+---------------+       +---------------+              |
| id            |       | id            |              |
| name          |       | name          |              |
| device_id     |------>| type          |              |
| ai_model_id   |       | file_path     |              |
| ...           |       | ...           |              |
+---------------+       +---------------+              |
       |                       |                       |
       |                       |                       |
       v                       v                       |
+---------------+       +---------------+              |
| job_instruction|       | dataset       |              |
+---------------+       +---------------+              |
| id            |       | id            |              |
| job_process_id|       | name          |              |
| ...           |       | ...           |              |
+---------------+       +---------------+              |
       |                       |                       |
       |                       |                       |
       v                       v                       |
+---------------+       +---------------+              |
| job_item      |       | training_job  |              |
+---------------+       +---------------+              |
| id            |       | id            |              |
| job_instruction_id|   | model_id      |              |
| ...           |       | dataset_id    |              |
+---------------+       | ...           |              |
       |                +---------------+              |
       |                                               |
       v                                               |
+---------------+       +---------------+              |
| job_item_point|       | product_template|            |
+---------------+       +---------------+              |
| id            |       | id            |              |
| job_item_id   |       | job_process_id|              |
| type          |       | feature_vector|              |
| detection_mode|       | ...           |              |
| feature_vector|       +---------------+              |
| ...           |               |                      |
+---------------+               |                      |
       |                        v                      |
       |                +---------------+              |
       |                | component_template|          |
       |                +---------------+              |
       |                | id            |              |
       |                | product_template_id|         |
       |                | job_item_point_id|           |
       |                | feature_vector|              |
       |                | ...           |              |
       |                +---------------+              |
       |                                               |
       v                                               v
+---------------+       +---------------+       +---------------+
| job_process_log|      | job_item_log  |       | device_log    |
+---------------+       +---------------+       +---------------+
| id            |       | id            |       | id            |
| job_process_id|       | job_process_log_id|   | device_id     |
| ...           |       | ...           |       | ...           |
+---------------+       +---------------+       +---------------+
       |                       |
       |                       |
       v                       v
+---------------+
| job_item_point_log|
+---------------+
| id            |
| job_item_log_id|
| detection_mode|
| confidence_score|
| ...           |
+---------------+
```

## 4. 数据迁移策略

从V1.0迁移到V1.5版本的数据库，需要执行以下步骤：

1. **备份V1.0数据库**
   ```sql
   mysqldump -u [username] -p wukong > wukong_v1_backup.sql
   ```

2. **创建V1.5数据库**
   ```sql
   CREATE DATABASE wukong_v1_5 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **导入V1.0核心表结构**
   ```sql
   mysql -u [username] -p wukong_v1_5 < wukong_v1_core_tables.sql
   ```

4. **创建新表和修改现有表**
   ```sql
   mysql -u [username] -p wukong_v1_5 < wukong_v1_5_schema_updates.sql
   ```

5. **迁移数据**
   ```sql
   -- 迁移用户数据
   INSERT INTO wukong_v1_5.wukong_user SELECT * FROM wukong.wukong_user;
   
   -- 迁移设备数据（需要适配新的表结构）
   INSERT INTO wukong_v1_5.device (id, uuid, name, hardware_code, ip_address, mac_address, status, system_version, app_version, last_heartbeat, created_at, updated_at, deleted)
   SELECT id, uuid, name, hardware_code, ip_address, mac_address, 
          CASE WHEN status = 'ACTIVE' THEN 'ACTIVE' ELSE 'INACTIVE' END,
          version_name, version_number, last_heartbeat, created_at, updated_at, deleted
   FROM wukong.device;
   
   -- 迁移作业流程数据
   INSERT INTO wukong_v1_5.job_process SELECT *, 'TEMPLATE_MATCHING', NULL, NULL FROM wukong.job_process;
   
   -- 其他表的数据迁移...
   ```

6. **验证数据迁移**
   ```sql
   -- 检查记录数是否一致
   SELECT COUNT(*) FROM wukong.wukong_user;
   SELECT COUNT(*) FROM wukong_v1_5.wukong_user;
   
   -- 检查关键数据是否正确迁移
   SELECT * FROM wukong_v1_5.job_process LIMIT 10;
   ```

## 5. 索引优化

为提高查询性能，V1.5版本添加了以下索引：

```sql
-- 模型表索引
CREATE INDEX idx_ai_model_type ON ai_model(type);
CREATE INDEX idx_ai_model_is_active ON ai_model(is_active);

-- 数据集表索引
CREATE INDEX idx_dataset_type ON dataset(type);

-- 产品模板表索引
CREATE INDEX idx_product_template_job_process_id ON product_template(job_process_id);

-- 组件模板表索引
CREATE INDEX idx_component_template_product_id ON component_template(product_template_id);
CREATE INDEX idx_component_template_point_id ON component_template(job_item_point_id);

-- 训练任务表索引
CREATE INDEX idx_training_job_status ON training_job(status);
CREATE INDEX idx_training_job_model_id ON training_job(model_id);
CREATE INDEX idx_training_job_dataset_id ON training_job(dataset_id);

-- 作业流程表索引
CREATE INDEX idx_job_process_detection_mode ON job_process(detection_mode);
CREATE INDEX idx_job_process_ai_model_id ON job_process(ai_model_id);

-- 校验点表索引
CREATE INDEX idx_job_item_point_detection_mode ON job_item_point(detection_mode);
```

## 6. 数据安全考虑

V1.5版本增强了数据安全性：

1. **敏感数据加密**
   - 用户密码使用bcrypt算法加密存储
   - 特征向量等敏感数据使用AES加密

2. **数据备份策略**
   - 自动每日增量备份
   - 每周完整备份
   - 备份文件加密存储

3. **访问控制**
   - 实施基于角色的访问控制
   - 记录数据库操作日志
   - 限制敏感操作的IP地址

## 7. 性能优化建议

1. **查询优化**
   - 使用预编译语句
   - 避免使用SELECT *
   - 分页查询大结果集

2. **索引使用**
   - 监控索引使用情况
   - 定期优化索引
   - 避免过度索引

3. **连接池配置**
   - 根据硬件配置调整连接池大小
   - 设置合理的超时时间
   - 监控连接使用情况

4. **大数据处理**
   - 特征向量等大数据使用分块处理
   - 考虑使用文件存储而非数据库存储大型二进制数据
   - 实施数据归档策略

## 8. 结论

V1.5版本的数据库设计在保留V1.0核心功能的基础上，增加了对机器学习的支持，简化了设备管理，优化了数据结构。这些变更使系统能够支持混合识别方法，提高产品识别的准确性和鲁棒性，同时适应单一设备部署模式。

数据迁移策略确保了从V1.0到V1.5的平滑过渡，索引优化和性能建议则保证了系统在新架构下的高效运行。
