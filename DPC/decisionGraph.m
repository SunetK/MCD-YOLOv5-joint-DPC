function [numClust, centInd] = decisionGraph(rho, delta, isManualSelect)
%%DECISIONGRAPH Decision graph for choosing the cluster centroids.
%   INPUT:
%       rho: local density [row vector]
%       delta: minimum distance between each point and any other point with higher density [row vector]
%       isManualSelect: 1 denote that all the cluster centroids are selected manually, otherwise 0
%  OUTPUT:
%       numClust: number of clusters
%       centInd:  centroid index vector

    NE = length(rho);
    numClust = 0;
    centInd = zeros(1, NE);
    Rms=0.23;
    if isManualSelect == 1
        
        fprintf('Manually select a proper rectangle to determine all the cluster centres (use Decision Graph)!\n');
        fprintf('The only points of relatively high *rho* and high  *delta* are the cluster centers!\n');
        plot(rho, delta, 's', 'MarkerSize', 7, 'MarkerFaceColor', 'r', 'MarkerEdgeColor', 'b');
        title('Decision Graph', 'FontSize', 17);
        xlabel('\rho');
        ylabel('\delta');
        
        % rectangle = getrect(fig);
        minRho = 5*Rms;    % 3--5  rms     rms=0.23  real data
        minDelta = 4;   % 3--6
        
        for i = 1 : NE
            if (rho(i) > minRho) && (delta(i) > minDelta)
                numClust = numClust + 1;
                centInd(i) = numClust;
            end
        end
        
    else
        % DO NOTHING, just for futher work ...
    end

end