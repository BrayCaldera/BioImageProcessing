% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% Histograma de una imagen DICOM
% Tarea 4

clc; clear all; close all;

tic

dicom_image = dicomread('image-000010.dcm');
figure
imshow(dicom_image,[]); % Mostrar imagen DICOM
[M,I] = max(dicom_image(:));
histogram_vector=zeros(1,M+1);
rango_vector = linspace(0,double(M),double(M)+1);

for i = 1:length(dicom_image) % Pixelwise operation
    for j = 1:length(dicom_image)
        V=double(dicom_image(i,j));
        histogram_vector(V+1)=histogram_vector(V+1)+1;
    end
end

figure % Figura que muestra el histograma completo
bar(rango_vector,histogram_vector) % Plotear en modo barra
title('Histograma de una imagen DICOM') % Título
xlabel('Posición') % Etiqueta del eje x
ylabel('Cantidad') % Etiqueta del eje y

figure % Figura que muestra sin los valores 0 y 1
bar(rango_vector(3:end),histogram_vector(3:end)) % Potear en modo barra
title('Histograma de una imagen DICOM (sin los valores 0 y 1)') % Título
xlabel('Posición') % Etiqueta del eje x
ylabel('Cantidad') % Etiqueta del eje y

toc