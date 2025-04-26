# Data Preparation Guide for Wukong ML Integration

This guide outlines the process for collecting, preparing, and managing data for the Wukong ML integration project. Proper data preparation is crucial for training effective machine learning models that can enhance the product recognition capabilities of the Wukong system.

## 1. Data Requirements

### 1.1 Data Types

For the Wukong ML integration, we need the following types of data:

1. **Product Images**
   - Full product images showing the entire assembly
   - Multiple angles and positions
   - Various lighting conditions
   - Different stages of assembly

2. **Component Images**
   - Individual components in isolation
   - Components in the context of partial assembly
   - Correctly installed components
   - Incorrectly installed components (for defect detection)

3. **Background Images**
   - Workstation backgrounds without products
   - Various lighting conditions
   - Different camera angles

### 1.2 Minimum Dataset Size

For effective training, we recommend the following minimum dataset sizes:

| Data Type | Minimum Images | Recommended Images |
|-----------|----------------|-------------------|
| Product (per type) | 50 | 100-200 |
| Component (per type) | 20 | 50-100 |
| Background | 10 | 30-50 |

### 1.3 Image Requirements

- **Resolution**: Match the camera resolution used in production (e.g., 3840×2160)
- **Format**: JPEG or PNG (lossless preferred for training data)
- **Color Space**: RGB
- **Aspect Ratio**: Maintain consistent aspect ratio
- **File Size**: Preferably under 5MB per image

## 2. Data Collection Strategy

### 2.1 Leveraging Existing Data

1. **Extract from V1.0 System**
   - Retrieve existing product images from the database
   - Extract component templates used for matching
   - Collect historical inspection images

2. **Organize by Product Type**
   - Create separate folders for each product type
   - Maintain version information if product designs change

### 2.2 New Data Collection

1. **Camera Setup**
   - Use the same camera model as in production
   - Maintain consistent camera height (500-800mm)
   - Ensure proper focus and exposure settings

2. **Lighting Conditions**
   - Collect images under standard factory lighting
   - Include variations in lighting intensity
   - Capture images with shadows and reflections
   - Document lighting conditions for each session

3. **Product Positioning**
   - Capture products in standard position
   - Include variations in position and orientation
   - Rotate products at 15-30 degree intervals
   - Shift position within the camera frame

4. **Assembly Stages**
   - Capture images at each stage of assembly
   - Document the assembly sequence
   - Include both correct and incorrect assemblies

### 2.3 Systematic Collection Process

1. **Create a Collection Plan**
   - Define the number of images needed per product/component
   - Specify the variations to capture
   - Create a checklist for each session

2. **Recording Session Information**
   - Document date, time, and location
   - Record camera settings and lighting conditions
   - Note any special conditions or variations

3. **Quality Control During Collection**
   - Review images immediately after capture
   - Check for focus, exposure, and framing issues
   - Retake problematic images

## 3. Data Annotation

### 3.1 Annotation Types

1. **Bounding Boxes**
   - Draw rectangles around products and components
   - Include the entire object with minimal margin
   - Ensure consistency in boundary definitions

2. **Segmentation Masks**
   - Create pixel-level masks for precise component boundaries
   - Useful for components with irregular shapes
   - Required for instance segmentation models

3. **Keypoints**
   - Mark specific points of interest on components
   - Useful for alignment and orientation detection
   - Typically used for complex assemblies

4. **Classification Labels**
   - Assign class labels to products and components
   - Include state information (installed/not installed)
   - Add quality indicators (correct/incorrect installation)

### 3.2 Annotation Tools

1. **Recommended Tools**
   - [LabelImg](https://github.com/tzutalin/labelImg) for bounding boxes
   - [CVAT](https://github.com/opencv/cvat) for comprehensive annotation
   - [VGG Image Annotator](https://www.robots.ox.ac.uk/~vgg/software/via/) for polygon and point annotations
   - [PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg) for segmentation annotation

2. **Setting Up an Annotation Environment**
   - Install the chosen annotation tool
   - Create predefined label categories
   - Establish annotation guidelines

### 3.3 Annotation Guidelines

1. **Bounding Box Guidelines**
   - Include the entire object with minimal margin
   - Be consistent with boundary definitions
   - For occluded objects, annotate only the visible part

2. **Labeling Conventions**
   - Use consistent naming conventions
   - Include hierarchical information (e.g., product_type/component_name)
   - Add state information in labels (e.g., screw_installed, screw_missing)

3. **Quality Control**
   - Review annotations for accuracy and consistency
   - Have multiple annotators check each other's work
   - Use automated validation tools when available

## 4. Data Augmentation

### 4.1 Augmentation Techniques

1. **Geometric Transformations**
   - Rotation (±30 degrees)
   - Scaling (0.8-1.2x)
   - Translation (±10% of image size)
   - Horizontal/vertical flipping (if appropriate for the product)

2. **Photometric Transformations**
   - Brightness adjustment (±20%)
   - Contrast adjustment (±20%)
   - Hue and saturation shifts
   - Gaussian noise addition

3. **Advanced Augmentations**
   - Random erasing (simulates occlusion)
   - Cutout/CutMix (for robustness)
   - Mosaic (combines multiple images)
   - MixUp (blends images and labels)

### 4.2 Augmentation Implementation

1. **Using PaddleX Data Augmentation**
   ```python
   import paddlex as pdx
   
   # Define transforms for training
   train_transforms = pdx.transforms.Compose([
       pdx.transforms.RandomDistort(brightness_range=0.2, contrast_range=0.2),
       pdx.transforms.RandomExpand(),
       pdx.transforms.RandomCrop(),
       pdx.transforms.RandomHorizontalFlip(),
       pdx.transforms.Resize(target_size=640),
       pdx.transforms.Normalize()
   ])
   ```

2. **Custom Augmentation Pipeline**
   ```python
   import cv2
   import numpy as np
   import random
   
   def augment_image(image, bbox=None):
       # Random rotation
       angle = random.uniform(-30, 30)
       h, w = image.shape[:2]
       center = (w // 2, h // 2)
       M = cv2.getRotationMatrix2D(center, angle, 1.0)
       image = cv2.warpAffine(image, M, (w, h), borderMode=cv2.BORDER_REFLECT)
       
       # Random brightness and contrast
       alpha = random.uniform(0.8, 1.2)  # Contrast
       beta = random.uniform(-20, 20)    # Brightness
       image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
       
       # Transform bounding box if provided
       if bbox is not None:
           # Transform bbox coordinates using the same rotation matrix
           # Implementation depends on bbox format
           pass
           
       return image, bbox
   ```

### 4.3 Augmentation Strategy

1. **Online vs. Offline Augmentation**
   - Online: Generate augmentations during training
   - Offline: Pre-generate augmented images and save to disk

2. **Augmentation Intensity**
   - Start with mild augmentations
   - Gradually increase intensity if model overfits
   - Monitor validation performance to adjust strategy

3. **Product-Specific Considerations**
   - Some products may not be valid when flipped
   - Certain components may have orientation constraints
   - Adjust augmentation parameters based on product characteristics

## 5. Dataset Organization

### 5.1 Directory Structure

```
wukong-dataset/
├── products/
│   ├── product_type_1/
│   │   ├── images/
│   │   └── annotations/
│   ├── product_type_2/
│   │   ├── images/
│   │   └── annotations/
│   └── ...
├── components/
│   ├── component_type_1/
│   │   ├── images/
│   │   └── annotations/
│   ├── component_type_2/
│   │   ├── images/
│   │   └── annotations/
│   └── ...
├── backgrounds/
│   ├── images/
│   └── annotations/
└── metadata/
    ├── product_metadata.json
    ├── component_metadata.json
    └── dataset_info.json
```

### 5.2 File Naming Conventions

Use consistent file naming that includes:
- Product/component identifier
- Capture conditions
- Sequence number
- Annotation status

Example: `product_A_standard_lighting_front_001.jpg`

### 5.3 Metadata Structure

Create JSON files to store metadata:

```json
{
  "dataset_name": "Wukong-ProductA-V1",
  "creation_date": "2024-05-15",
  "version": "1.0",
  "num_images": 150,
  "num_annotations": 450,
  "classes": [
    {"id": 1, "name": "screw_type_a", "count": 200},
    {"id": 2, "name": "connector_type_b", "count": 150},
    {"id": 3, "name": "housing", "count": 100}
  ],
  "capture_conditions": {
    "camera": "MindVision MV-SUA800GC-T",
    "resolution": "3840x2160",
    "lighting": "standard factory lighting"
  }
}
```

## 6. Dataset Splitting

### 6.1 Train/Validation/Test Split

Divide the dataset into:
- Training set: 70-80% of the data
- Validation set: 10-15% of the data
- Test set: 10-15% of the data

### 6.2 Stratified Splitting

Ensure each split contains a representative distribution of:
- Product types
- Component types
- Lighting conditions
- Camera angles
- Correct/incorrect assemblies

### 6.3 Cross-Validation Strategy

For smaller datasets, consider using k-fold cross-validation:
1. Divide the dataset into k equal parts (typically k=5)
2. Train k different models, each using k-1 parts for training and 1 part for validation
3. Average the performance metrics across all k models

## 7. Data Versioning and Management

### 7.1 Version Control

1. **Dataset Versioning**
   - Assign version numbers to datasets (e.g., v1.0, v1.1)
   - Document changes between versions
   - Maintain a changelog

2. **Git LFS for Image Storage**
   - Use Git Large File Storage for version control of images
   - Store annotations in standard Git repositories
   - Link annotations to specific image versions

### 7.2 Data Management Tools

1. **DVC (Data Version Control)**
   - Track large files outside of Git
   - Synchronize data with models
   - Reproduce experiments with specific data versions

2. **Label Studio**
   - Collaborative annotation
   - Quality control workflows
   - Export to multiple formats

### 7.3 Backup Strategy

1. **Regular Backups**
   - Daily incremental backups
   - Weekly full backups
   - Store backups in multiple locations

2. **Backup Verification**
   - Regularly test backup restoration
   - Verify data integrity
   - Document backup procedures

## 8. Data Quality Assessment

### 8.1 Quality Metrics

1. **Annotation Quality**
   - Intersection over Union (IoU) between annotators
   - Consistency of label assignments
   - Completeness of annotations

2. **Image Quality**
   - Resolution and clarity
   - Proper exposure
   - Color accuracy
   - Focus quality

### 8.2 Quality Improvement Process

1. **Identify Problem Areas**
   - Review model performance on specific subsets
   - Analyze confusion matrices
   - Examine false positives and negatives

2. **Targeted Data Collection**
   - Collect additional data for underperforming categories
   - Focus on challenging lighting or positioning scenarios
   - Add examples of common failure cases

3. **Annotation Refinement**
   - Re-annotate problematic images
   - Standardize annotation boundaries
   - Resolve label inconsistencies

## 9. Synthetic Data Generation

### 9.1 Synthetic Data Techniques

1. **3D Model Rendering**
   - Create 3D models of products and components
   - Render with various lighting and backgrounds
   - Generate perfect annotations automatically

2. **Composition-based Generation**
   - Cut out components and place on background images
   - Vary position, orientation, and lighting
   - Generate realistic compositions

3. **GAN-based Generation**
   - Train Generative Adversarial Networks on existing data
   - Generate novel images with similar characteristics
   - Use conditional GANs for specific product types

### 9.2 Implementation Tools

1. **Blender for 3D Rendering**
   - Open-source 3D creation suite
   - Python API for automation
   - Realistic physics and lighting simulation

2. **OpenCV for Composition**
   ```python
   import cv2
   import numpy as np
   
   # Load component and background
   component = cv2.imread('component.png', cv2.IMREAD_UNCHANGED)
   background = cv2.imread('background.jpg')
   
   # Random position
   x = np.random.randint(0, background.shape[1] - component.shape[1])
   y = np.random.randint(0, background.shape[0] - component.shape[0])
   
   # Create mask from alpha channel if available
   if component.shape[2] == 4:
       alpha = component[:, :, 3] / 255.0
       alpha = np.expand_dims(alpha, axis=2)
       rgb = component[:, :, :3]
       
       # Blend component onto background
       h, w = component.shape[:2]
       roi = background[y:y+h, x:x+w]
       blended = (1.0 - alpha) * roi + alpha * rgb
       background[y:y+h, x:x+w] = blended
   
   # Save the result
   cv2.imwrite('synthetic_image.jpg', background)
   ```

3. **PaddleGAN for GAN-based Generation**
   - Part of the PaddlePaddle ecosystem
   - Supports multiple GAN architectures
   - Includes tools for image-to-image translation

### 9.3 Balancing Real and Synthetic Data

1. **Mixing Strategy**
   - Start with a base of real data
   - Gradually add synthetic data
   - Monitor validation performance to determine optimal mix

2. **Domain Adaptation**
   - Use techniques to reduce the gap between synthetic and real data
   - Apply style transfer to make synthetic images more realistic
   - Fine-tune models on small real datasets after pre-training on synthetic data

## 10. Continuous Data Collection

### 10.1 Active Learning

1. **Uncertainty Sampling**
   - Identify images where the model is least confident
   - Prioritize these for annotation
   - Focus resources on the most informative examples

2. **Implementation Strategy**
   ```python
   import paddle
   import numpy as np
   
   def get_uncertainty_scores(model, unlabeled_data_loader):
       uncertainties = []
       image_ids = []
       
       model.eval()
       with paddle.no_grad():
           for batch_id, data in enumerate(unlabeled_data_loader):
               images = data[0]
               ids = data[1]
               
               # Get model predictions
               outputs = model(images)
               
               # For classification, use entropy of softmax probabilities
               probs = paddle.nn.functional.softmax(outputs, axis=1)
               entropy = -paddle.sum(probs * paddle.log(probs + 1e-10), axis=1)
               
               uncertainties.extend(entropy.numpy())
               image_ids.extend(ids.numpy())
       
       # Sort by uncertainty (highest first)
       sorted_indices = np.argsort(uncertainties)[::-1]
       sorted_ids = [image_ids[i] for i in sorted_indices]
       
       return sorted_ids
   ```

3. **Feedback Loop**
   - Implement a system for model feedback
   - Regularly retrain with newly annotated data
   - Track performance improvements over time

### 10.2 Production Data Utilization

1. **Data Collection from Production**
   - Capture images during normal operation
   - Log detection results and confidence scores
   - Flag potential false positives/negatives

2. **Human-in-the-Loop Verification**
   - Review and correct model predictions
   - Focus on edge cases and failures
   - Build a curated dataset of challenging examples

3. **Privacy and Security Considerations**
   - Ensure data collection complies with company policies
   - Remove any sensitive information
   - Secure data storage and transmission

## 11. Data Pipeline Implementation

### 11.1 PaddleX Dataset Creation

```python
import paddlex as pdx

# Create detection dataset
train_dataset = pdx.datasets.VOCDetection(
    data_dir='wukong-dataset',
    file_list='wukong-dataset/train_list.txt',
    label_list='wukong-dataset/labels.txt',
    transforms=train_transforms
)

# Create evaluation dataset
eval_dataset = pdx.datasets.VOCDetection(
    data_dir='wukong-dataset',
    file_list='wukong-dataset/eval_list.txt',
    label_list='wukong-dataset/labels.txt',
    transforms=eval_transforms
)
```

### 11.2 Data Loading and Batching

```python
# Create data loaders
train_loader = paddle.io.DataLoader(
    train_dataset,
    batch_size=8,
    shuffle=True,
    num_workers=4,
    drop_last=True
)

eval_loader = paddle.io.DataLoader(
    eval_dataset,
    batch_size=1,
    shuffle=False,
    num_workers=2
)
```

### 11.3 Data Pipeline Monitoring

1. **Performance Metrics**
   - Track data loading time
   - Monitor memory usage
   - Measure preprocessing overhead

2. **Data Quality Checks**
   - Verify image dimensions and channels
   - Check for corrupted images
   - Validate annotation formats

3. **Automated Alerts**
   - Set up alerts for data pipeline failures
   - Monitor disk space for dataset storage
   - Track dataset growth over time

## 12. Conclusion

Proper data preparation is the foundation of successful machine learning integration. By following this guide, you can create high-quality datasets that enable the Wukong system to achieve robust product recognition across varying conditions. Remember that data collection and preparation is an iterative process—continuously evaluate model performance and refine your dataset to address specific challenges and edge cases.

## 13. Appendices

### 13.1 Sample Data Collection Checklist

```
Product Type: _______________
Date: _______________
Operator: _______________

Camera Settings:
- Model: _______________
- Resolution: _______________
- Aperture: _______________
- Shutter Speed: _______________
- ISO: _______________

Lighting Conditions:
- Primary Light Source: _______________
- Secondary Light Sources: _______________
- Light Meter Reading: _______________

Collection Plan:
[ ] Standard position (10 images)
[ ] Rotated 15° clockwise (5 images)
[ ] Rotated 15° counter-clockwise (5 images)
[ ] Shifted left (5 images)
[ ] Shifted right (5 images)
[ ] Shifted forward (5 images)
[ ] Shifted backward (5 images)
[ ] Increased lighting (5 images)
[ ] Decreased lighting (5 images)
[ ] With shadows (5 images)

Assembly Stages:
[ ] Base product (5 images)
[ ] After component 1 (5 images)
[ ] After component 2 (5 images)
...
[ ] Fully assembled (10 images)

Defect Simulation:
[ ] Missing component 1 (3 images)
[ ] Missing component 2 (3 images)
[ ] Incorrectly installed component 1 (3 images)
[ ] Incorrectly installed component 2 (3 images)
```

### 13.2 Annotation Format Examples

**PASCAL VOC Format (XML)**
```xml
<annotation>
  <folder>wukong-dataset</folder>
  <filename>product_A_001.jpg</filename>
  <size>
    <width>3840</width>
    <height>2160</height>
    <depth>3</depth>
  </size>
  <object>
    <name>screw_type_a</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
      <xmin>1245</xmin>
      <ymin>876</ymin>
      <xmax>1289</xmax>
      <ymax>921</ymax>
    </bndbox>
  </object>
  <!-- More objects... -->
</annotation>
```

**COCO Format (JSON)**
```json
{
  "info": {
    "year": 2024,
    "version": "1.0",
    "description": "Wukong Dataset",
    "contributor": "Wukong Team",
    "date_created": "2024-05-15"
  },
  "images": [
    {
      "id": 1,
      "file_name": "product_A_001.jpg",
      "width": 3840,
      "height": 2160,
      "date_captured": "2024-05-15"
    }
  ],
  "annotations": [
    {
      "id": 1,
      "image_id": 1,
      "category_id": 1,
      "bbox": [1245, 876, 44, 45],
      "area": 1980,
      "segmentation": [],
      "iscrowd": 0
    }
  ],
  "categories": [
    {
      "id": 1,
      "name": "screw_type_a",
      "supercategory": "screw"
    }
  ]
}
```

### 13.3 Useful Scripts

**Convert VOC to COCO Format**
```python
import os
import json
import xml.etree.ElementTree as ET
from glob import glob

def voc_to_coco(voc_dir, output_json):
    # Initialize COCO format
    coco = {
        "info": {"year": 2024, "version": "1.0", "description": "Wukong Dataset"},
        "images": [],
        "annotations": [],
        "categories": []
    }
    
    # Create category mapping
    categories = {}
    cat_id = 1
    
    # Process each XML file
    ann_id = 1
    for img_id, xml_file in enumerate(glob(os.path.join(voc_dir, "*.xml"))):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Get image info
        filename = root.find("filename").text
        width = int(root.find("size/width").text)
        height = int(root.find("size/height").text)
        
        # Add image
        coco["images"].append({
            "id": img_id + 1,
            "file_name": filename,
            "width": width,
            "height": height
        })
        
        # Process objects
        for obj in root.findall("object"):
            name = obj.find("name").text
            
            # Add category if new
            if name not in categories:
                categories[name] = cat_id
                coco["categories"].append({
                    "id": cat_id,
                    "name": name,
                    "supercategory": name.split("_")[0]
                })
                cat_id += 1
            
            # Get bounding box
            bbox = obj.find("bndbox")
            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)
            width = xmax - xmin
            height = ymax - ymin
            
            # Add annotation
            coco["annotations"].append({
                "id": ann_id,
                "image_id": img_id + 1,
                "category_id": categories[name],
                "bbox": [xmin, ymin, width, height],
                "area": width * height,
                "iscrowd": 0
            })
            ann_id += 1
    
    # Save to JSON file
    with open(output_json, 'w') as f:
        json.dump(coco, f, indent=2)
    
    print(f"Converted {len(coco['images'])} images with {len(coco['annotations'])} annotations")

# Example usage
voc_to_coco("wukong-dataset/annotations", "wukong-dataset/annotations.json")
```

**Generate Train/Val/Test Split**
```python
import os
import random
import shutil
from glob import glob

def create_dataset_split(image_dir, output_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15, seed=42):
    # Set random seed for reproducibility
    random.seed(seed)
    
    # Get all image files
    image_files = glob(os.path.join(image_dir, "*.jpg"))
    random.shuffle(image_files)
    
    # Calculate split sizes
    total = len(image_files)
    train_size = int(total * train_ratio)
    val_size = int(total * val_ratio)
    
    # Split the data
    train_files = image_files[:train_size]
    val_files = image_files[train_size:train_size+val_size]
    test_files = image_files[train_size+val_size:]
    
    # Create output directories
    os.makedirs(os.path.join(output_dir, "train"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "val"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "test"), exist_ok=True)
    
    # Copy files to respective directories
    for f in train_files:
        shutil.copy(f, os.path.join(output_dir, "train", os.path.basename(f)))
        # Also copy annotation if exists
        ann_file = f.replace(".jpg", ".xml")
        if os.path.exists(ann_file):
            shutil.copy(ann_file, os.path.join(output_dir, "train", os.path.basename(ann_file)))
    
    for f in val_files:
        shutil.copy(f, os.path.join(output_dir, "val", os.path.basename(f)))
        ann_file = f.replace(".jpg", ".xml")
        if os.path.exists(ann_file):
            shutil.copy(ann_file, os.path.join(output_dir, "val", os.path.basename(ann_file)))
    
    for f in test_files:
        shutil.copy(f, os.path.join(output_dir, "test", os.path.basename(f)))
        ann_file = f.replace(".jpg", ".xml")
        if os.path.exists(ann_file):
            shutil.copy(ann_file, os.path.join(output_dir, "test", os.path.basename(ann_file)))
    
    print(f"Split dataset: {len(train_files)} train, {len(val_files)} validation, {len(test_files)} test")

# Example usage
create_dataset_split("wukong-dataset/images", "wukong-dataset/split")
```

**Generate PaddleX Dataset List Files**
```python
import os
from glob import glob

def create_paddlex_list_files(dataset_dir, output_dir):
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all image files and their annotations
    train_images = glob(os.path.join(dataset_dir, "train", "*.jpg"))
    val_images = glob(os.path.join(dataset_dir, "val", "*.jpg"))
    test_images = glob(os.path.join(dataset_dir, "test", "*.jpg"))
    
    # Create label list
    labels = set()
    for xml_file in glob(os.path.join(dataset_dir, "**", "*.xml"), recursive=True):
        with open(xml_file, 'r') as f:
            content = f.read()
            # Extract all class names from XML
            for name in content.split("<name>")[1:]:
                label = name.split("</name>")[0].strip()
                labels.add(label)
    
    # Write label list
    with open(os.path.join(output_dir, "labels.txt"), 'w') as f:
        for label in sorted(labels):
            f.write(f"{label}\n")
    
    # Write train list
    with open(os.path.join(output_dir, "train_list.txt"), 'w') as f:
        for img_path in train_images:
            rel_path = os.path.relpath(img_path, dataset_dir)
            ann_path = os.path.splitext(img_path)[0] + ".xml"
            rel_ann_path = os.path.relpath(ann_path, dataset_dir)
            if os.path.exists(ann_path):
                f.write(f"{rel_path} {rel_ann_path}\n")
    
    # Write val list
    with open(os.path.join(output_dir, "val_list.txt"), 'w') as f:
        for img_path in val_images:
            rel_path = os.path.relpath(img_path, dataset_dir)
            ann_path = os.path.splitext(img_path)[0] + ".xml"
            rel_ann_path = os.path.relpath(ann_path, dataset_dir)
            if os.path.exists(ann_path):
                f.write(f"{rel_path} {rel_ann_path}\n")
    
    # Write test list
    with open(os.path.join(output_dir, "test_list.txt"), 'w') as f:
        for img_path in test_images:
            rel_path = os.path.relpath(img_path, dataset_dir)
            ann_path = os.path.splitext(img_path)[0] + ".xml"
            rel_ann_path = os.path.relpath(ann_path, dataset_dir)
            if os.path.exists(ann_path):
                f.write(f"{rel_path} {rel_ann_path}\n")
    
    print(f"Created PaddleX list files in {output_dir}")

# Example usage
create_paddlex_list_files("wukong-dataset/split", "wukong-dataset")
```
