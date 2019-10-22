#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 23:52:45 2019

@author: beneragon
"""

import cv2
#cv2.nameWindow('"Daenerys",cv2.WINDOW_NORMAL)
img = cv2.imread('/home/beneragon/Pictures/Daenerys.jpg')
nimg = cv2.resize(img,(1280,800))
cv2.imshow("Daenerys",nimg)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image