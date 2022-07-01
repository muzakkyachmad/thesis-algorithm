#creator : Achmad Muzakky (Zakky) - MSc Sanitary Engineering IHE Delft 2019

#file name : algo_fw_1 = algorithm floyd-warshall version 1
#definition : This python file is a file that contains some codes to execute the floyd-warshall algorithm of each WWTP data from a matrix data on the Excel data
#input data : An Excel file named wwtp_data and contains some sheets which represents every data of each WWTP
#mechanism : This python file will read the Excel data of each WWTP data in matrix on each sheet and execute it
#output data : This python file will release the matrix of the shortest path of every simulation in excel file

#######################################################################################################################
#this code below is to import package to execute the shortest path finder algorithm - floyd warshall
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


#######################################################################################################################
#to execute the floyd warshall of 27 WWTP - technology is not considered from decentralised scenario

df1=pd.read_excel('wwtp_data.xlsx', sheet_name='27dmatrix',index_col=0)

matrix=csr_matrix(df1.values)

dist_matrix1 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df1[:] = dist_matrix1

df1.to_excel("spf_results_27d.xlsx", sheet_name="27d_matrix")


#######################################################################################################################
#to execute the floyd warshall of 7 WWTP - technology is not considered from semi-decentralised scenario

df2=pd.read_excel('wwtp_data.xlsx', sheet_name='7sdmatrix',index_col=0)

matrix=csr_matrix(df2.values)

dist_matrix2 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df2[:] = dist_matrix2

df2.to_excel("spf_results_7sd.xlsx", sheet_name="7sd_matrix")


#######################################################################################################################
#to execute the floyd warshall of 4 WWTP - technology is CAS from semi-decentralised scenario

df3=pd.read_excel('wwtp_data.xlsx', sheet_name='4sdcasmatrix',index_col=0)

matrix=csr_matrix(df3.values)

dist_matrix3 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df3[:] = dist_matrix3

df3.to_excel("spf_results_4sd_cas.xlsx", sheet_name="4sd_cas_matrix")


#######################################################################################################################
#to execute the floyd warshall of 3 WWTP - technology is MBR from semi-decentralised scenario

df4=pd.read_excel('wwtp_data.xlsx', sheet_name='3sdmbrmatrix',index_col=0)

matrix=csr_matrix(df4.values)

dist_matrix4 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df4[:] = dist_matrix4

df4.to_excel("spf_results_3sd_mbr.xlsx", sheet_name="3sd_mbr_matrix")


#######################################################################################################################
#to execute the floyd warshall of 12 WWTP - technology is CAS from decentralised scenario

df5=pd.read_excel('wwtp_data.xlsx', sheet_name='12dcasmatrix',index_col=0)

matrix=csr_matrix(df5.values)

dist_matrix5 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df5[:] = dist_matrix5

df5.to_excel("spf_results_12d_cas.xlsx", sheet_name="12d_cas_matrix")


#######################################################################################################################
#to execute the floyd warshall of 15 WWTP - technology is MBR from decentralised scenario

df6=pd.read_excel('wwtp_data.xlsx', sheet_name='15dmbrmatrix',index_col=0)

matrix=csr_matrix(df6.values)

dist_matrix6 = floyd_warshall(csgraph=matrix, directed=False, return_predecessors=False)

df6[:] = dist_matrix6

df6.to_excel("spf_results_15d_mbr.xlsx", sheet_name="15d_mbr_matrix")

###################### this is the end line of the algo_fw_1 python file###############################################
