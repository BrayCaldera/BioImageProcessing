function I = ShowDicomSeries(Prefix, DataNumberRange, rangeInf, rangeSup)
   figure(1)
   for i=DataNumberRange
       Filename = sprintf('%s%06d.dcm',Prefix,i);
       % Filename = (Prefix);
       if exist(Filename, 'file') == 2
           I = dicomread(Filename);
           
           I = DinamicRange(I,0,max(I(:)));
           imshow((I),[rangeInf rangeSup]);
           drawnow
           disp(i);
           %pause
       end
   end
end