
intialize d[v][o] = infinity for v !=t. d[t][i]=0 for all i
for i=1 to n-1:
    for each v !=t:
        d[v][i] = min (len(v,x) + d[x][i-1])
for each v, output d[v][n-1].