# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V8
# Cálculo de catenaria

from modules.Functions import *

if __name__ == "__main__":
    catenaria_dxf = "data/perfil/catenaria_new.dxf" 
    
    # To = 1545 #kgf 
    To = 600 #kgf
    p= 0.7816  #kgf/m
    vao = 350 # vao em m

    deslocamento_y = 12
    # vertices = [(10,40),(450,0)]
    vertices = [(50,10),(450,40)]
    create_catenaria(catenaria_dxf,vertices,p,To)
