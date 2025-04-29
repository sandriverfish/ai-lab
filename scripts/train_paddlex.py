import paddlex as pdx

# 数据集路径
train_dataset = pdx.datasets.ImageNet(
    data_dir='dataset/train',
    file_list='dataset/train_list.txt',
    label_list='dataset/labels.txt',
    transforms=pdx.transforms.Compose([
        pdx.transforms.RandomCrop(),
        pdx.transforms.RandomHorizontalFlip(),
        pdx.transforms.Normalize()
    ]),
    num_workers=4,
    shuffle=True
)

val_dataset = pdx.datasets.ImageNet(
    data_dir='dataset/val',
    file_list='dataset/val_list.txt',
    label_list='dataset/labels.txt',
    transforms=pdx.transforms.Compose([
        pdx.transforms.ResizeByShort(),
        pdx.transforms.Normalize()
    ]),
    num_workers=4
)

# 模型初始化
model = pdx.cls.MobileNetV3_small(num_classes=len(train_dataset.labels))

# 开始训练
model.train(
    num_epochs=50,
    train_dataset=train_dataset,
    train_batch_size=32,
    eval_dataset=val_dataset,
    learning_rate=0.001,
    save_dir='output/mobilenetv3_small',
    use_vdl=True
)
