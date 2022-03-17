
#tutorial and trial from abdul yt


for (int k = 1, k <= n, k++)
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            A[i,j] = min(A[i,j], A[i,k]+A[k,j])