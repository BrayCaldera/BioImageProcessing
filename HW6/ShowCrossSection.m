%This is a funcion.......
%Inputs:
%V=medical volume to get the cross sections
%PlaneOrientationOption:
% 1 - Axial
% 2 - Sagital
% 3 - Coronal

function ShowCrossSection(V,PlaneOrientationOption,PausedByUser)
if(PlaneOrientationOption<1 || PlaneOrientationOption>3)
    disp('You must ose 1, 2 or 3 as PlaneOrientationOption')
    return;
end

[m,n,NSlides]=size(V);

if(PlaneOrientationOption==1)
    Limit=NSlides;
elseif(PlaneOrientationOption==2)
    Limit=n;
elseif(PlaneOrientationOption==3)
    Limit=m;
end

figure(1)

for k=1:Limit
    if(PlaneOrientationOption==1)
        I=V(:,:,k);
    elseif(PlaneOrientationOption==2)
        I=V(:,k,:);
        I=reshape(I,m,NSlides);
        % I=imresize(I,[m,NSlides*3]);
        I=imresize(I,[m,NSlides]);
        I=imrotate(I,-90);
    elseif(PlaneOrientationOption==3)
        I=V(k,:,:);
        I=reshape(I,n,NSlides);
        I=imrotate(I,-90);
    end
    imshow((I),[1000 2000]);
    drawnow
    if(PausedByUser==1)
        pause;
    end
end
