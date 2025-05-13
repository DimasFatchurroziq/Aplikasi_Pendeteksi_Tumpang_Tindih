import torch
from utils.treshold_util import Treshold

class SementaraService:
    # def __init__(self, treshold_repository):
    #     self.treshold_repository = treshold_repository

    def treshold_filtering(self, list_compare, treshold):
        list_treshold = []
        for compare in list_compare:
            score = compare.similarity_score
            if isinstance(score, torch.Tensor):
                score = score.item()
            if score >= treshold:
                saved = {
                    "rule_1": compare.rule_1.content,
                    "rule_2": compare.rule_2.content,
                    "similarity_score": score,
                    "scenario": compare.scenario,
                }
                list_treshold.append(saved)
        return list_treshold
        


            
            
        
