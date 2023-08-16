function [numClust, clustInd, centInd, haloInd] = densityClust(dist, dc, rho, isHalo)
    [NE, ~] = size(dist);
    delta = zeros(1, NE); % minimum distance between each point and any other point with higher density
    indNearNeigh = Inf * ones(1, NE); % index of nearest neighbor with higher density
    
    [~, ordRho] = sort(rho, 'descend');
 
    for i = 2 : NE
        delta(ordRho(i)) = max(dist(ordRho(i), :));
        for j = 1 : (i-1)
            if dist(ordRho(i), ordRho(j)) < delta(ordRho(i))
                delta(ordRho(i)) = dist(ordRho(i), ordRho(j));
                indNearNeigh(ordRho(i)) = ordRho(j);
            end
        end
    end
    delta(ordRho(1)) = max(delta);
    indNearNeigh(ordRho(1)) = 0; % no point with higher density
    
    isManualSelect = 1; % 1 denote that all the cluster centroids are selected manually, otherwise 0
    [numClust, centInd] = decisionGraph(rho, delta, isManualSelect);
    
    clustInd = zeros(1, NE);
    for i = 1 : NE
        if centInd(ordRho(i)) == 0 % not centroid
            clustInd(ordRho(i)) = clustInd(indNearNeigh(ordRho(i)));
        else
            clustInd(ordRho(i)) = centInd(ordRho(i));
        end
    end
    
    haloInd = haloAssign(dist, clustInd, numClust, dc, rho, isHalo);
    
end

function [haloInd] = haloAssign(dist, clustInd, numClust, dc, rho, isHalo)
    [NE, ~] =size(dist);
    if isHalo == 1
        haloInd = clustInd;
        bordRho = zeros(1, numClust);
        for i = 1 : (NE - 1)
            for j = (i + 1) : NE
                if (clustInd(i) ~= clustInd(j)) && ((dist(i, j) < dc))
                    avgRho = (rho(i) + rho(j)) / 2;
                    if avgRho > bordRho(clustInd(i))
                        bordRho(clustInd(i)) = avgRho;
                    end
                    if avgRho > bordRho(clustInd(j))
                        bordRho(clustInd(j)) = avgRho;
                    end
                end
            end
        end
        for i = 1 : NE
            if rho(i) < bordRho(clustInd(i))
                haloInd(i) = 0; % 0 denotes the point is a halo
            end
        end
    else
        haloInd = zeros(1, NE); % 0 denotes no halo assignment
    end
end
