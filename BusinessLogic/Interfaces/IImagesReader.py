from interface import Interface
from typing import List

class IImagesReader(Interface):
    def Read(self,
    paths: List[str]) -> List:
        pass