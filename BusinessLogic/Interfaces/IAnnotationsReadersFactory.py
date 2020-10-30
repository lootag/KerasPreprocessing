from interface import Interface

from Entities.Enums.AnnotationType import AnnotationType
from ..Interfaces.IAnnotationsReader import IAnnotationsReader

class IAnnotationsReadersFactory(Interface):
    def Create(self, 
    annotationType: AnnotationType) -> IAnnotationsReader:
        pass