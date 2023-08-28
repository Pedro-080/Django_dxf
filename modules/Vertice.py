class Vertice:
    def __init__(self,num,x,y):
        self.num = num
        self.coord_x = x
        self.coord_y = y
        
    def __str__(self):
        return f"{self.num},{self.coord_x:.4f},{self.coord_y:.4f}"

    def set_num(self,num):
        self.num=num


    def tupla(self):
        return (round(self.coord_x,4),round(self.coord_y,4))