from interface import Interface
from typing import List


from Entities.Annotation import Annotation


class IAnnotationsTransformer(Interface):
    def Transform(self,
    annotations: List[Annotation],
    configFile: str) -> List:
        pass