close 
clear
clc

x = [48.1,47,54.9]
figure(1)

bar(x)
text(0.5,52,'\itIris Setosa 48.1');
text(1.5,52,'\itIris Versicolour 47');
text(2.5,58,'\itIris Virginica 54.9');
axis([0 4 0 70])
grid on
xlabel('type'),ylabel('nombre')
title('nombre de chaque classe')