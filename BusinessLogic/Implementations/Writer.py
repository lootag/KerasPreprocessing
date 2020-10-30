from interface import implements
from typing import List
import numpy as np
import h5py
import os

from ..Interfaces.IWriter import IWriter

class Writer(implements(IWriter)):
    def Write(self,
    images: List,
    transformedAnnotations: List,
    outputFile: str):
        print("writing")
        imagesAsNumpyArray = np.array(images)
        transformedAnnotationsAsNumpyArray = np.array(transformedAnnotations)
        if not os.path.exists(outputFile):
            output = h5py.File(outputFile, 'w')
            output.create_dataset("features", data=imagesAsNumpyArray, compression="gzip", chunks=True, maxshape=(None,imagesAsNumpyArray.shape[1], imagesAsNumpyArray.shape[2], imagesAsNumpyArray.shape[3]))
            output.create_dataset("labels", data=transformedAnnotationsAsNumpyArray, compression="gzip", chunks=True, maxshape=(None,transformedAnnotationsAsNumpyArray.shape[1]))
        else:
            with h5py.File(outputFile, 'a') as output:
                output["features"].resize((output["features"].shape[0] + imagesAsNumpyArray.shape[0]), axis=0)
                output["features"][-imagesAsNumpyArray.shape[0]:] = imagesAsNumpyArray
                output["labels"].resize((output["labels"].shape[0] + transformedAnnotationsAsNumpyArray.shape[0]), axis=0)
                output["labels"][-transformedAnnotationsAsNumpyArray.shape[0]:] = transformedAnnotationsAsNumpyArray



