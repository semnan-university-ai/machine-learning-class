random=randi([1 50],[100 2]);
disp(random)
disp('_______________________________________________________________')
goal=[random(43,1),random(43,2)];
[m,fasele]=knnsearch(random,goal,'k',3 'Distance','euclidean');
for i=1:size(m,2)
      disp(random(m(1,i),:))
      disp(d(i))
      disp('_______________________________')
end
