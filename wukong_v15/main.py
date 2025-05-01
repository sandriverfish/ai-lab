import os
import paddlex as pdx
from paddlex import transforms as T

def train():
    # Define training and evaluation transforms
    train_transforms = T.Compose([
        T.RandomDistort(),
        T.RandomExpand(),
        T.RandomCrop(),
        T.RandomHorizontalFlip(),
        T.BatchRandomResize(
            target_sizes=[192, 256, 320, 384, 448, 512, 576, 640],
            interp='RANDOM'),
        T.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    eval_transforms = T.Compose([
        T.Resize(target_size=256),
        T.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Initialize dataset
    train_dataset = pdx.datasets.KeypointDetectionDataset(
        data_dir='data/itx',
        train_list='data/itx/train.json',
        transform=train_transforms,
        shuffle=True)

    eval_dataset = pdx.datasets.KeypointDetectionDataset(
        data_dir='data/itx',
        train_list='data/itx/val.json',
        transform=eval_transforms,
        shuffle=False)

    # Initialize model
    num_joints = 6  # Number of keypoints
    model = pdx.det.PPTinyPose(num_joints=num_joints)

    # Training parameters
    save_dir = 'output/ppTinyPose'
    num_epochs = 100
    batch_size = 8
    learning_rate = 0.001

    # Start training
    model.train(
        num_epochs=num_epochs,
        train_dataset=train_dataset,
        train_batch_size=batch_size,
        eval_dataset=eval_dataset,
        learning_rate=learning_rate,
        save_dir=save_dir,
        use_vdl=True,
        early_stop=True,
        early_stop_patience=10)

if __name__ == '__main__':
    train()