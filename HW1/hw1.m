%//////////////////////////////////////////////////////////////////////////
%//                                                                      //
%//                   Homework No.1 - RGB descomposition                 //
%//                          Bioimage Processing                         //
%//                       Brayan Daniel Caldera Rosas                    //
%//                                                                      //
%//////////////////////////////////////////////////////////////////////////

% Cleaning
clc;
clear all;
close all;

rgbPlot('example1.jpg')
saveas(gcf,'ex1.png')
rgbPlot('example2.jpg')
saveas(gcf,'ex2.png')
rgbPlot('example3.png')
saveas(gcf,'ex3.png')