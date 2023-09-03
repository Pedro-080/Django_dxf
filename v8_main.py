# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V8
# Cálculo de catenaria

from modules.Functions import *

if __name__ == "__main__":
    catenaria_dxf = "data/perfil/catenaria.dxf"
    
    
    To = 1551.0428 #kgf
    p= 0.7816  #kgf/m
    vao = 350 # vao em m

    create_catenaria(catenaria_dxf,vao,p,To)
