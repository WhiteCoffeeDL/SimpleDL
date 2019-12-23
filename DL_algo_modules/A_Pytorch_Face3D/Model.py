import cv2
import numpy as np
from common.global_value import GLOBAL_VALUE

class Model():
    def __init__(self, gpu_mode=False):
        self.gpu_mode = gpu_mode
        self.KEY = "Face3D"

    def __call__(self, img, landmark, result=None):
        if None == result:
            result = {}
        if None == img or None == landmark:
            return result
        
        face_count = len(landmark)
        if 1 == face_count:
            tmp_result = self.forward(img, landmark)
        else:
            tmp_result = []
            for tmp_landmark in landmark:
                tmp = self.forward(img, tmp_landmark)
                tmp_result.append(tmp)
        
        result[self.KEY] = tmp_result

    def forward(self, img, landmark):
        #TODO
        