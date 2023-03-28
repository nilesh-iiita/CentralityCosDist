#!/usr/bin/env python
# coding: utf-8

__author__ = "\x1b[0;5;37;40m Nilesh Kumar \x1b[0;1;30;47m"
__copyright__ = "Copyright 2023, UAB"
__credits__ = ["Nilesh Kumar"]
__license__ = "GPL"
__version__ = "0.1.1"
__maintainer__ = "Nilesh Kumar"
__email__ = "nilesh.iiita@gmail.com"
__status__ = "Production"

from collections import defaultdict
import numpy as np
import networkx as nx
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity
from glob import glob
from collections import defaultdict

class CentralityCosDist:
    __author__ = "\x1b[0;5;37;40m Nilesh Kumar \x1b[0;1;30;47m"
    __copyright__ = "Copyright 2023, UAB"
    __credits__ = ["Nilesh Kumar"]
    __license__ = "GPL"
    __version__ = "0.1.1"
    __maintainer__ = "Nilesh Kumar"
    __email__ = "nilesh.iiita@gmail.com"
    __status__ = "Production"

    algorithm_name = 'CentralityCosDist'
    
    def Cosine_similarity(self, method = "cosine"):
        #return Centrality_df
        features = self.seed_nodes
        # print(features)
        Centrality_df = self.Centralites
        #print(self.Centralites, self.seed_nodes)
    
        Centrality_df = Centrality_df.fillna(0)
        #Select rows for seed gene(s)
        Seed_df = Centrality_df.loc[features]

        seed_ndarr = np.array(Seed_df)
        Centrality_ndarr = np.array(Centrality_df)
        

        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html
        # Distance = distance.cdist(Centrality_ndarr, seed_ndarr, self.similarity_method)
        Distance = cosine_similarity(Centrality_ndarr)
        #print(distance.cdist(seed_ndarr, Centrality_ndarr, "cosine"))
        # print(Distance)
        # df = pd.DataFrame(Distance, columns = Seed_df.index, index = Centrality_df.index)
        df = pd.DataFrame(Distance, columns = Centrality_df.index, index = Centrality_df.index)
        # print(df)
        # self.Test = df
        
        df = df[df.index.isin(features)][features]

        df = df[df.index.tolist()]
        LOL = df.values.tolist()

        Dic = defaultdict(list)

        for i in range(len(LOL)):
            for j in range(len(LOL)):
                if LOL[i][j] > 0.90:
                    Dic[i].append((features[j],LOL[i][j]))
                    # print(i, j, LOL[i][j])
        Biggest_grp = 0
        for i in Dic:
            if len(Dic[Biggest_grp]) < len(Dic[i]):
                Biggest_grp = i
        close_related_seeds = set([i[0] for i in Dic[Biggest_grp]])
        ##############################################################
        Seed_df = Centrality_df.loc[list(close_related_seeds)]

        seed_ndarr = np.array(Seed_df)
        ##############################################################
        Distance = cosine_similarity(Centrality_ndarr, seed_ndarr)
        df = pd.DataFrame(Distance, columns = Seed_df.index, index = Centrality_df.index)
        

        df_avg = df.copy()
        df_avg['_Average_distance'] = df_avg.mean(numeric_only=True, axis=1) ## Similarity score
        df_avg['Rank'] = 1-df_avg['_Average_distance'] # 1-Distance
        df_avg.sort_values(by='_Average_distance', ascending=True, inplace=True)
        df_avg['_Rank'] = df_avg['Rank'].rank()
        df_avg['_Max_rank'] = df_avg['_Average_distance'].rank(method='max')
        #df_avg['NA_bottom'] = df_avg['Average_distance'].rank(na_option='bottom')
        df_avg['_Percentile_rank'] = df_avg['_Average_distance'].rank(pct=True, ascending=False)
        df_avg = df_avg[list(df_avg)[-4:]+list(df_avg)[:-4]]
        df_return = pd.concat([Centrality_df, df_avg], axis=1).reindex(Centrality_df.index)
        df_return.sort_values(by='_Average_distance', ascending=False, inplace=True)
        #print(df_avg.shape[0])
        #print(df_avg)
        df_return['Similarity_score'] = df_return['_Average_distance']
        df_return['Rank'] = df_return['Rank'].rank()
        self.distance_mat =  df_return
    

    # def __init__(self, Graph_file, Centrality_file):
    def __init__(self, Centrality_file):
        #self.max_number_of_added_nodes = max_number_of_added_nodes
        #self.alpha = alpha
        #self.node_final_values = dict()
        self.results = None
        # self.Graph_file = Graph_file
        self.Centrality_file = Centrality_file

    def copy(self):
        return CentralityCosDist(**self.get_params())

    # def set_params(self, Graph_file, Centrality_file):
    def set_params(self, Centrality_file):
        # self.Graph_file = Graph_file
        self.Centrality_file = Centrality_file
        #self.max_number_of_added_nodes = max_number_of_added_nodes
        #self.alpha = alpha

    def get_params(self):

        params = {
            #'max_number_of_added_nodes': self.max_number_of_added_nodes,
            #'alpha': self.alpha
            # 'Graph_file' : self.Graph_file,
            'Centrality_file' : self.Centrality_file
        }
        return params
    
    def map_graph_centralities(self, Graph_file):
        pass

    def run(self, seed_nodes):
        self.seed_nodes = seed_nodes
        self.Centralites = pd.read_csv(self.Centrality_file)
        self.Centralites = self.Centralites.set_index(list(self.Centralites)[0])
        self.similarity_method = "cosine"
        self.Cosine_similarity(self) #, method=self.Centralites)#, method = "cosine")
        self.similarity_score = self.distance_mat['Similarity_score']
        self.rank = self.distance_mat['Rank']
        
    def get_results_df(self):
        self.results.index.name = "IDs"
        print(self.results[['Rank']])
    