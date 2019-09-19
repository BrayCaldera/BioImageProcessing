% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% Histograma de una imagen DICOM
% Tarea 4

clc; clear all; close all;

dicom_image = dicomread('image-000010.dcm');
figure
imshow(dicom_image,[]);

[M,I] = max(dicom_image(:));

histogram_vector=zeros(1,M+1);
rango_vector = linspace(0,double(M),double(M)+1);

for i = 1:length(dicom_image)
    for j = 1:length(dicom_image)
        pixel = dicom_image(i,j);
        for x = 1:length(rango_vector)
            if (pixel==rango_vector(x))
               histogram_vector(x)=histogram_vector(x)+1; 
            end
        end
    end
end

figure
bar(rango_vector,histogram_vector)
title('Histograma de una imagen DICOM')
xlabel('Posición')
ylabel('Cantidad')

figure
bar(rango_vector(3:end),histogram_vector(3:end))
title('Histograma de una imagen DICOM (sin los valores 0 y 1)')
xlabel('Posición')
ylabel('Cantidad')
