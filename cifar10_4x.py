from PIL import Image
import os
import numpy as np
import pickle
from typing import Any, Callable, Optional, Tuple

from torchvision.datasets.vision import VisionDataset


class CIFAR10_4x(VisionDataset):
    """

    Args:
        root (string): Root directory of dataset where directory
            ``cifar-10-batches-py`` exists or will be saved to if download is set to True.
        split : tarin, valid or test
    """
    base_folder = 'cifar_10_4x'

    file_dic = {
        "train": "train",
        "valid": "valid",
        "test": "test"
    }

    meta = {
        'filename': 'batches.meta',
        'key': 'label_names',
    }

    def __init__(
            self,
            root: str,
            split: str = 'train',
    ) -> None:

        super(CIFAR10_4x, self).__init__(root)

        self.split = split  # training set or test set


        file_name = self.file_dic[split]

        self.data: Any = []
        self.targets = []

        # now load the picked numpy arrays

        file_path = os.path.join(self.root, self.base_folder, file_name)
        with open(file_path, 'rb') as f:
            entry = pickle.load(f, encoding='latin1')
            self.data.append(entry['data'])
            if 'labels' in entry:
                self.targets.extend(entry['labels'])
            else:
                self.targets.extend(entry['fine_labels'])

        self.data = np.vstack(self.data) # HWC

        self._load_meta()

    def _load_meta(self) -> None:
        path = os.path.join(self.root, self.base_folder, self.meta['filename'])

        with open(path, 'rb') as infile:
            data = pickle.load(infile, encoding='latin1')
            self.classes = data[self.meta['key']]
        self.class_to_idx = {_class: i for i, _class in enumerate(self.classes)}

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        img, target = self.data[index], self.targets[index]
        img = img.transpose(2, 0, 1) # HWC -> CHW

        return img, target

    def __len__(self) -> int:
        return len(self.data)

    def extra_repr(self) -> str:
        return "Split: {}".format(self.split)
