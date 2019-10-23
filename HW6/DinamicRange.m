function O = DinamicRange(I,A,B)
    [m,n]=size(I);
    O=zeros(m,n);
    slope = 255/double(B-A);
    Interceptor = -slope*A;
    
    for i=1:m
        for j=1:n
            V=double(I(i,j));
            if (V>=A && V<=B)
                NV=round((slope*V)+Interceptor);
            elseif (V>B)
                NV=0;
            else
                NV=0;
            end
            O(i,j)=NV;
        end
    end
    
end
