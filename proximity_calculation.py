import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import pdist, squareform

csvFile = pd.read_csv('data.csv')

df = csvFile.select_dtypes(include=['number'])

#euclidean distance
dist_matrix = squareform(pdist(df, metric='euclidean'))
dist_df = pd.DataFrame(dist_matrix, columns=df.index, index=df.index)

#cosine similarity
sim_matrix = cosine_similarity(df)
sim_matrix_df = pd.DataFrame(sim_matrix, columns=df.index, index=df.index)

#correlation 
instance_corr_matrix = df.T.corr()
instance_corr_matrix_df = pd.DataFrame(instance_corr_matrix, columns=df.index, index=df.index)

df.to_csv('numerical_data.csv', index=False)
dist_df.to_csv('euclidean_dist.csv', index=True)  
sim_matrix_df.to_csv('cosine_similarity.csv', index=True)  
instance_corr_matrix_df.to_csv('correlation.csv', index=True)  
