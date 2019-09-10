"""Program to load and plot DICOM Files"""

import matplotlib.pyplot as plt
import pydicom

def load_dcm(filename):
    dataset = pydicom.dcmread(filename)
    return dataset

def print_dataset_details(filename,dataset):
    print()
    print("Filename.........:", filename)
    print("Storage type.....:", dataset.SOPClassUID)
    print()

    pat_name = dataset.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    print("Patient's name...:", display_name)
    print("Patient id.......:", dataset.PatientID)
    print("Modality.........:", dataset.Modality)
    #print("Study Date.......:", dataset.StudyDate)

    if 'PixelData' in dataset:
        rows = int(dataset.Rows)
        cols = int(dataset.Columns)
        print("Image size.......: {rows:d} x {cols:d}, {size:d} bytes".format(
            rows=rows, cols=cols, size=len(dataset.PixelData)))
    if 'PixelSpacing' in dataset:
        print("Pixel spacing....:", dataset.PixelSpacing)

    # use .get() if not sure the item exists, and want a default value if missing
    print("Slice location...:", dataset.get('SliceLocation', "(missing)"))

def plot_dcm_image(dataset):
    # plot the image using matplotlib
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()


if __name__=='__main__':
    filename = 'Anonymized20190910.dcm'
    dataset = load_dcm(filename)
    print_dataset_details(filename,dataset)
    plot_dcm_image(dataset)
