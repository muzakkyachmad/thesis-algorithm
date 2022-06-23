#this file is to execute the spf algorithm of each wwtp data

#######################################################################################################################
#this code below is to import package to execute the shortest path finder algorithm - floyd warshall
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

#######################################################################################################################
#to execute the floyd warshall of 7 WWTP - technology is not considered from semi-decentralised scenario

df=pd.read_excel('wwtp_data.xlsx', sheet_name='7sdmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("floyd_warshall_results.xlsx", sheet_name="7sd_result") #Publishes results to excel


#######################################################################################################################
#to execute the floyd warshall of 4 WWTP - technology is CAS from semi-decentralised scenario with 7 WWTP in total

df=pd.read_excel('wwtp_data.xlsx', sheet_name='4sdcasmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("floyd_warshall_results.xlsx", sheet_name="4sd_cas_result") #Publishes results to excel


#######################################################################################################################
#to execute the floyd warshall of 3 WWTP - technology is MBR from semi-decentralised scenario with 7 WWTP in total

df=pd.read_excel('wwtp_data.xlsx', sheet_name='3sdmbrmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("floyd_warshall_results.xlsx", sheet_name="3sd_mbr_result") #Publishes results to excel


#######################################################################################################################
#to execute the floyd warshall of 27 WWTP - technology is not considered from decentralised scenario

df=pd.read_excel('wwtp_data.xlsx', sheet_name='27dmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("floyd_warshall_results.xlsx", sheet_name="27d_result") #Publishes results to excel


#######################################################################################################################
#to execute the floyd warshall of 12 WWTP - technology is CAS from decentralised scenario

df=pd.read_excel('wwtp_data.xlsx', sheet_name='12dcasmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("floyd_warshall_results.xlsx", sheet_name="12d_cas_result") #Publishes results to excel


#######################################################################################################################
#to execute the floyd warshall of 15 WWTP - technology is MBR from decentralised scenario

df=pd.read_excel('wwtp_data.xlsx', sheet_name='15dmbrmatrix',index_col=0) #creates DataFrame by reading excel file

matrix=csr_matrix(df.values) #Converts DataFrame to csr_matrix

dist_matrix = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False) #In-built implementation of the floyd-warshall algorithm by scipy

df[:] = dist_matrix #Replaces the DataFrame with the shortest path matrix

df.to_excel("floyd_warshall_results.xlsx", sheet_name="15d_mbr_result") #Publishes results to excel