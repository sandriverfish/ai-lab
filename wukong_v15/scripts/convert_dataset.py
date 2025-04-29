import json
import os

def convert_coco_to_txt(json_path, output_txt_path, data_dir):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Create image_id to annotations mapping
    image_annotations = {}
    for ann in data['annotations']:
        image_id = ann['image_id']
        category_id = ann['category_id']
        if image_id not in image_annotations:
            image_annotations[image_id] = set()
        image_annotations[image_id].add(category_id - 1)  # Convert to 0-based indexing

    # Write image paths and labels
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        for img in data['images']:
            if img['id'] in image_annotations:
                image_path = os.path.join(data_dir, 'images', img['file_name'])
                # Use the first category for now since PaddleClas expects single-label
                label = min(image_annotations[img['id']])
                # Ensure no empty lines and proper format
                line = f"{image_path} {label}"
                f.write(line.strip() + '\n')

def main():
    data_dir = "/home/nvidia/ai-lab/wukong_v15/data/itx"
    
    # Convert train.json
    convert_coco_to_txt(
        os.path.join(data_dir, "train.json"),
        os.path.join(data_dir, "train.txt"),
        data_dir
    )
    
    # Convert val.json
    convert_coco_to_txt(
        os.path.join(data_dir, "val.json"),
        os.path.join(data_dir, "val.txt"),
        data_dir
    )

    # Create label list file with proper format (index space label_name)
    labels = [
        "itx_board",
        "memory_slot",
        "msata_slot",
        "hdmi_port",
        "usb_port",
        "ethernet_port",
        "power_connector"
    ]
    
    with open(os.path.join(data_dir, "labels.txt"), "w", encoding='utf-8') as f:
        for idx, label in enumerate(labels):
            # Use space instead of tab for better compatibility
            f.write(f"{idx} {label}\n")

    # Create symlink for label.txt if it doesn't exist
    label_txt = os.path.join(data_dir, "label.txt")
    labels_txt = os.path.join(data_dir, "labels.txt")
    if not os.path.exists(label_txt):
        if os.path.exists(label_txt):
            os.remove(label_txt)
        os.symlink(labels_txt, label_txt)

if __name__ == "__main__":
    main()
    print("Conversion completed successfully!")