function V=BuildMedicalVolume(Prefix,DataNumberRange)
figure(1)
k=1;
for i=DataNumberRange
    FileName = sprintf('%s%06d.dcm',Prefix,i);
    if exist(FileName, 'file') == 2
        I=dicomread(FileName);
        
        %I=DinamicRange(I,0,3000);
        V(:,:,k)=I;
        k=k+1;
    end
end