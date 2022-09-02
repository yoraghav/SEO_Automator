import cv2
import numpy as np
import requests

def slicer(img):
    img = np.array(img)
    crops = np.zeros((6,10,8,3))

    crops[0] = img[9:19,17:25]
    crops[1] = img[9:19,35:43]
    crops[2] = img[9:19,53:61]
    crops[3] = img[9:19,71:79]
    crops[4] = img[9:19,89:97]
    crops[5] = img[9:19,107:115]
    
    return crops

def converter(img):
    key = np.zeros((10,8))

    for i in range(10):
        for j in range(8):
            if(img[i][j][0] == 0):
                key[i][j]=1
    return key
    
def main():
    img = cv2.imread("1.png")
    st = ['1','2','3','4','5','6','7','8','9','A','B','C','E','F','X']
    b = slicer(img)
    ans = ""
    for i in range(6):
        mat = converter(b[i])
        for j in range(len(st)):
            ur = "matrices/"+st[j]+".npy"
            if((np.load(ur) == mat).all()):
                ans = ans + st[j]
                
    return ans




    
