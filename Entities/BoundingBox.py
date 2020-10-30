class BoundingBox:
    def __init__(self,
    xMin: int,
    yMin: int,
    xMax: int,
    yMax: int):
        self.__XMin = xMin
        self.__Ymin = yMin
        self.__XMax = xMax
        self.__YMax = yMax
    def GetXMin(self) -> int:
        return self.__XMin
    def GetYMin(self) -> int:
        return self.__Ymin
    def GetXMax(self) -> int:
        return self.__XMax
    def GetYMax(self) -> int:
        return self.__YMax

