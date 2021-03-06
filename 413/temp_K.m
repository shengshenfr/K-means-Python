close 
clear
clc
%% attrbut = 2, influence sur le nombre de K
%K=2
x1 = 200:200:2000;
y1 = [0.011232 0.019627 0.028521 0.03728 0.04832 0.055526 0.064093 0.074792 0.080475 0.089315];
p = polyfit(x1,y1,5);
a1 = 200:200:2000;
b1 = polyval(p,a1);

figure(1)
plot(a1,b1,'square-');
grid on
hold on

%K = 3
x2 = 200:200:2000;
y2 = [0.013108 0.023809 0.035607 0.045333 0.056686 0.067058 0.078307 0.088123 0.098163 0.109994];
p = polyfit(x2,y2,3);
a2 = 200:200:2000;
b2 = polyval(p,a2);

figure(1)
plot(a2,b2,'m--');

%K = 4
x3 = 200:200:2000;
y3 = [0.015389 0.028128 0.041475 0.054078 0.068477 0.078078 0.091376 0.106436 0.118654 0.131741];
p = polyfit(x3,y3,3);
a3 = 200:200:2000;
b3 = polyval(p,a3);

figure(1)
plot(a3,b3,'c-.');

%K = 5
x4 = 200:200:2000;
y4 = [0.017502 0.032784 0.046682 0.060991 0.076926 0.091489 0.107486 0.120647 0.136479 0.150868 ];
p = polyfit(x4,y4,3);
a4 = 200:200:2000;
b4 = polyval(p,a4);

figure(1)
plot(a4,b4,'r--');

%K = 6
x5 = 200:200:2000;
y5 = [0.018939 0.036078 0.053331 0.069354 0.08646 0.103232 0.12014 0.137161 0.153468 0.172252];
p = polyfit(x5,y5,3);
a5 = 200:200:2000;
b5 = polyval(p,a5);

figure(1)
plot(a5,b5,'g-');

%K = 7
x6 = 200:200:2000;
y6 = [0.021052 0.039687 0.059026 0.077382 0.095219 0.11648 0.133387 0.157159 0.175042 0.190867];
p = polyfit(x6,y6,3);
a6 = 200:200:2000;
b6 = polyval(p,a6);


figure(1)
plot(a6,b6,'b-');

%K = 8
x7 = 200:200:2000;
y7 = [0.02331 0.044469 0.066469 0.085985 0.105384 0.127174 0.149376 0.170583 0.190736 0.214313];
p = polyfit(x7,y7,3);
a7 = 200:200:2000;
b7 = polyval(p,a7);


figure(1)
plot(a7,b7,'diamond--');





legend('\itK=2','\itK=3','\itK=4','\itK=5','\itK=6','\itK=7','\itK=8');

xlabel('nombre_de_points'),ylabel('time')
title('Influence de nombre K,attrbut = 2')