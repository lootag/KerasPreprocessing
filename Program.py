from injector import Binder, Injector, inject
from typing import List
import os
import sys
import argparse

from BusinessLogic.Interfaces.IAnnotationsTransformer import IAnnotationsTransformer
from BusinessLogic.Interfaces.IAnnotationsReadersFactory import IAnnotationsReadersFactory
from BusinessLogic.Interfaces.IImagesReader import IImagesReader
from BusinessLogic.Interfaces.IWriter import IWriter
from BusinessLogic.Interfaces.IValidator import IValidator
from IBatchProcessor import IBatchProcessor
from BusinessLogic.Implementations.ImagesReader import ImagesReader
from BusinessLogic.Implementations.AnnotationsTransformer import AnnotationsTransformer
from BusinessLogic.Implementations.AnnotationsReadersFactory import AnnotationsReadersFactory
from BusinessLogic.Implementations.Writer import Writer
from BusinessLogic.Implementations.Validator import Validator
from BatchProcessor import BatchProcessor
from Entities.AnnotatedImage import AnnotatedImage
from Entities.Enums.AnnotationType import AnnotationType


class Program: 
    @inject 
    def __init__(self, 
    batchProcessor: IBatchProcessor,
    validator: IValidator):
        self.__batchProcessor = batchProcessor
        self.__validator = validator
    def main(self):
        self.__makeOutputDirectoryIfIDoesntExist()
        parser = argparse.ArgumentParser(description="A small CLI app to create keras ready annotated images")
        parser.add_argument('--batch_size', dest="batchSize", type=int, default=10)
        parser.add_argument('--annotation_type', dest="annotationType", type=str, default="PASCAL_VOC")
        args = parser.parse_args()
        batchSize = args.batchSize
        annotationType = AnnotationType[args.annotationType]
        configFile = "classes.json"
        outputFile = "Output/output.h5"
        self.__deleteOutputIfItExists(outputFile)
        self.__batchProcessor.Process(annotatedImages=self.__getAllAnnoatedImages(),
        annotationType=annotationType,
        batchSize=batchSize,
        configFile=configFile,
        outputFile=outputFile)
    def __getAllAnnoatedImages(self) -> List[AnnotatedImage]:
        annotatedImages: List[AnnotatedImage] = []
        imageNames = os.listdir("Images")
        imagePaths = ["Images/" + imageName for imageName in imageNames]
        annotationNames = os.listdir("Annotations")
        annotationPaths = ["Annotations/" + annotationName for annotationName in annotationNames]
        validationResult = self.__validator.Validate(imagePaths=imagePaths,
                                                     imageNames=imageNames,
                                                     annotationPaths=annotationPaths)
        if not validationResult:
            print("There's something wrong in your input! Check it and then try again please")
            sys.exit()
        for imageNameIndex in range(len(imageNames)):
            imageName = imageNames[imageNameIndex]
            imagePath = "Images/" + imageName
            annotationPath = "Annotations/" + imageName[:len(imageName) - 3] + "xml"
            annotatedImage = AnnotatedImage(imagePath=imagePath, annotationPath=annotationPath)
            annotatedImages.append(annotatedImage)
        return annotatedImages
    
    def __deleteOutputIfItExists(self,
    outputFile: str):
        if os.path.exists(outputFile):
            os.remove(outputFile)
    
    def __makeOutputDirectoryIfIDoesntExist(self):
        if not os.path.exists("Output"):
            os.mkdir("Output")
def resolveDependencies(binder: Binder):
    binder.bind(IImagesReader, to=ImagesReader)
    binder.bind(IAnnotationsReadersFactory, to=AnnotationsReadersFactory)
    binder.bind(IAnnotationsTransformer, to=AnnotationsTransformer)
    binder.bind(IWriter, to=Writer)
    binder.bind(IValidator, to=Validator)
    binder.bind(IBatchProcessor, to=BatchProcessor)







injector = Injector(resolveDependencies)
program = injector.get(Program)

if __name__=="__main__":
    program.main()