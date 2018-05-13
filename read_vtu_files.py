#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 08:17:38 2018

@author: oguz
"""



f1=open('EmbeddedSphere_0.vtu','r') #cube
f2=open('EmbeddedSphere_wholeSurface_0.vtu','r') #sphere



#Check line by line if "NumberOfPoints" string is in those lines.
for line in f1:
    if "NumberOfPoints" in line : the_line_1=line    
for line in f2:
    if "NumberOfPoints" in line : the_line_2=line

print('The line that we found for cube is : ',the_line_1)
print('The line that we found for sphere is : ',the_line_2)

print('The lines of 1 splitted: ',the_line_1.split())
print('The lines of 2 splitted: ',the_line_2.split())
print("")

    
for word in the_line_2.split():
    if "NumberOfPoints" in word:
        num_of_points_2=word[16 :-1]


for word in the_line_2.split():
    if "NumberOfCells" in word:
        num_of_cells_2=word[15 :-2]
        
print('Number of points in Sphere',num_of_points_2)
print('Number of Cells in Sphere',num_of_cells_2)

print('')
        



# We close the files, since we found the lines we want from them.
f1.close()
f2.close()

for word in the_line_1.split():
    if "NumberOfPoints" in word:
        num_of_points_1=word[16 :-1]


for word in the_line_1.split():
    if "NumberOfCells" in word:
        num_of_cells_1=word[15 :-2]
        

print('Number of points in Sphere',num_of_points_1)
print('Number of Cells in Sphere',num_of_cells_1)
        
        

#below are trials, can be ignored.

##for char in range(1,len(the_line)-9):
##    if the_line[char]=='N' and  the_line[char+1]=='u' and the_line[char+2]=='m' and the_line[char+8]=='P':
##        print (the_line[char+15 :]) 
        
            

##for i in range(1,5):
##    print (f.readline())    
##print (f.readline())
##print (f.readline())
##print (f.readline())
##f.write("hello world")
##f.close()
##
##fread=open('test.txt','r')
##print (fread.read())