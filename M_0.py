﻿
'''Փոխել 0-ները հարևան M-երի քանակով '''

x=[[0,'M',0,'M',0],
   [0,0,'M',0,0],
   [0,0,0,0,0],
   ['M','M',0,0,0],
   [0,0,0,'M',0]]



for i in range(0,5):
    for j in range(0,5):
        if x[i][j]!='M':
            for i1 in range(-1,2):
                for j1 in range(-1,2):
                    if i+i1>=0 and i+i1<=4 and j+j1>=0 and j+j1<=4 and x[i+i1][j+j1]=='M':
                        x[i][j]+=1
        print(x[i][j],end="")
    print("")
