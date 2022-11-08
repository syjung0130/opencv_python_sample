# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = np.zeros((120, 120), dtype=np.uint8) # 120x120 2차원 배열 생성, 검은색 흑백 이미지
img[25:35, :] = 45 # 25~35행 모든 열에 45 할당
img[55:65, :] = 115 # 55~65행 모든 열에 115 할당
img[85:95, :] = 160 # 85~95행 모든 열에 160 할당
img[:, 35:45] = 205 # 모든 행 35~45 열에 205 할당
img[:, 75:85] = 255 # 모든 행 75~85 열에 255 할당


cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 2차원 배열이고 가질 수 있는 값은 0 ~ 255 사이가 된다.  
## OpenCV에서 이미지를 표현하기 위한 NumPy배열은 반드시 dtype이 uint8이어야 한다.
## 0은 검은색을 의미하고 255는 흰색을 의미하므로
## 그 사이의 값은 값이 커질 수록 밝은 색을 나타내고
## 값이 작아질수록 어두운 색을 표현하는 1채널 그레이 스케일 이미지를 표현할 수 있다.
## 완전히 검은 바탕에 행단위와 열단위로 점점 밝은 값일 지정해서 체크무늬를 만들었다.