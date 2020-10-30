from typing import List

from Entities.BoundingBox import BoundingBox

class Annotation:
    def __init__(self,
    classNames: List[str],
    boundingBoxes: List[BoundingBox]):
        self.__ClassNames = classNames
        self.__BoundingBoxes = boundingBoxes
    def GetClassNames(self) -> List[str]:
        return self.__ClassNames
    def GetBoundingBoxes(self) -> List[BoundingBox]:
        return self.__BoundingBoxes