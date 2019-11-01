function CalculadoraDerivadaImagen(I)
    dIdj = circshift(I,[0, -1])-I;
    dIdi = circshift(I,[-1, 0])-I;
    mag = sqrt(