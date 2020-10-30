from interface import implements
from typing import List
import numpy as np
import cv2

from ..Interfaces.IImagesReader import IImagesReader

class ImagesReader(implements(IImagesReader)):
    def Read(self,
    paths: List[str]) -> List:
        print("reading images")
        images = []
        for path in paths:
            npImage = cv2.imread(path)
            npImageRgb = cv2.cvtColor(npImage, cv2.COLOR_BGR2RGB)
            image = npImageRgb.tolist()
            images.append(image)
        return images

        