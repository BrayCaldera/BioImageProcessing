% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% 
% Tarea 6
%% EXAMPLE CODE

% Notes:
% INTENSITY_COEF=0.11353517; % 255/max(value of a particular set of DICOM)

% ShowDicomSeries('series-000000/image-',178, 0, 255) % Just One

% ShowDicomSeries('series-000000/image-',0:360, 0, 255) % All

%--------------------------------------------------------------------------
%% MAIN CODE
% tic
V = BuildMedicalVolume('series-000000/image-',0:360);
% toc
%%
tic
% ShowCrossSection(V,3,0) % Show Coronal Axis
ShowCrossSection(V,2,0) % Show Sagital Axis

toc