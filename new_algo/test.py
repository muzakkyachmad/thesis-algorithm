#to execute the floyd warshall of 7 WWTP - technology is not considered from semi-decentralised scenario
#this code below is to import package to execute the shortest path finder algorithm - floyd warshall
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

df2=pd.read_excel('wwtp_data.xlsx', sheet_name='7sdmatrix',index_col=0)

matrix=csr_matrix(df2.values)

dist_matrix2 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df2[:] = dist_matrix2

df2.to_excel("spf_results_7sd.xlsx", sheet_name="7sd_matrix")

