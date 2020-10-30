from injector import Binder, Injector, inject
from interface import implements
from typing import List
import math

from BusinessLogic.Interfaces.IAnnotationsTransformer import IAnnotationsTransformer
from BusinessLogic.Interfaces.IImagesReader import IImagesReader
from BusinessLogic.Interfaces.IWriter import IWriter
from BusinessLogic.Interfaces.IAnnotationsReadersFactory import IAnnotationsReadersFactory
from Entities.AnnotatedImage import AnnotatedImage
from Entities.Enums.AnnotationType import AnnotationType
from IBatchProcessor import IBatchProcessor


class BatchProcessor(implements(IBatchProcessor)):
    @inject
    def __init__(self,
    annotationsReadersFactory: IAnnotationsReadersFactory,
    annotationsTransformer: IAnnotationsTransformer,
    imagesReader: IImagesReader,
    writer: IWriter):
        self.__annotationsReadersFactory = annotationsReadersFactory
        self.__annotationsTransformer = annotationsTransformer
        self.__imagesReader = imagesReader
        self.__writer = writer
    def Process(self,
    annotatedImages: List[AnnotatedImage],
    annotationType: AnnotationType,
    batchSize: int,
    configFile: str,
    outputFile: str):
        numberOfBatches = math.ceil(len(annotatedImages)/batchSize)
        for batch in range(numberOfBatches):
            print("Processing batch " +  str(batch + 1) + " out of " + str(numberOfBatches))
            start = batch*batchSize
            if batch == numberOfBatches - 1:
                end = len(annotatedImages)
            else:
                end = start + batchSize
            annotatedImagesToProcess = annotatedImages[start:end]
            imagePathsToProcess = [annotatedImage.GetImagePath() for annotatedImage in annotatedImagesToProcess]
            annotationPathsToProcess = [annotatedImage.GetAnnotationPath() for annotatedImage in annotatedImagesToProcess]
            images = self.__imagesReader.Read(imagePathsToProcess)
            annotationsReader = self.__annotationsReadersFactory.Create(annotationType)
            annotations = annotationsReader.Read(annotationPathsToProcess)
            transformedAnnotations = self.__annotationsTransformer.Transform(annotations, configFile)
            self.__writer.Write(images, transformedAnnotations, outputFile=outputFile)
        
        