close 
clear
clc
%% influence du nombre de points, k=4, attribut = 2

x1 = 200:200:2000;
y1 = [0.015389 0.028128 0.041475 0.054078 0.068477 0.078078 0.091376 0.106436 0.118654 0.131741];
p = polyfit(x1,y1,4);
a1 = 200:200:2000;
b1 = polyval(p,a1);


figure(1)
plot(a1,b1,'*-');
grid on


legend('\itnombre de points');

xlabel('nombre_de_points'),ylabel('time')
title('influence du nombre de points, k=4, attribut=2')