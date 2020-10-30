from interface import Interface
from typing import List

from Entities.AnnotatedImage import AnnotatedImage
from Entities.Enums.AnnotationType import AnnotationType

class IBatchProcessor(Interface):
    def Process(self,
    annotatedImages: List[AnnotatedImage],
    annotationType: AnnotationType,
    batchSize: int,
    configFile: str,
    outputFile: str):
        pass
        