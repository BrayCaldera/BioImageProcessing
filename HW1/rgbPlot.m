function [] = rgbPlot(ImgName)

figure

% Loading Image
Img = imread(ImgName);
subplot(2,3,1:3)
imshow(Img); title('Original Image');

% Image Asignation
Red = Img;
Blue = Img;
Green = Img;

%% RGB

% Red Channel
Red(:,:,2) = 0;
Red(:,:,3) = 0;
subplot(234)
imshow(Red); title('Channel Red')

% Blue Channel
Blue(:,:,1) = 0;
Blue(:,:,3) = 0;
subplot(235)
imshow(Blue); title('Channel Blue')

% Green Channel
Green(:,:,1) = 0;
Green(:,:,2) = 0;
subplot(236)
imshow(Green); title('Channel Green')
end