class AnnotatedImage:
    def __init__(self,
    imagePath: str,
    annotationPath: str):
        self.__ImagePath = imagePath
        self.__AnnotationPath = annotationPath
    def GetImagePath(self) -> str:
        return self.__ImagePath
    def GetAnnotationPath(self) ->str:
        return self.__AnnotationPath