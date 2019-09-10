"""Program to load DICOM Files"""

import os
import pydicom

filename = 'series-000000/image-000000.dcm'
ds = pydicom.dcmread(filename)
print(ds.PixelData)
if ds:
    print('Se cargó')