clc; clear all; close all;

dicom_image = dicomread('image-000010.dcm');
%figure
%imshow(X,[]);

[M,I] = max(dicom_image(:));

histogram_vector=zeros(1,M);

for i = 1:length(dicom_image)
    for j = 1:length(dicom_image)
        
    end
end