class Stats():
    def __init__(self,names,scores):
        self.names=names
        self.scores=scores
    def mean(self):
        return sum(self.scores)/len(self.scores)
    def var(self):
        score_sq = [s ** 2 for s in self.scores]
        return sum(score_sq)/len(self.scores) - self.mean() ** 2
    def maximum(self):#maxは組み込みにあるので別の名前をつける
        M=max(self.scores)
        ids=[i for i in range(len(self.scores)) if self.scores[i]==M]
        return M, [self.names[i] for i in ids]
    def minimum(self):#minも同様
        m=min(self.scores)
        ids=[i for i in range(len(self.scores)) if self.scores[i]==m]
        return m, [self.names[i] for i in ids]

sugaku=Stats(['A','B','C'],[80,70,60])
print(sugaku.mean(), sugaku.var(), sugaku.maximum(),sugaku.minimum())