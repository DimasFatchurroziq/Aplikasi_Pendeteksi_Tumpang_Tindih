class Treshold:
    def treshold_filtering(self, score, treshold):
        if isinstance(score, torch.Tensor):
            score = score.item()
        if score >= treshold:
            return
            treshold_result.append(score)
        return treshold_result
