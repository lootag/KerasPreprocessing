from interface import implements
from typing import List
import os

from ..Interfaces.IValidator import IValidator

class Validator(implements(IValidator)):
    def Validate(self,
    imagePaths: List[str],
    imageNames: List[str],
    annotationPaths: List[str]) -> bool:
        print("validating")
        allFilesAreImages = self.__checkAllFilesAreImages(imagePaths)
        allImagesAreAnnotated = self.__checkAllImagesAreAnnotated(imageNames)
        return allFilesAreImages and allImagesAreAnnotated
    
    def __checkAllFilesAreImages(self,
    imagePaths: List[str]) -> bool:
        for imagePath in imagePaths:
            extension = imagePath[len(imagePath) - 3: len(imagePath)]
            if extension != "jpg" and extension != "png":
                return False

        return True
    
    def __checkAllImagesAreAnnotated(self,
    imageNames: List[str]) -> bool:
        for imageName in imageNames:
            theoreticalAnnotationPath = "Annotations/" + imageName[:len(imageName) - 3] + "xml"
            if not os.path.isfile(path = theoreticalAnnotationPath):
                return False
            
        return True

