% Brayan Daniel Caldera Rosas
% Procesamiento de Bioimágenes
% 
% Tarea 6
%% MAIN CODE
%% BUILD
tic
V = BuildMedicalVolume('series-000000/image-',0:360);
% V1 = BuildMedicalVolume('series-000000/image-',178:180);
toc
%% SHOW
tic

%ShowCrossSection(V,1,false,968,1160) % Show Liver axial
%ShowCrossSection(V,2,false,968,1160) % Show Liver Sagital
%ShowCrossSection(V,3,false,968,1160) % Show Liver Coronal

%ShowCrossSection(V,1,false,1000,1200) % Show Kidneys axial
%ShowCrossSection(V,2,false,1000,1200) % Show Kidneys Sagital
%ShowCrossSection(V,3,false,1000,1200) % Show Kidneys Coronal

%ShowCrossSection(V,1,false,968,1160) % Show small intestine axial
%ShowCrossSection(V,2,false,968,1160) % Show small intestine Sagital
%ShowCrossSection(V,3,false,900,1200) % Show small intestine Coronal

toc