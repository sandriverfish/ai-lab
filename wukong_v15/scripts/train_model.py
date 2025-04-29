import paddlex as pdx
from paddlex.cls import transforms as T

# 定义数据增强
train_transforms = T.Compose([
    T.RandomCrop(crop_size=224),
    T.RandomHorizontalFlip(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
eval_transforms = T.Compose([
    T.ResizeByShort(short_size=256),
    T.CenterCrop(crop_size=224),
    T.Normalize()
])

# 加载数据集
train_dataset = pdx.datasets.ImageNet(
    data_dir='data/itx/images',
    file_list='data/itx/train.json',
    label_list='data/itx/labels.txt',
    transforms=train_transforms,
    shuffle=True
)
eval_dataset = pdx.datasets.ImageNet(
    data_dir='data/itx/images',
    file_list='data/itx/val.json',
    label_list='data/itx/labels.txt',
    transforms=eval_transforms
)

# 初始化模型
model = pdx.cls.MobileNetV3_small(num_classes=len(train_dataset.labels))

# 开始训练
model.train(
    num_epochs=20,
    train_dataset=train_dataset,
    train_batch_size=32,
    eval_dataset=eval_dataset,
    learning_rate=0.001,
    lr_decay_epochs=[10, 15],
    save_dir='output',
    use_vdl=True
)