#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:12:41 2018

@author: oguz
"""

from paraview.simple import *


## Run this script, with proper source directories, and select some cells or points using the renderview GUI. 

## When you are done selecting, simply call SaveSelection() from the paraview python shell to Save the selection -

## as an unstructured grid in a xml-based vtk data file .

## ShowAndSaveSelection() Shows both the RenderView and SpreadSheetView of the selected points/cells and saves it just like SaveSelection().






def clean_start():
    Disconnect()    
    Connect()
    

#GetSelectionSource function written by Utkarsh Ayachit from kitware.com
#Basically returns the selected parts, which will be used as ExtractSelection's parameter.
def GetSelectionSource(proxy=None):
    """If a selection has exists for the proxy (if proxy is not specified then
       the active source is used), returns that selection source"""
    if not proxy:
        proxy = GetActiveSource()
    if not proxy:
        raise RuntimeError, \
        "GetSelectionSource() needs a proxy argument of that an active source is set."
    return proxy.GetSelectionInput(proxy.Port)





    
    

clean_start()

#copied from trace, hopefully helps?
paraview.simple._DisableFirstRenderCameraReset()



#Directory information. You should change it.
object_directory="/home/oguz/Desktop/tum/softwarelab/paraview_vtufiles/"
cube="EmbeddedSphere_0.vtu"
sphere="EmbeddedSphere_wholeSurface_0.vtu"

#r1 is the cube objecttime.sleep(20)
r1=OpenDataFile(object_directory+cube) 

#Create a Render view.
renderView1 = GetActiveViewOrCreate('RenderView')

#display r1,which is the cube, in the Render view
r1_disp=Show(r1,renderView1) 


# It is like left clicking once on the cube object, now any filter will be applied on this cube.
SetActiveSource(r1)


#Function assumes the Active Source is the one that we are selecting from.
#This one creates another layout, in which the selected points/cells are shown in spreadsheetview.
#In the original layout the selected part's RenderView is shown.
#Finally the selected part is saved by writer.
def ShowAndSaveSelection():
    
    
    active_selection = GetSelectionSource()
    
    #Creating our ExtractSelection source, from the selected parts.
    ex_sel=ExtractSelection(Selection=active_selection)
    
    HideAll()
    
    #Show only the extracted selection in Layout 1
    ex_sel_disp=Show(ex_sel)
    
    #updates any RenderView related changes( like hide, show, .. )
    RenderAllViews()
    
    #New Layout
    CreateLayout('Layout #2')
    SetActiveView(None)
    
    #Creating a spreadSheetview 
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024L
    
    #Creating a layout and assigning it the spreadSheetview1
    layout2 = GetLayout()
    layout2.AssignView(0, spreadSheetView1)
    
    #Display the ExtractSelection source in spreadSheetView on Layout 2
    disp=Show(ex_sel,spreadSheetView1)
    
    #We want to see the Cell Data with connnecting points
    disp.FieldAssociation = 'Cell Data' 
    disp.GenerateCellConnectivity=1


    #Update the changes
    spreadSheetView1.Update()
    RenderAllViews()
    ex_sel.UpdatePipeline()
    
    #Saving procedure
    writer = XMLUnstructuredGridWriter(FileName="Mouse_Selected.vtu")
    writer.UpdatePipeline()
    del writer
    Delete()
    
    
    #A lot simpler and cleaner function, which just saves the selected data.
def SaveSelection():
    
    active_selection = GetSelectionSource()
    ex_sel=ExtractSelection(Selection=active_selection)
    
    
    #Saving procedure
    writer = XMLUnstructuredGridWriter(FileName="Mouse_Selected.vtu")
    writer.UpdatePipeline()
    del writer
    Delete()
    
   
        
    
    
    
    
    
    
    






#spreadSheetView1.SetPropertyWithName('SelectionOnly',1)