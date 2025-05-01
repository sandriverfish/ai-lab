import os
import json
import shutil
import cv2
import numpy as np
from pathlib import Path
import paddle
from ppdet.core.workspace import create
from ppdet.core.workspace import load_config
from ppdet.engine import Trainer

def create_coco_annotation(image_dir, keypoint_names):
    """
    创建COCO格式的数据集注释
    """
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": [{
            "id": 1,
            "name": "itx_board",
            "keypoints": keypoint_names,
            "skeleton": []
        }]
    }
    
    image_id = 1
    anno_id = 1
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    for img_file in image_files:
        img_path = os.path.join(image_dir, img_file)
        img = cv2.imread(img_path)
        height, width = img.shape[:2]
        
        # 添加图像信息
        coco_format["images"].append({
            "id": image_id,
            "file_name": img_file,
            "height": height,
            "width": width
        })
        
        # 这里需要手动标注或其他方式获取以下信息
        # bbox = [x, y, width, height]  # 需要标注
        # keypoints = []  # 需要标注 [x1,y1,v1,x2,y2,v2,...]
        
        image_id += 1
    
    return coco_format

def prepare_dataset(data_dir):
    """
    准备训练数据集
    """
    # 创建必要的目录
    images_dir = os.path.join(data_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    # 定义关键点名称
    keypoint_names = [
        "memory_slot",
        "usb_port",
        "hdmi_port",
        "msata_slot",
        "power_connector",
        "ethernet_port"
    ]
    
    # 创建COCO格式的注释
    coco_anno = create_coco_annotation(images_dir, keypoint_names)
    
    # 保存注释文件
    with open(os.path.join(data_dir, 'train.json'), 'w') as f:
        json.dump(coco_anno, f, indent=2)

def train_model(config_file):
    """
    训练模型
    """
    # 设置GPU设备
    paddle.device.set_device('gpu:0')
    
    # 加载配置
    cfg = load_config(config_file)
    
    # 创建训练器
    trainer = Trainer(cfg)
    
    # 开始训练
    trainer.train()

if __name__ == "__main__":
    # 设置路径
    data_dir = "/home/nvidia/ai-lab/wukong_v15/data/itx"
    config_file = "/home/nvidia/ai-lab/wukong_v15/config/ppyoloe_rtpose.yaml"
    
    # 准备数据集
    prepare_dataset(data_dir)
    
    # 训练模型
    train_model(config_file)