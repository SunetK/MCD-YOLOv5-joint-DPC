function [numClust, centInd] = decisionGraph(rho, delta, isManualSelect)
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
