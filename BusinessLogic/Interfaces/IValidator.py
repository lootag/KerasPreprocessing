from interface import Interface
from typing import List

class IValidator(Interface):
    def Validate(self,
    imagePaths: List[str],
    imageNames: List[str],
    annotationPaths: List[str]) -> bool:
        pass