import cv2
import numpy as np
from PIL import Image


image = np.array(Image.open('img.png')) # 이미지 불러와서 numpy 배열화

image = cv2.pyrDown(image) # 배열 사이즈 축소

y, x, z = np.shape(image) # 사이즈 가져오기



print("img x, y, z : ", x, y, z) 





for i in range(y):

    for j in range(x):


        if image[i][j][0] >= 255 and image[i][j][1] >= 255 and image[i][j][2] >= 255 and image[i][j][3] >= 255:
            print('□', end='')

        else:
            print('■', end='')

    print()

