function a = ShowDicomSeries(Prefix, DataNumberRange)
   figure(1)
   for i=DataNumberRange
       % Filename = sprintf('%s%d.dcm',Prefix,i);
       Filename = (Prefix);
       if exist(Filename, 'file') == 0
           I = dicomread(Filename);
           I = DinamicRange(I,0,500);
           imshow((I),[100 1000]);
           drawnow
           disp(i);
           %pause
       end
   end
end