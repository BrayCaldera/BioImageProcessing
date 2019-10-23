% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% 
% Tarea 6
%% MAIN CODE
tic

V = BuildMedicalVolume('series-000000/image-',0:360);

% ShowCrossSection(V,1,false) % Show Axial Axis
% ShowCrossSection(V,3,false) % Show Coronal Axis
ShowCrossSection(V,2,false) % Show Sagital Axis

toc