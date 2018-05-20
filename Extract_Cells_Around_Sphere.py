### SOFTWARE LAB 2018
### Phyton-based Paraview sPostProcessor
### Students: Oguz Oztoprak & Darwin Droll
### Supervisors: John Jomo & Benjamin Wassermann
### Disclaimer: Works on our machine, soo.

### May 2018
### Extracting Cells around the given sphere.

### We know that the center of the sphere is in 0.5,0.5,0.5 and the radius of sphere is 0.1.


from paraview.simple import *

def clean_start():
    Disconnect()    
    Connect()


#Directory information. You should change it.
object_directory="/home/oguz/Desktop/tum/softwarelab/paraview_vtufiles/"
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



# Creating the ExtractCellsbyRegion proxy from the cube.
cells_around_sphere = ExtractCellsByRegion(Input=r1)


# We want the cells that are inside
cells_around_sphere.IntersectWith = 'Sphere'
cells_around_sphere.Extractonlyintersected = 1
cells_around_sphere.Extractintersected = 1
cells_around_sphere.IntersectWith.Center=[0.5,0.5,0.5]


cells_around_sphere.IntersectWith.Radius = 0.1000

# show data in view

HideAll()
cells_around_sphere_disp = Show(cells_around_sphere, renderView1)

#Saving every cell intersecting with the sphere
#Saving procedure
writer1 = XMLUnstructuredGridWriter(FileName="Cells_around_sphere.vtu")
writer1.UpdatePipeline()
del writer1

HideAll()


SetActiveSource(cells_around_sphere)

# Extracting the cells around the mid section of the sphere.
cells_on_plane=ExtractCellsByRegion()

cells_on_plane.IntersectWith='Plane'

cells_on_plane.IntersectWith.Origin = [0.5, 0.5, 0.5]

cells_on_plane.IntersectWith.Normal = [0.0, 0.0, -1.0]

# Only the cells inside are showed.
cells_on_plane.Extractonlyintersected = 1
cells_on_plane.Extractintersected = 1

# Properties modified on extractCellsByRegion2.IntersectWith
cells_on_plane.IntersectWith.Normal = [0.0, 0.0, -1.0]

HideAll()


cells_on_plane_disp=Show(cells_on_plane,renderView1)
RenderAllViews()
renderView1.Update()


CreateLayout('Layout #2')
SetActiveView(None)

#Create a new SphreadSheetView
spreadSheetView1 = CreateView('SpreadSheetView')
    
 #Some default properties.
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L


# Creating another layout to show the cell data in spreadsheetview
# In layout1 the renderview will be shown.
layout2 = GetLayout()
layout2.AssignView(0, spreadSheetView1)


# Show the cell data of the cells that are intersecting with the mid 
cells_on_plane_disp_spread=Show(cells_on_plane,spreadSheetView1)


cells_on_plane_disp_spread.FieldAssociation = 'Cell Data' 
cells_on_plane_disp_spread.GenerateCellConnectivity=1

spreadSheetView1.Update()
RenderAllViews()


# Saving all the cells that intersect the mid section/plane of the sphere.
#Saving procedure
writer2 = XMLUnstructuredGridWriter(FileName="Cells_around_sphere_plane.vtu")
writer2.UpdatePipeline()
del writer2





