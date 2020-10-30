from interface import implements
from typing import List
import untangle

from Entities.Annotation import Annotation
from Entities.BoundingBox import BoundingBox

from ..Interfaces.IAnnotationsReader import IAnnotationsReader

class PascalVocReader(implements(IAnnotationsReader)):
    def Read(self,
    paths: List[str]) -> List[Annotation]:
        print("reading annotations")
        annotations = []
        for path in paths:
            dto = untangle.parse(path)
            classNames = []
            boundingBoxes = []
            for obj in dto.annotation.object:
                classNames.append(obj.name.cdata)
                boundingBox = BoundingBox(xMin=obj.bndbox.xmin.cdata, yMin=obj.bndbox.ymin.cdata, xMax=obj.bndbox.xmax.cdata, yMax=obj.bndbox.ymax.cdata)
                boundingBoxes.append(boundingBox)
            annotation = Annotation(classNames=classNames, boundingBoxes=boundingBoxes)
            annotations.append(annotation)  
        return annotations

        