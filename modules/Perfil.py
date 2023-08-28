from .Vertice import Vertice

class Perfil:
    def __init__(self):
        self.vertices = []
        ...
        
    def __str__(self):
        for vertice in self.vertices:
            print(vertice)   
        return "\n"

    def __len__(self):
        return len(self.vertices)

    def add_vertice(self, coord_x, coord_y):
        vertice = Vertice(len(self.vertices)+1, coord_x, coord_y)
        self.vertices.append(vertice)
        ...

    def add_estruturas(self,estaqueamento):
        for estrutura in estaqueamento:
            self._add_vertice_x(estrutura)
        self._sort_num() 
        ...


    def _add_vertice_x(self,coord_x): # A partir de uma coordenada x, calcula a y e insere no perfil
        
        index = 0
        while index < len(self.vertices) and coord_x > self.vertices[index].coord_x:
            index += 1
        
        #Calcula as diferenças
        x_dif= self.vertices[index].coord_x-self.vertices[index-1].coord_x
        y_dif= self.vertices[index].coord_y-self.vertices[index-1].coord_y
        
        #Razão de variação
        m=y_dif/x_dif
        b=self.vertices[index-1].coord_y - m * self.vertices[index-1].coord_x
        coord_y = m * coord_x + b
        
        # print(f"dist x:{x_dif}")
        # print(f"dist y:{y_dif}")
        # print(f"({coord_x},{coord_y})")
        
        
        self.vertices.insert(index, Vertice(index, coord_x, coord_y)) 
        
        ...
        
    def _sort_num(self):
        for index in range(len(self.vertices)):
            # print(index+1)
            self.vertices[index].set_num(index+1)
        return 

    def poins_tuple(self):
        list_tuplas = []
        for vertice in self.vertices:
            list_tuplas.append(vertice.tupla())
        return list_tuplas
        ...

    def save_txt(self, path_file):
        save_vertices = []
        for vertice in self.vertices:
            # print(vertice)
            save_vertices.append(vertice)
            
        with open(path_file,"w") as file:
            for obj in save_vertices:
                file.write(str(obj) + "\n")  
        ...
        
    def inserir_ordenado(self, vertice):
        index = 0
        while index < len(self.vertices) and vertice.coord_x > self.vertices[index].coord_x:
            index += 1
        self.vertices.insert(index, vertice)        
        ...
        
    def find_point(self,coord_X):
        for vertice in self.vertices:
            if vertice.coord_x == coord_X:
                return vertice.tupla()
        return None
