clear
close all;
clc;

aa = load('3D_data\G100\G100_3D_0031_CenStrong.txt');
xy = [aa(:,1) , aa(:,2) , aa(:,3) ];
X = xy;
xy = floor(xy);
% A1= zeros(size(data));
% for ii = 1:size(xy,1)
    % A1(xy(ii,2)+1,xy(ii,1)+1,xy(ii,3)+1) = data(xy(ii,2)+1,xy(ii,1)+1,xy(ii,3)+1);
% end

figure(1);
plot3(X(:, 1), X(:, 2), X(:, 3), 'b.');
xlabel('Dim 1');
ylabel('Dim 2');
zlabel('Dim 3');
title('Original Data Set');

%% Settings of System Parameters for DensityClust
dist = pdist2(X, X); % [NE, NE] matrix (this case may be not suitable for large-scale data sets)
% average percentage of neighbours, ranging from [0, 1]
% as a rule of thumb, set to around 1%-2% of NE (see the corresponding *Science* paper for more details)
percNeigh = 0.02;
% 'Gauss' denotes the use of Gauss Kernel to compute rho, and
% 'Cut-off' denotes the use of Cut-off Kernel.
% For large-scale data sets, 'Cut-off' is preferable owing to computational efficiency,
% otherwise, 'Gauss' is preferable in the case of small samples (especially with noises).
%kernel = 'Cut-off';
% set critical system parameters for DensityClust

dc = 3;
rho = [aa(:,4)];

%[dc, rho] = paraSet(dist, percNeigh, kernel, dc);     %rho的读取

figure(2);
plot(rho, 'b*');
xlabel('ALL Data Points');
ylabel('\rho');
title('Distribution Plot of \rho');

%% Density Clustering
isHalo = 1; 
[numClust, clustInd, centInd, haloInd] = densityClust(dist, dc, rho, isHalo);
save('densityClust.mat', 'numClust', 'clustInd', 'centInd', 'haloInd');
figure(3);
bb = load('data_f1\ppt\Real_data\new\0031_realcen.txt');
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
