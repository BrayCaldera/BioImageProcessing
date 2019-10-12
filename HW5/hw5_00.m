% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% 
% Tarea 5

% clc; clear; close all;

Filename = 'series-000000/image-000000.dcm';

figure(1)
for i=1:100
   % Filename = sprintf('%s%d.dcm',Prefix,i);
    % Filename = (Prefix);
   if exist(Filename, 'file') == 1
       I = dicomread(Filename);
       I = DinamicRange(I,0,500);
       imshow((I),[100 1000]);
       drawnow
       disp(i);
       %pause
   end
end