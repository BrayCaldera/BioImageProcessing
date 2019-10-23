% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% 
% Tarea 5
%% MAIN CODE

% Notes:
% INTENSITY_COEF=0.11353517; % 255/max(value of a particular set of DICOM)

ShowDicomSeries('series-000000/image-',178, 0, 255) % All

% ShowDicomSeries('series-000000/image-',0:360, 0, 255) % All
% ShowDicomSeries('series-000000/image-',0:360, 110, 132) % Kidneys %All pictures
% ShowDicomSeries('series-000000/image-',178, 122, 126) % Kidneys %One picture
                                        %1)  %2)  %3)
 % 1) To select which image you want to see (you can select a range)
 % 2) The lower coeficient of intensity
 % 3) The higher coeficient of intensity
 
% ShowDicomSeries('series-000000/image-',0:360, 135, 138) % Bones
% ShowDicomSeries('series-000000/image-',50, 135, 148) % Bones %One picture

% ShowDicomSeries('series-000000/image-',0:360, 101, 147) % Spleen
% ShowDicomSeries('series-000000/image-',1, 122, 127) % Spleen %One picture
