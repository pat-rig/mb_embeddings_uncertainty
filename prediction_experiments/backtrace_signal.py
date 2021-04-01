"""
    WHY ARE ASVs WITH MOST SIGNAL FOR RAW DATA NOT IMPORTANT FOR PCA?
    
    import os
    os.chdir('/Users/patrick/Drive/13_sem/research_project/TEMP/prediction_experiments')
"""
import pickle
import pandas as pd

# load tables of most important asvs
with open('imp_asv_tables.obj', mode='rb') as table_file:
    tables = pickle.load(table_file)
    table_file.close()
    
<<<<<<< HEAD
    # Only execute on machine with large memory
# =============================================================================
# # only execute on large memory machine (file requires ~1GB)
# # load abundance data 
# # abundance_data = pd.read_csv('../data/seqtab_filter.07.txt', delim='\t', index_col=0)
# 
# # pick asvs to inspect
# sign_asvs_raw = tables['sign_asvs']['raw']
# sign_asvs_pca = tables['sign_asvs']['pca']
# 
# # extract and save abundance vectors
# sign_abundances = {'pca': abundance_data.loc[:, sign_asvs_pca],
#                    'raw': abundance_data.loc[:, sign_asvs_raw]}
# 
# with open('sign_abundances.obj', mode='wb') as abundance_file:
#     pickle.dump(sign_abundances, abundance_file)
#     abundance_file.close()
#     
# =============================================================================
    # if on local machine: collect abundances
=======
# only execute on large memory machine (file requires ~1GB)
# load abundance data 
abundance_data = pd.read_csv('../data/seqtab_filter.07.txt', sep='\t', index_col=0)
>>>>>>> df70e0dd81a0b6928037872bcc13cd7c3b8d34ba


with open('sign_abundances.obj', mode='rb') as abundance_file:
    sign_abundances = pickle.load(abundance_file)
    abundance_file.close()
<<<<<<< HEAD

# first look compute variances per column
raw_variances = sign_abundances['raw'].var(axis=0).values
pca_variances = sign_abundances['pca'].var(axis=0).values    

    
=======
    
    
>>>>>>> df70e0dd81a0b6928037872bcc13cd7c3b8d34ba
