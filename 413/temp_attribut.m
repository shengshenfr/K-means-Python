close 
clear
clc
%% K=4, influence de nombre d'attributs des points
%attribut = 2
x1 = 200:200:2000;
y1 = [0.02339 0.045051 0.066458 0.089318 0.111631 0.131478 0.154275 0.175053 0.195833 0.216681];
p = polyfit(x1,y1,5);
a1 = 200:200:2000;
b1 = polyval(p,a1);

figure(1)
plot(a1,b1,'square-');
grid on
hold on

%attribut = 3
x2 = 200:200:2000;
y2 = [0.025862 0.051013 0.075444 0.102132 0.125907 0.155058 0.176705 0.199437 0.223625 0.246784];
p = polyfit(x2,y2,3);
a2 = 200:200:2000;
b2 = polyval(p,a2);

figure(1)
plot(a2,b2,'m--');

%attribut = 4
x3 = 200:200:2000;
y3 = [0.028583 0.053417 0.080197 0.105261 0.153234 0.162276 0.190809 0.225809 0.234674 0.320387];
p = polyfit(x3,y3,3);
a3 = 200:200:2000;
b3 = polyval(p,a3);

figure(1)
plot(a3,b3,'c-.');

%attribut = 5
x4 = 200:200:2000;
y4 = [0.030416 0.05905 0.088325 0.118641 0.161989 0.176624 0.204274 0.232386 0.316645 0.355062 ];
p = polyfit(x4,y4,3);
a4 = 200:200:2000;
b4 = polyval(p,a4);

figure(1)
plot(a4,b4,'r--');

%attribut = 6
x5 = 200:200:2000;
y5 = [0.033574 0.065062 0.097107 0.156676 0.161271 0.193649 0.227956 0.257521 0.288014 0.318678];
p = polyfit(x5,y5,3);
a5 = 200:200:2000;
b5 = polyval(p,a5);

figure(1)
plot(a5,b5,'<-');

%attribut = 7
x6 = 200:200:2000;
y6 = [0.036306 0.071822 0.125855 0.164638 0.178416 0.210385 0.246951 0.280784 0.319257 0.35134];
p = polyfit(x6,y6,3);
a6 = 200:200:2000;
b6 = polyval(p,a6);


figure(1)
plot(a6,b6,'hexagram-');

%attribut = 8
x7 = 200:200:2000;
y7 = [0.050242 0.077235 0.145367 0.17401 0.191311 0.233987 0.269237 0.301948 0.366709 0.379375];
p = polyfit(x7,y7,3);
a7 = 200:200:2000;
b7 = polyval(p,a7);


figure(1)
plot(a7,b7,'diamond--');





legend('\itattribut=2','\itattribut=3','\itattribut=4','\itattribut=5','\itattribut=6','\itattribut=7','\itattribut=8');

xlabel('nombre_de_points'),ylabel('time')
title('Influence de nombre d''attributs des points,K=4')