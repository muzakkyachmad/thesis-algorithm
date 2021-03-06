
#Import the packages that you need

import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

df=pd.read_excel('wwtpdatafinal.xlsx', sheet_name='7sdmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("SPF_Results_7sd.xlsx", sheet_name="spf_7sd") #Publishes results to excel