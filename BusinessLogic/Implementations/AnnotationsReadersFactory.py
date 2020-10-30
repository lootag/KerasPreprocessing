from interface import implements

from ..Interfaces.IAnnotationsReader import IAnnotationsReader
from ..Interfaces.IAnnotationsReadersFactory import IAnnotationsReadersFactory
from ..Implementations.PascalVocReader import PascalVocReader
from Entities.Enums.AnnotationType import AnnotationType

class AnnotationsReadersFactory(implements(IAnnotationsReadersFactory)):
    def Create(self,
    annotationType: AnnotationType) -> IAnnotationsReader:
        if annotationType == AnnotationType.PASCAL_VOC:
            return PascalVocReader()
        else:
            raise("The annotation type you have inserted is not supported.")
        