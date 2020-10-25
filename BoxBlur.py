#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:23:30 2020

@author: yuwenchen
"""
image = [[7,4,0,1], 
 [5,6,2,2], 
 [6,10,7,8], 
 [1,4,2,0]]

def boxBlur(image):
    filterWid = len(image[0])
    filterHig = len(image)
    res = []
    
    for j in range(filterHig):
        widlist = []
        for i in range(filterWid):
            if i<1 or j<1 or i+1 == filterWid or j+1 == filterHig: # Kernel doesn't fit
                continue
            else:
                #print(j,i)
                kernel = image[j-1][i-1]+\
                         image[j-1][i+0]+\
                         image[j-1][i+1]+\
                         image[j+0][i-1]+\
                         image[j+0][i+0]+\
                         image[j+0][i+1]+\
                         image[j+1][i-1]+\
                         image[j+1][i+0]+\
                         image[j+1][i+1]
                kernel = kernel // 9   
                widlist.append(kernel)
        
        if widlist:
            res.append(widlist)
        
    
    return res

print(boxBlur(image))