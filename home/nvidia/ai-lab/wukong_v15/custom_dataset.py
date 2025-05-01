import os
from ppdet.core.workspace import register, serializable
# Import the base class it should inherit from
from ppdet.data.source.keypoint_source import KeypointTopDownSource

@register
@serializable
class CustomKeypointDataset(KeypointTopDownSource):
    """Custom keypoint dataset placeholder."""

    def __init__(self,
                 dataset_dir=None,
                 image_dir=None,
                 anno_path=None,
                 num_joints=6,
                 trainsize=[192, 256],
                 pixel_std=200,
                 use_gt_bbox=True,
                 **kwargs): # Accept extra args
        super(CustomKeypointDataset, self).__init__(
            dataset_dir=dataset_dir,
            image_dir=image_dir,
            anno_path=anno_path,
            num_joints=num_joints,
            trainsize=trainsize,
            pixel_std=pixel_std,
            use_gt_bbox=use_gt_bbox,
            **kwargs) # Pass extra args

    # No need to override parse_dataset unless custom logic is needed.
    # The parent class's implementation will be used by default.
    # The infer.py script likely uses TestReader transforms for --infer_img,
    # so this class mainly needs to exist and be loadable.