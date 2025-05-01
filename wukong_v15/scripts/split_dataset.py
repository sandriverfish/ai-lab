import json
import random

def split_dataset(input_json, train_json, val_json, split_ratio=0.8):
    with open(input_json, 'r') as f:
        data = json.load(f)
    
    # Get unique image IDs
    image_ids = [img['id'] for img in data['images']]
    random.shuffle(image_ids)
    
    # Split image IDs
    split_point = int(len(image_ids) * split_ratio)
    train_ids = set(image_ids[:split_point])
    val_ids = set(image_ids[split_point:])
    
    # Create train and val datasets
    train_data = {
        'info': data['info'],
        'categories': data['categories'],
        'images': [],
        'annotations': []
    }
    
    val_data = {
        'info': data['info'],
        'categories': data['categories'],
        'images': [],
        'annotations': []
    }
    
    # Split images
    for img in data['images']:
        if img['id'] in train_ids:
            train_data['images'].append(img)
        else:
            val_data['images'].append(img)
    
    # Split annotations
    for ann in data['annotations']:
        if ann['image_id'] in train_ids:
            train_data['annotations'].append(ann)
        else:
            val_data['annotations'].append(ann)
    
    # Save split datasets
    with open(train_json, 'w') as f:
        json.dump(train_data, f, indent=2)
    
    with open(val_json, 'w') as f:
        json.dump(val_data, f, indent=2)

if __name__ == '__main__':
    input_json = '../data/itx/train.json'
    train_json = '../data/itx/train_split.json'
    val_json = '../data/itx/val.json'
    split_dataset(input_json, train_json, val_json)