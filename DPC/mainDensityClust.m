clear
close all;
clc;

aa = load('3D_data\G100\G100_3D_0099_CenStrong.txt');
xy = [aa(:,1) , aa(:,2) , aa(:,3) ];
X = xy;
xy = floor(xy);

figure(1);
plot3(X(:, 1), X(:, 2), X(:, 3), 'b.');
xlabel('Dim 1');
ylabel('Dim 2');
zlabel('Dim 3');
title('Original Data Set');

dc = 3;
rho = [aa(:,4)];

figure(2);
plot(rho, 'b*');
xlabel('ALL Data Points');
ylabel('\rho');
title('Distribution Plot of \rho');

isHalo = 1; 
[numClust, clustInd, centInd, haloInd] = densityClust(dist, dc, rho, isHalo);
save('densityClust.mat', 'numClust', 'clustInd', 'centInd', 'haloInd');
figure(3);
bb = load('Real_data\G100\0099_realcen.txt');
cen = [bb(:,1) , bb(:,2) , bb(:,3)];
CEN = cen;
cmap = colormap;
for ii = 1:numClust
    plot3(X(clustInd == ii, 1), X(clustInd == ii, 2),X(clustInd == ii, 3), 'o', 'MarkerSize', 2, 'MarkerFaceColor', cmap(ii,:));   %%改动  plot3(X(clustInd == ii, 1), X(clustInd == ii, 2),X(clustInd == ii, 3), 'r.', 'MarkerEdgeColor',cmap(ii,:));
    plot3(X(centInd == ii, 1), X(centInd == ii, 2),X(centInd == ii, 3), 'bd', 'MarkerSize', 5, 'MarkerFaceColor', 'r');
    plot3(CEN(:, 1), CEN(:, 2), CEN(:, 3), 's', 'MarkerSize', 5, 'MarkerFaceColor', 'g');
    hold on;   
end
xlabel('x');
ylabel('y');
zlabel('v');
title('DensityClust for Centroid of Clump');
