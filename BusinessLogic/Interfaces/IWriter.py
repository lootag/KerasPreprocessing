from interface import Interface
from typing import List

class IWriter(Interface):
    def Write(self,
    images: List,
    transformedAnnotations: List,
    outputFile: str) -> None: 
        pass