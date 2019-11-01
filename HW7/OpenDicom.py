"""
Created on Tue Mar 26 09:23:39 2019

@author: germen

Modified on Fri Nov 01 07:37:15 2019
by: DanCaldera

For Python3.x
"""

import os
import pydicom
from pydicom.data import get_testdata_files
import cv2
#import Tkinter, tkFileDialog
import tkinter
from tkinter import filedialog
import glob
from numpy import random,genfromtxt,size
import numpy as np
import vtk



class VtkPointCloud:
    def __init__(self, zMin=0, zMax=300.0, maxNumPoints=1e6):
        self.maxNumPoints = maxNumPoints
        self.vtkPolyData = vtk.vtkPolyData()
        self.clearPoints()
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.vtkPolyData)
        mapper.SetColorModeToDefault()
        mapper.SetScalarRange(zMin, zMax)
        mapper.SetScalarVisibility(1)
        self.vtkActor = vtk.vtkActor()
        self.vtkActor.SetMapper(mapper)
 
    def addPoint(self, point):
        if self.vtkPoints.GetNumberOfPoints() < self.maxNumPoints:
            pointId = self.vtkPoints.InsertNextPoint(point[:])
            self.vtkDepth.InsertNextValue(point[2])
            self.vtkCells.InsertNextCell(1)
            self.vtkCells.InsertCellPoint(pointId)
        else:
            r = random.randint(0, self.maxNumPoints)
            self.vtkPoints.SetPoint(r, point[:])
        self.vtkCells.Modified()
        self.vtkPoints.Modified()
        self.vtkDepth.Modified()
 
    def clearPoints(self):
        self.vtkPoints = vtk.vtkPoints()
        self.vtkCells = vtk.vtkCellArray()
        self.vtkDepth = vtk.vtkDoubleArray()
        self.vtkDepth.SetName('DepthArray')
        self.vtkPolyData.SetPoints(self.vtkPoints)
        self.vtkPolyData.SetVerts(self.vtkCells)
        self.vtkPolyData.GetPointData().SetScalars(self.vtkDepth)
        self.vtkPolyData.GetPointData().SetActiveScalars('DepthArray')


root = tkinter.Tk()
root.withdraw()
dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
mylist = [f for f in glob.glob(dirname + "/*.dcm")]
mylist.sort()
NFiles=np.array(mylist).shape

pointCloud = VtkPointCloud()

# import pdb; pdb.set_trace()

CurrentFileToOpen=0
while CurrentFileToOpen<NFiles[0]:
    ds = pydicom.dcmread(mylist[CurrentFileToOpen])  # plan dataset
    ImageData = np.array(ds.pixel_array, dtype=float)
    SegmetnedSkull = cv2.inRange(ImageData, 240, 250)

    indices = np.where(SegmetnedSkull != [0])
    coordinates = list(zip(indices[0], indices[1]))
    myarray = np.asarray(coordinates)
    #print coordinates[0]
    for k in range(len(coordinates)):
        point = [myarray[k,0], myarray[k,1], CurrentFileToOpen*1.4]
        #print point
        pointCloud.addPoint(point)
   
    import pdb; pdb.set_trace()
    dcm_sample=SegmetnedSkull#(ImageData/np.max(ImageData))
    cv2.imshow('sample image dicom',dcm_sample)
    cv2.waitKey(1);
    CurrentFileToOpen=CurrentFileToOpen+1;
    
    
cv2.destroyAllWindows()
cv2.waitKey(1)


# Renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(pointCloud.vtkActor)
#renderer.SetBackground(.2, .3, .4)
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.ResetCamera()
 
# Render Window
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
 
# Interactor
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
 
# Begin Interaction
renderWindow.Render()
renderWindow.SetWindowName("XYZ Data Viewer")
renderWindowInteractor.Start()