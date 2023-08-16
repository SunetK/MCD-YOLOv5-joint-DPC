function [dc, rho] = paraSet(dist, percNeigh, kernel, dc)
    
    distRow = squareform(dist, 'tovector');
    sortDistRow = sort(distRow);
    [NE, ~] = size(dist);
 
    if strcmp(kernel, 'Gauss')
        rho = sum(exp(-(dist/dc).^2) , 1) - exp(-(0/dc).^2); % local density estimation using Guass Kernel
    elseif strcmp(kernel, 'Cut-off')
        rho = sum(dist < dc, 1) - 1; % the number of points that are closer than dc to point i
    else
        % NO NOTHING, just for further work ...
    end

end     
