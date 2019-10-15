% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% 
% Tarea 5

% clc; clear; close all;
Prefix = 'image-';
Filename = sprintf('%s%06d.dcm',Prefix,178);
% Filename = 'series-000000/image-000300.dcm';

figure(1)
A = dicomread(Filename);
I = DinamicRange(A,0,255);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
M = max(A(:));
m = min(A(:));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
MI = max(I(:));
mI = min(I(:));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
imshow(I,[]);
