import torch
from torchvision import datasets
from pycocotools.coco import COCO
from helmet.constants import ANNOTATIONS_COCO_JSON_FILE
from helmet.exception import HelmetException
import cv2
import os
import sys
import copy

class HelmetDetection(datasets.VisionDataset):
    def __init__(self, root, split='train', transform=None, target_transform=None, transforms=None):
        super().__init__(root, transforms, transform, target_transform)
        self.split = split
        self.coco = COCO(os.path.join(root, split, ANNOTATIONS_COCO_JSON_FILE))
        self.ids = list(sorted(self.coco.imgs.keys()))