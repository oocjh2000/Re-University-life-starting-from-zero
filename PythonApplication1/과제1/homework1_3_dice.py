import random as r
class dice(object):
    """description of class"""
    def __init__(self,side):
        self.side=side
    def roll(self):
        return r.randint(1,self.side)

if __name__=="__main__":
    dice1=dice(6)
    print(dice1.side,'면체 주사위를 굴려 나온수는',dice1.roll(),'입니다.')

