# flake8: noqa
# Estudo sobre tratamento de DXF
# VERSÃO - V1 perfil
# Empranchamento de perfil

from Functions import  *


if __name__ == "__main__":
    perfil_original = "data/layout/Perfil_0A.dxf"
    
    perfil_copia = "data/layout/Perfil_0A_copia.dxf"
    perfil_limpo = "data/layout/Perfil_0A_LIMPO.dxf"
   
    
    # doc_copia = ezdxf.readfile(perfil_copia)
    # doc_limpo = ezdxf.readfile(perfil_limpo)
    
    
    
    # inspecionar_bloco(doc_copia ,"Carimbo Babilonia")
    # inspecionar_bloco(doc_limpo,"Carimbo Babilonia")
    
    numero_layout = 3
    #===================FUNCIONANDO========================
    # positions = busca_texto(perfil_original)
    # grifar(perfil_original,perfil_copia,positions)
    
    doc = carregar(perfil_original)
    
    
    
    
    # Cria um conjunto de layouts na quantidade da variável numero_layout
    doc = criar_layouts(doc,numero_layout)
 
     #Lista todos os blocos nomeados do arquivo original
    # lista_blocos = listar_blocos(doc)   
    
    # Insere o carimbo "Carimbo Babilonia" em todos os layouts
    doc = inserir_carimbo(doc,"Carimbo Babilonia",numero_layout)
    
    
    # doc = definir_area_viewport(doc)
    
    inspecionar_bloco(doc,"Carimbo Babilonia")
    # doc = circular(doc,(0,0))
    # definir_area_viewport(doc)
    # inserir_viewport(doc,numero_layout)
    # 
    
    
    
    
    
    
    salvar(doc,perfil_copia)
    # print(lista_blocos)
    

