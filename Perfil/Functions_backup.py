import ezdxf
from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing
import ezdxf.math
# print(ezdxf.__version__)

# from ezdxf.acc import Vec2



def list_all_layouts(file_path):
    doc = ezdxf.readfile(file_path)
    layouts = doc.layouts
    
    # layout_names = [layout.dxf.name for layout in layouts if layout.is_any_layout]
    layouts_sem_model = [layout.name for layout in layouts if layout.name != 'Model']
    
    # return layout_names
    return layouts_sem_model


def listar_numero_layouts(caminho_arquivo):
    # Abra o documento DXF em modo somente leitura
    doc = ezdxf.readfile(caminho_arquivo)
    layouts = doc.layouts
    # Obtenha o número de layouts
    numero_layouts = layouts.__iter__()

    return numero_layouts


def duplicar_layout(caminho_arquivo, nome_layout_original, nome_layout_novo,caminho_copia):
    # Abre o documento DXF em modo de leitura e escrita
    doc = ezdxf.readfile(caminho_arquivo)

    # Obtém o layout original
    layout_original = doc.layout(name=nome_layout_original)

    if layout_original is None:
        print(f'O layout "{nome_layout_original}" não foi encontrado.')
        return

    # Cria um novo layout
    novo_layout = doc.layouts.new(name=nome_layout_novo)

    # Copia as entidades do layout original para o novo layout
    for entity in layout_original:
        novo_layout.add_entity(entity.copy())

    # Salva o documento com o novo layout
    doc.saveas(caminho_copia)



def duplicate_layout(path_file, save_path, source_layout_name,new_layout_name):
    doc = ezdxf.readfile(path_file)
    
    existing_layout = doc.layouts.get(source_layout_name)
    if existing_layout:
        new_layout = doc.layouts.new(new_layout_name)
        for entity in existing_layout:
            new_layout.add_entity(entity)
        
        ...
    # layouts = doc.layouts 
    
    doc.saveas(save_path) 
    
    
    
    
    
    
    # if source_layout_name in layouts:  # Verifica se o layout de origem existe
    #     source_layout = layouts.get(source_layout_name)
    #     new_layout = layouts._add_layout(new_layout_name,layout="Layout2")
    #     # new_layout.copy_from(source_layout)

    #     doc.saveas(output_file_name)  # Salva o arquivo DXF duplicado
    # else:
    #     print(f"Layout {source_layout_name} não encontrado.")
        
        
        
# def duplicate_layout(source_layout_name, target_layout_name, output_file_name):
#     doc = ezdxf.new(dxfversion='R2010')  # Cria um novo documento DXF
#     layouts = doc.layouts  # Obtém a lista de layouts
#     if source_layout_name in layouts:  # Verifica se o layout de origem existe
#         source_layout = layouts.get(source_layout_name)
#         target_layout = layouts.copy_layout(source_layout, target_layout_name)  # Duplica o layout
#         doc.layouts._dxf_layouts
        
#         doc.saveas(output_file_name)  # Salva o arquivo DXF duplicado
#     else:
#         print(f"Layout {source_layout_name} não encontrado.")      
        
        
        
        
        
        
        
        
        
        
def test(file_path):
    doc = ezdxf.readfile(file_path)
    layouts = doc.layouts
    
    layout01 = layouts.set_active_layout("01")
    
    dxf = layout01.dxf_layout.dxf
    
    
    # layouts_list = doc.layout_names_in_taborder()
    
    
    
    
    # layouts_list = doc.layouts.get_active_layout_key()
    # layouts_list = doc.layouts.get_layout_by_key("D2")
    
    

    
    # layouts_list = layouts.names_in_taborder()
    # layouts_list = layouts.names()
    # return layouts_list


def print_entity(e):
    print("LINE on layer: %s\n" % e.dxf.layer)
    print("start point: %s\n" % e.dxf.start)
    print("end point: %s\n" % e.dxf.end)
    return None

def test2(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    for e in msp:
        if e.dxftype()== "LINE":
            print_entity(e)
    ...
    
def busca_lines(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    lines = msp.query("TEXT")
    for e in lines:
        print_entity(e)
        
            
def busca_texto(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    texts = [entity for entity in msp if entity.dxftype() == 'MTEXT']
    
    positions = []
    
    
    for text in texts:
        try:
            text.dxf.text = int(text.dxf.text)
            positions.append(text.dxf.insert)
            print(f'Texto: {text.dxf.text},Typo: {type(text.dxf.text)} , Posição: {text.dxf.insert}') 
        except:
            None
        
    return positions
    ...
    
def grifar(file_path,save_path,positions):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    
    try:
        doc.layers.new('marker',dxfattribs={'color':10})
    except:
        None
    

    for center in positions:
        msp.add_circle(center,radius=5,dxfattribs={'layer': 'marker'})   
    
    doc.saveas(save_path)    

    ...

def draw_crossings_lines(psp: Paperspace):
    # These layouts have no margins and offset defined, so the drawing space is
    # the whole sheet, but printers and plotters will not print to the
    # border of the sheet! In real world files keep always a safety space between
    # the sheet borders and the content. The size of that safety space cannot be
    # known because it's different for each printer and plotter.
    width = psp.dxf.paper_width
    height = psp.dxf.paper_height
    psp.add_line((0, 0), (width, height))
    psp.add_line((0, height), (width, 0))


def criar_viewport(file_path,save_path):
    doc = ezdxf.readfile(file_path)

 
    layout1 = doc.page_setup("Layout1", "ISO A0", landscape=True)
    layout2 = doc.page_setup("Layout2", "ISO A0", landscape=False)
    draw_crossings_lines(layout1)
    draw_crossings_lines(layout2)
        
    doc.saveas(save_path)         


    
def criar_layouts(file_path, num_layouts):
    doc = ezdxf.readfile(file_path)

    list_layouts = list(range(1,num_layouts+1))
 
    for aba in list_layouts:     
        doc.page_setup(str(aba), "ISO A1", landscape=True)


    return doc


def salvar(doc: Drawing, save_path):
    output_file = ezdxf.new(dxfversion='R2013')
    output_msp = output_file.modelspace()
    
    # for e in doc.modelspace():
    #     output_msp.add_entity(e)
    
    try:
        
        
        output_file.saveas(save_path)
    except:
        print("O arquivo não pode ser salvo")


def listar_blocos(file_path):
    doc = ezdxf.readfile(file_path)
    lista_blocos = []
    for block in doc.blocks:
        if not block.name[0] == "*":
            # print(f"block: {block.name} ")
            lista_blocos.append(block.name)
    
    return lista_blocos
    

def inserir_carimbo(doc:Drawing,nome_carimbo,numero_layout):
        
    list_layouts = list(range(1,numero_layout+1))        
    
    for numero in list_layouts:
        msp = doc.layouts.get(str(numero))   
        msp.add_blockref(nome_carimbo,insert=(0,0))
        ...
    
    
    return doc
       
    
def inserir_viewport(doc:Drawing,numero_layout):
    list_layouts = list(range(1,numero_layout+1))   
    for numero in list_layouts:
        layout = doc.layouts.get(str(numero))
        # viewport = layout.add_viewport(center=(4, 5), width=8, height=6, view_center_point=(0, 0), view_height=20)
        # create_viewports(layout)
        # buscar_viewport(layout)
    
    # definir_area_viewport(doc,list_layouts)
    
    
    return doc

  
def create_viewports(paperspace: Paperspace):
  
    paperspace.add_viewport(
        center=(16, 13.5),
        size=(0.3, 0.15),
        view_center_point=(10, 6.25),
        view_height=7.5,
    )
    paperspace.add_viewport()



def definir_area_viewport(doc:Drawing,list_layouts):
    layout = doc.layouts.get(str(list_layouts[0]))
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    center =(width/2,height/2) 
    
    
    
    ...


def inspecionar_bloco(doc:Drawing,nome_bloco):
    msp = doc.modelspace()
    
    
    print(f"n de entidades: {len(msp)}")
    
    
    
    # try:
    #     block = doc.blocks.get(nome_bloco)
    #     if block is not None:
    #         for e in block:
    #             if e.dxftype() == "LWPOLYLINE" :
    #                 print(e.closed)
    # except:
    #     print("erro")
    
    ...





def buscar_viewport(layout: Paperspace):
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height 
    print(f"width: {width}")
    print(f"height: {height}")
    
    
    
    
    
    
    # points = [(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)]
    
    # layout.add_lwpolyline(points,format='xy')
    # # linha = layout.add_line([(0,0), (1,1)])
    # ezdxf.math.intersection_line_line_2d
    # line1_start = ezdxf.math.Vec2(0, 0)
    # line1_end = ezdxf.math.Vec2(3, 3)

    # line2_start = ezdxf.math.Vec2(0, 3)
    # line2_end = ezdxf.math.Vec2(3, 0)

    # intersection_point = ezdxf.math.intersection_line_line_2d((line1_start, line1_end), (line2_start, line2_end))

    # if intersection_point is not None:
    #     print(f"As linhas se cruzam no ponto {intersection_point}.")
    # else:
    #     print("As linhas não se cruzam.")   
    
    
    
    
    # if e.dxftype()== 'LINE' or e.dxftype() == "LWPOLYLINE":
    #     ponto_intersecao = polilinha.intersect(e)
    #     if ponto_intersecao:
    #         polilinha.append(ponto_intersecao[0])
    #         break
    #     print(f"{e.dxfattribs} \n")
    #     # intersecao = e
        
    ...
    




# ===============APAGAR=====================    
    

# def localizar_carimbo(file_path,save_path):
#     doc = ezdxf.readfile(file_path) 
#     # msp = doc.modelspace()
    
#     all_blocks = set()
#     # all_atributos = []
    
#     # for block in doc.blocks:
#     #     block_properties = []
#     #     for entity in block:
#     #         block_properties.append((entity.dxftype(), entity.dxfattribs()))
#     #     all_properties.append((block.name, block_properties)) 



    
  
#     # for block in doc.blocks:
#     #     atributos = dir(block)
#     #     all_atributos.append((block.name, atributos))

    
#     # all_blocks = list(all_blocks)
    
#     # for block in doc.blocks:
#     #     if not block.block.is_anonymous:
            
#     #         print(f"block: {block.name} ")
#     for block in doc.blocks:
#         if not block.name[0] == "*":
#             print(f"block: {block.name} ")    
    
    
#     # for block in all_atributos:
#     #     print(f"block: {block}\n")        
   
        
#     # for entity in msp:
#     #     if entity.dxftype() == 'INSERT':
#     #         block_name = entity.dxf.name
#     #         if block_name:                
#     #             all_blocks.add(entity.dxf.name)

#     # for block in doc.blocks:
#     #     if block_name:
#     #         all_blocks.add(block.name)
    
#     # all_blocks = list(all_blocks)
    
#     # for block in all_blocks:
#     #     print(f"block: {block}")

