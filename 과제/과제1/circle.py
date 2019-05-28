class circle(object):
    """12주차 과제"""
    def __init__(self,r,x,y):
        self.r=r
        self.x=x
        self.y=y
    def area(self):
        return 3.141592*self.r*self.r
    def center(self):
        return (self.x,self.y)


