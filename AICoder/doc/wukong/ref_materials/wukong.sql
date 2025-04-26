-- 创建数据库（如果还没有创建）
CREATE DATABASE IF NOT EXISTS wukong CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'wukong'@'localhost' IDENTIFIED BY 'wukong@01';
GRANT ALL ON wukong.* TO 'wukong'@'localhost';
CREATE USER IF NOT EXISTS 'wukong'@'%' IDENTIFIED BY 'wukong@01';
GRANT ALL PRIVILEGES ON wukong.* TO 'wukong'@'%' WITH GRANT OPTION;

CREATE USER IF NOT EXISTS 'metabase'@'%' IDENTIFIED BY 'metabase';
GRANT SELECT ON wukong.* TO 'metabase'@'%';

FLUSH PRIVILEGES;

-- 使用wukong数据库
USE wukong;

-- 创建用户表
CREATE TABLE IF NOT EXISTS wukong_user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    status ENUM('ACTIVE', 'INACTIVE', 'LOCKED') NOT NULL DEFAULT 'ACTIVE',
    phone VARCHAR(20),
    description VARCHAR(255),
    last_login_time DATETIME,
    failed_login_attempts INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建终端设备表
CREATE TABLE IF NOT EXISTS device (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    uuid VARCHAR(50) NOT NULL,               -- 唯一标识
    terminal_code VARCHAR(50) UNIQUE NOT NULL,       -- 终端编号
    hardware_code VARCHAR(50),                       -- 硬件编码
    name VARCHAR(100) NOT NULL,                      -- 设备名
    location VARCHAR(100),                           -- 位置
    ip_address VARCHAR(45),                          -- IP地址
    mac_address VARCHAR(17),                         -- MAC地址
    status ENUM('UNBOUND', 'BOUND', 'ACTIVE') NOT NULL DEFAULT 'UNBOUND',  -- 状态
    work_status ENUM('IDLE', 'WORKING') NOT NULL DEFAULT 'IDLE',      -- 工作状态
    description VARCHAR(255),                        -- 描述
    online_status TINYINT(1) DEFAULT 0,              -- 在线状态 (0: 离线, 1: 在线)
    activation_time DATETIME,                        -- 激活时间
    last_heartbeat DATETIME,                         -- 最后心跳时间
    version_name VARCHAR(50),                        -- 版本名
    version_number VARCHAR(50),                      -- 版本号
    manufacturer VARCHAR(100),                       -- 制造商
    model VARCHAR(100),                              -- 型号
    upgrade_strategy ENUM('NO_UPGRADE', 'AUTO_UPGRADE', 'SPECIFIC_VERSION') NOT NULL DEFAULT 'NO_UPGRADE', -- 升级策略
    app_version_id INT,                              -- 应用版本ID
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建终端截图表
CREATE TABLE IF NOT EXISTS device_screenshot (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,               -- 主键
    device_id BIGINT NOT NULL,                          -- 所属终端
    device_uuid VARCHAR(50) NOT NULL,                   -- 所属终端唯一标识
    name VARCHAR(100) NOT NULL,                         -- 图片名称
    snapshot VARCHAR(100),                              -- 文件名
    thumbnail VARCHAR(100),                             -- 缩略图路径文件名
    snapshot_size BIGINT DEFAULT 0,                     -- 图片大小（单位：字节）
    snapshot_checksum VARCHAR(64),                      -- 图片校验值（如MD5）
    width INT DEFAULT 0,                                -- 图片宽度
    height INT DEFAULT 0,                               -- 图片高度
    source ENUM('LOCAL', 'TERMINAL') DEFAULT 'TERMINAL', -- 来源（本地，终端）
    description VARCHAR(255),                           -- 描述
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建作业流程表
CREATE TABLE IF NOT EXISTS job_process (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    version INT DEFAULT 0,                              -- 版本
    name VARCHAR(100) NOT NULL,                          -- 作业流程名称
    device_id BIGINT NOT NULL,                          -- 所属终端（外键）
    device_uuid VARCHAR(50) NOT NULL,                   -- 所属终端唯一标识
    auto_loop TINYINT(1) DEFAULT 1,                     -- 是否自动循环（0: 否, 1: 是）
    ng_terminate TINYINT(1) DEFAULT 1,                   -- NG是否终止（0: 否, 1: 是）
    is_default TINYINT(1) DEFAULT 0,                      -- 是否默认作业流程（0: 否, 1: 是）
    is_published TINYINT(1) DEFAULT 0,                  -- 是否已发布（0: 否, 1: 是）
    last_published_json TEXT,                           -- 最后一次发布的JSON
    creator_id BIGINT NOT NULL,                          -- 创建者ID（外键，指向用户表）
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,       -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    published_at DATETIME,                              -- 发布时间
    deleted TINYINT(1) DEFAULT 0,                       -- 删除标记（0: 未删除, 1: 已删除）
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE,  -- 外键约束
    FOREIGN KEY (creator_id) REFERENCES wukong_user(id) ON DELETE CASCADE    -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建作业指示表
CREATE TABLE IF NOT EXISTS job_instruction (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100),                                  -- 作业指示名称
    job_process_id BIGINT NOT NULL,                     -- 所属作业流程
    job_process_uuid VARCHAR(50),                       -- 所属作业流程唯一标识
    instruction_text TEXT,                               -- 作业指示文本
    instruction_image VARCHAR(255),                      -- 作业指示图像（存储图像路径）
    instruction_image_size BIGINT DEFAULT 0,             -- 图片大小（单位：字节）
    instruction_image_checksum VARCHAR(64),              -- 图片校验值（如MD5）
    instruction_thumbnail VARCHAR(255),                 -- 作业指示缩略图（存储缩略图路径）
    step_order INT NOT NULL,                             -- 步骤顺序
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,       -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,                       -- 删除标记（0: 未删除, 1: 已删除）
    FOREIGN KEY (job_process_id) REFERENCES job_process(id) ON DELETE CASCADE  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建作业项目表
CREATE TABLE IF NOT EXISTS job_item (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                 -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100),                                  -- 作业项目名称
    job_process_id BIGINT NOT NULL,                     -- 所属作业流程
    job_process_uuid VARCHAR(50),                       -- 所属作业流程唯一标识
    job_instruction_id BIGINT NOT NULL,                 -- 所属作业指示
    job_instruction_uuid VARCHAR(50),                   -- 所属作业指示唯一标识
    item_image VARCHAR(255),                             -- 作业项目图像（存储图像路径）
    item_image_size BIGINT DEFAULT 0,                    -- 图像大小（单位：字节）
    item_image_checksum VARCHAR(64),                     -- 图像校验值（如MD5）
    item_thumbnail VARCHAR(255),                         -- 作业项目缩略图（存储缩略图路径）
    mode ENUM('MATCHING', 'OTHER') NOT NULL,            -- 模式（匹配模式，其他模式）
    standard_time INT NOT NULL,                          -- 标准时间（单位：秒）
    upper_limit_time INT NOT NULL,                       -- 上限时间（单位：秒）
    step_order INT NOT NULL,                             -- 步骤顺序
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,       -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,                       -- 删除标记（0: 未删除, 1: 已删除）
    FOREIGN KEY (job_instruction_id) REFERENCES job_instruction(id) ON DELETE CASCADE,  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建校验点表
CREATE TABLE IF NOT EXISTS job_item_point (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    name VARCHAR(100),                                  -- 校验点名称
    job_process_id BIGINT NOT NULL,                     -- 所属作业流程
    job_process_uuid VARCHAR(50),                       -- 所属作业流程唯一标识
    job_item_id BIGINT NOT NULL,                        -- 所属作业项目
    job_item_uuid VARCHAR(50),                         -- 所属作业项目唯一标识
    type ENUM('BASE_POINT', 'CHECK_POINT', 'BASE_SEARCH_AREA', 'BARCODE_AREA') NOT NULL,   -- 类型（基准点，校验点，基准点搜索区域）
    shape ENUM('RECTANGLE', 'POLYGON') NOT NULL,        -- 形状
    `left` INT NOT NULL,                                  -- 左上角x坐标
    top INT NOT NULL,                                   -- 左上角y坐标
    width INT NOT NULL,                                 -- 最外层矩形框的宽度
    height INT NOT NULL,                                -- 最外层矩形框的高度
    snapshot VARCHAR(255),                              -- 校验点截图
    snapshot_size BIGINT DEFAULT 0,                    -- 截图大小（单位：字节）
    snapshot_checksum VARCHAR(64),                     -- 截图校验值（如MD5）
    similarity DECIMAL(3,2) NOT NULL,                   -- 相似度（范围0.50-1.00）
    step_order INT NOT NULL,                             -- 步骤顺序
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted TINYINT(1) DEFAULT 0,                       -- 删除标记（0: 未删除, 1: 已删除）
    FOREIGN KEY (job_item_id) REFERENCES job_item(id) ON DELETE CASCADE  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建作业项目日志表
CREATE TABLE IF NOT EXISTS job_process_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    barcode VARCHAR(255),                                -- 条码
    device_id BIGINT NOT NULL,                          -- 所属终端
    device_uuid VARCHAR(50),                           -- 所属终端唯一标识
    job_process_id BIGINT NOT NULL,                     -- 所属作业流程
    job_process_uuid VARCHAR(50),                       -- 所属作业流程唯一标识
    job_process_version INT NOT NULL,                  -- 作业流程版本
    status ENUM('PROCESSING', 'COMPLETED', 'FAILED', 'CANCELLED') NOT NULL DEFAULT 'PROCESSING', -- 作业流程状态（进行中，完成，失败，取消）
    start_time DATETIME NOT NULL,                       -- 开始时间
    end_time DATETIME,                                  -- 结束时间
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE,  -- 外键约束
    FOREIGN KEY (job_process_id) REFERENCES job_process(id) ON DELETE CASCADE  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS job_item_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    barcode VARCHAR(255),                                -- 条码
    job_process_log_id BIGINT NOT NULL,                 -- 所属作业流程日志
    job_process_log_uuid VARCHAR(50),                   -- 所属作业流程日志唯一标识
    job_process_id BIGINT NOT NULL,                     -- 所属作业流程
    job_process_uuid VARCHAR(50),                       -- 所属作业流程唯一标识
    job_process_version INT NOT NULL,                  -- 作业流程版本
    job_instruction_id BIGINT NOT NULL,                -- 所属作业指示
    job_instruction_uuid VARCHAR(50),                   -- 所属作业指示唯一标识
    job_item_id BIGINT NOT NULL,                        -- 所属作业项目
    job_item_uuid VARCHAR(50),                          -- 所属作业项目唯一标识
    status ENUM('PROCESSING', 'COMPLETED', 'FAILED', 'CANCELLED') NOT NULL DEFAULT 'PROCESSING', -- 作业项目状态（进行中，完成，失败，取消）
    start_time DATETIME NOT NULL,                       -- 开始时间
    end_time DATETIME,                                  -- 结束时间
    job_item_timeout TINYINT(1) DEFAULT 0,              -- 是否超时（0: 否, 1: 是）
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (job_process_log_id) REFERENCES job_process_log(id) ON DELETE CASCADE,  -- 外键约束
    FOREIGN KEY (job_instruction_id) REFERENCES job_instruction(id) ON DELETE CASCADE  -- 外键约束
    FOREIGN KEY (job_item_id) REFERENCES job_item(id) ON DELETE CASCADE,  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS job_item_point_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    uuid VARCHAR(50) NOT NULL,                          -- 唯一标识
    barcode VARCHAR(255),                                -- 条码
    job_process_log_id BIGINT NOT NULL,                 -- 所属作业流程日志
    job_process_log_uuid VARCHAR(50),                   -- 所属作业流程日志唯一标识
    job_item_log_id BIGINT NOT NULL,                    -- 所属作业项目日志
    job_item_log_uuid VARCHAR(50),                     -- 所属作业项目日志唯一标识
    job_process_id BIGINT NOT NULL,                     -- 所属作业流程
    job_process_uuid VARCHAR(50),                       -- 所属作业流程唯一标识
    job_process_version INT NOT NULL,                  -- 作业流程版本
    job_item_point_id BIGINT NOT NULL,                  -- 所属作业项目校验点
    job_item_point_uuid VARCHAR(50),                    -- 所属作业项目校验点唯一标识
    job_item_point_snapshot VARCHAR(255),                -- 作业项目校验点截图
    status ENUM('PROCESSING', 'COMPLETED', 'FAILED', 'CANCELLED') NOT NULL DEFAULT 'PROCESSING', -- 作业项目状态（进行中，完成，失败，取消）
    start_time DATETIME NOT NULL,                       -- 开始时间
    end_time DATETIME,                                  -- 结束时间
    error_code VARCHAR(50),                              -- 错误码
    description TEXT,                                     -- 描述
    similarity DECIMAL(3,2) NOT NULL,                   -- 相似度
    snapshot VARCHAR(255),                              -- 校验点截图
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (job_process_log_id) REFERENCES job_process_log(id) ON DELETE CASCADE,  -- 外键约束
    FOREIGN KEY (job_item_log_id) REFERENCES job_item_log(id) ON DELETE CASCADE,  -- 外键约束
    FOREIGN KEY (job_item_point_id) REFERENCES job_item_point(id) ON DELETE CASCADE  -- 外键约束
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 创建指令表
CREATE TABLE IF NOT EXISTS notification (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 指令的唯一标识
    type VARCHAR(50) NOT NULL,                           -- 指令类型
    parameters TEXT,                                     -- 指令参数（可以是 JSON 字符串）
    device_id BIGINT NOT NULL,                           -- 关联的终端 ID
    status ENUM('UNSENT', 'SENT') NOT NULL DEFAULT 'UNSENT', -- 指令状态（未分发，已分发）
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,     -- 创建时间
    dispatched_at DATETIME,                            -- 分发时间
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE  -- 外键约束，关联终端设备表
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 配置表
CREATE TABLE IF NOT EXISTS config (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,                -- 主键
    config_key VARCHAR(50) UNIQUE NOT NULL,              -- 配置键
    config_value TEXT,                                    -- 配置值
    type ENUM('SYSTEM', 'APP') NOT NULL DEFAULT 'SYSTEM',  -- 类型（系统，应用）
    seq INT NOT NULL DEFAULT 0,                          -- 排序
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,      -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS device_log (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    device_id BIGINT NOT NULL,
    terminal_code VARCHAR(50) NOT NULL,                   -- 终端编号
    hardware_code VARCHAR(50) NOT NULL,                   -- 硬件编码
    file VARCHAR(255) NOT NULL,                           -- 日志文件路径
    file_name VARCHAR(100) NOT NULL,                      -- 日志文件名
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS device_schedule (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    device_id BIGINT NOT NULL,
    task_type VARCHAR(50) NOT NULL,                         -- 任务类型
    task_time TIME NOT NULL,                                -- 任务时间
    days_of_week VARCHAR(255),                              -- 任务执行的星期几
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS app_version (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- 主键ID
    version_name VARCHAR(20) NOT NULL,          -- APK版本号
    version_number INT NOT NULL,                -- APK版本号
    file VARCHAR(255) NOT NULL,                 -- APP文件路径
    file_name VARCHAR(100) NOT NULL,           -- APP文件名
    file_size BIGINT DEFAULT 0,                -- APP文件大小（单位：字节）
    checksum VARCHAR(64),                      -- APP文件校验值（如MD5）
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    UNIQUE KEY unique_version (version_name, version_number) -- 联合唯一索引
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS cloud_sync_event (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    event_type ENUM('SUBSYSTEM', 'DEVICE', 'JOB_PROCESS', 'JOB_PROCESS_LOG') NOT NULL,
    operation_type ENUM('SYNC', 'DELETE') NOT NULL,
    param1 VARCHAR(50),
    param2 VARCHAR(50),
    status ENUM('UNSYNCED', 'SYNCED', 'FAILED') NOT NULL DEFAULT 'UNSYNCED', -- 事件状态（未同步，已同步，失败）
    description VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,     -- 创建时间
    synced_at DATETIME                            -- 同步时间
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS device_crash (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    terminal_code VARCHAR(50) UNIQUE NOT NULL,       -- 终端编号
    hardware_code VARCHAR(50),                       -- 硬件编码
    ip_address VARCHAR(45),                          -- IP地址
    mac_address VARCHAR(17),                         -- MAC地址
    version_name VARCHAR(50),                        -- 版本名
    version_number VARCHAR(50),                      -- 版本号
    stack TEXT,
    other TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS sys_version (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- 主键ID
    version_name VARCHAR(20) NOT NULL,          -- 系统版本号
    version_number INT NOT NULL,                -- 系统版本号
    file VARCHAR(255) NOT NULL,                 -- 系统文件路径
    file_name VARCHAR(100) NOT NULL,           -- 系统文件名
    file_size BIGINT DEFAULT 0,                -- 系统文件大小（单位：字节）
    checksum VARCHAR(64),                      -- 系统文件校验值（如MD5）
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- 创建时间
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 更新时间
    UNIQUE KEY unique_version (version_name, version_number) -- 联合唯一索引
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


