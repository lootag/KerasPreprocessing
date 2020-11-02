from interface import Interface
from typing import List
from Entities.Annotation import Annotation

class IAnnotationsReader(Interface):
    def Read(self,
    paths: List[str]) -> List[Annotation]:
        pass

