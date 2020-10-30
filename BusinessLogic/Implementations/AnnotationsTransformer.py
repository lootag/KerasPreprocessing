from interface import implements
from typing import List

from ..Interfaces.IAnnotationsTransformer import IAnnotationsTransformer
from Entities.Annotation import Annotation
import json

class AnnotationsTransformer(implements(IAnnotationsTransformer)):
    def Transform(self,
    annotations: List[Annotation],
    configFile: str) -> List:
        print("transforming annotations")
        transformedAnnotations = []
        with open(configFile) as cf:
            classDictionary = json.load(cf)
            numberOfClasses = len(classDictionary)
            numberOfObjects = 5*numberOfClasses
            for annotation in annotations:
                transformedAnnotation = [0]*numberOfClasses*numberOfObjects + [-1]*4*numberOfObjects
                classNames = annotation.GetClassNames()
                boundingBoxes = annotation.GetBoundingBoxes()
                for classNameIndex in range(len(classNames)):
                    classIndex = classDictionary[classNames[classNameIndex]]
                    oneHotEncodedClass = [0]*numberOfClasses
                    oneHotEncodedClass[classIndex] = 1
                    transformedAnnotation[classNameIndex*numberOfClasses: classNameIndex*numberOfClasses + numberOfClasses] = oneHotEncodedClass
                for boundingBoxIndex in range(len(boundingBoxes)):
                    transformedAnnotation[numberOfClasses*numberOfObjects + boundingBoxIndex*4] = int(boundingBoxes[boundingBoxIndex].GetXMin())
                    transformedAnnotation[numberOfClasses*numberOfObjects + boundingBoxIndex*4 + 1] = int(boundingBoxes[boundingBoxIndex].GetYMin())
                    transformedAnnotation[numberOfClasses*numberOfObjects + boundingBoxIndex*4 + 2] = int(boundingBoxes[boundingBoxIndex].GetXMax())
                    transformedAnnotation[numberOfClasses*numberOfObjects + boundingBoxIndex*4 + 3] = int(boundingBoxes[boundingBoxIndex].GetYMax())
                transformedAnnotations.append(transformedAnnotation)
            return transformedAnnotations
            
                




                 
                
