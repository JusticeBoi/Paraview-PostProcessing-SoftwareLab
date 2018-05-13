#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:22:28 2018

@author: oguz
"""
def clean_start():
    Disconnect()
    Connect()
    return

clean_start()

paraview.simple._DisableFirstRenderCameraReset()

r1=OpenDataFile("/home/oguz/Desktop/tum/softwarelab/paraview_vtufiles/EmbeddedSphere_0.vtu") #cube
renderView1 = GetActiveViewOrCreate('RenderView')
r2=OpenDataFile("/home/oguz/Desktop/tum/softwarelab/paraview_vtufiles/EmbeddedSphere_wholeSurface_0.vtu")#sphere



SetActiveSource(r1)

#Create a calculator
calculator1 = Calculator()

#for now the function is set  to empty.
calculator1.Function = ''

r=input('what is the radius= \n ')

cx=input(' x coord of center of the sphere= \n ')
cy=input(' y coord of center of the sphere= \n ')
cz=input(' z coord of center of the sphere= \n ')

#calculator1.Function takes a string, so we format the string according to the provided input from the usr, in this case.
inp='((coordsX-{})^2)+((coordsY-{})^2)+((coordsZ-{})^2)<{}^2'.format(cx,cy,cz,r)

#FOR THE GIVEN OBJECT, USE R=0.1, CX,CY,CZ = 0.5 FOR GOOD VISUAL RESULTS.

calculator1.Function = inp

#show calc.
calcdisp=Show(calculator1)

#hide calc.
Hide(calculator1)


SetActiveSource(calculator1)

#Create a threshold filter
threshold1 = Threshold(Input=calculator1)

threshold1.Scalars = ['POINTS', 'Result']

#where 1.0 is the cells with points that are inside the provided sphere and 0.0 are outside.

#if we set threshold to 0.2 to 1.0,it wont show the cells outside of the given function
threshold1.ThresholdRange = [0.2, 1.0]

#alternatively one could do;
#threshold1.ThresholdRange = [0.0, 0.9]
#to see not see the cells that are inside of the provided sphere.

#show it.
thresdisp=Show(threshold1,renderView1)