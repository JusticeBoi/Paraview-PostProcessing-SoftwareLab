### SOFTWARE LAB 2018
### Phyton-based Paraview sPostProcessor
### Students: Oguz Oztoprak & Darwin Droll
### Supervisors: John Jomo & Benjamin Wassermann
### Disclaimer: Works on our machine, soo.

### May 2018


### HOW IT WORKS

## Run script, it will ask x,y,z coordinates respectively, of a point and it will show and save the cell that

## contains that point. The default saving format is MLUnstructuredGrid, .vtu .


from paraview.simple import *

#When in python shell of paraview, with this func have a clean start.
def clean_start():
    Disconnect()    
    Connect()
    return


clean_start()

#copied from trace, hopefully helps?
paraview.simple._DisableFirstRenderCameraReset()



#Directory information. You should change it.
object_directory="C:\Users\Darwin\OneDrive\TUM\Softwarelab\paraview_vtufiles\\"
#object_directory="/home/oguz/Desktop/tum/softwarelab/paraview_vtufiles/"
cube="EmbeddedSphere_0.vtu"
sphere="EmbeddedSphere_wholeSurface_0.vtu"

#r1 is the cube object
r1=OpenDataFile(object_directory+cube) 

#Create a Render view.
renderView1 = GetActiveViewOrCreate('RenderView')

#display r1,which is the cube, in the Render view
r1_disp=Show(r1,renderView1) 


# It is like left clicking once on the cube object, now any filter will be applied on this cube.
SetActiveSource(r1)


#Get the input parameters as floats
#try for example 0.5, 0.5, 0.5 
ext_loc_x=float(input("X coord of the location: \n\n"))

ext_loc_y=float(input("Y coord of the location: \n\n"))

ext_loc_z=float(input("Z coord of the location: \n\n"))

#List the parameters, Location property below accepts a list
inp_list=[ext_loc_x,ext_loc_y,ext_loc_z] 

#create a ExtractLocation filter
extract_loc=ExtractLocation()

#this is the mode that we want.
extract_loc.Mode = 'Extract Cell At Location' 

# Enter which location to extract as a list
extract_loc.Location=inp_list 


# Hide the cube itself
Hide(r1,renderView1) 

# Show the extracted Location
extract_loc_disp=Show(extract_loc,renderView1) 

# updates the view.
renderView1.Update()


# Now we prepare for changing the main view from Render view to Spreadsheet view.
#Delete(renderView1) 
#del renderView1

#Create a new SphreadSheetView
spreadSheetView1 = CreateView('SpreadSheetView')
    
 #Some default properties.
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
    
## PREVIOUSLY THERE WERE SOME LAYOUT STUFF WAS HERE.
## CAUSED ERRORS SO I JUST DELELTED IT AND IT WORKS FINE, FOR NOW xD.


#show the extracted part in spreadsheetview
extract_loc_disp=Show(extract_loc,spreadSheetView1)
spreadSheetView1.Update()
RenderAllViews()

#Shows the Cell Data for 1, Shows the Point Data for 0
extract_loc_disp.SetPropertyWithName('FieldAssociation',1)



#This is something i found, which seems easier and the format is just like the given geometry's format.
#In my pc this is saved in /Home/selected_point.vtu
writer = XMLUnstructuredGridWriter(FileName="selected_point.vtu")
writer.UpdatePipeline()
del writer






# # ##OLD WAY OF SAVING

# # # input 1 directs  the user to save the selected cell in a vtu format in the same place as the object directory
# # # input 0 directs the user to save the selected cell in a vtu format in a new directory.

# # #where_to_save=int(raw_input('Saving the file the same location where your object is %s, if OK press 1, if not ok press 0\n\n' %object_directory))
# # #if where_### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # ##to_save==1:
# # #    name=### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # raw_input('name of the vtu file(without .vtu): \n\n')
# # #    direc### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # tory_input=object_directory+name+'.vtu'
# # #    SaveD### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # ata(directory_input, proxy=extract_loc)
# # #elif wher### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # e_to_save==0:
# # #    name=### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # raw_input('name of the vtu file(without .vtu): \n\n')
# # #    new_s### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # ave_loc=raw_input('Write the directory of the file (i.e. /home/oguz/Desktop/) \n\n')
# # #    direc### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # tory_input=new_save_loc+name+'.vtu'
# # #    SaveD### SOFTWARE LAB 2018
# # ### Phyton-based Paraview sPostProcessor
# # ### Students: Oguz Oztoprak & Darwin Droll
# # ### Supervisors: John Jomo & Benjamin Wassermann
# # ### Disclaimer: Works on our machine, soo.
# # ata(object_directory, proxy=extract_loc)
    

# # ##OLD WAY OF SAVING FINISHED HERE


# # ##To see the properties of any object, just get the ListProperties() function, like shown below, and it will show which properties
# #     # you can set. Setting a property is also shown below
    
    
# # ##extract_loc_disp.ListProperties()
# # ##
# # ##spreadSheetView1.SetPropertyWithName('SelectionOnly',1)
# # ##spreadSheetView1.SetPropertyWithName('SelectionOnly',0)
