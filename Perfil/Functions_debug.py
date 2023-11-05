from ezdxf.layouts import Paperspace
from ezdxf.document import Drawing

# Ferramenta de debug, insere um circulo na coordenada desejada
# Debug tool, inserts a circle at determinade coordenate
def circular(doc:Drawing,coordenada,cor=10):
    layout = doc.layouts.get("1")
    width = layout.dxf.paper_width
    height = layout.dxf.paper_height
    
    try:
        doc.layers.new('marker_circle',dxfattribs={'color':cor})
    except Exception as e:
        # print(f"{str(e)}")
        ...

    layout.add_circle(coordenada,radius=5,dxfattribs={'layer': 'marker_polyline','color':cor})   
    
    return doc
    
# Ferramenta de debug, insere uma polylinha com os vertices desejados
# Debug tool, inserts a polyline at determinade vertices    
def polyline(doc:Drawing,coordenada,cor=10):
    layout = doc.layouts.get("1")
    
    try:
        doc.layers.new('marker_polyline',dxfattribs={'color':cor})
    except Exception as e:
        ...

    layout.add_lwpolyline(coordenada,format='xy',dxfattribs={'layer': 'marker_polyline','color':cor}) 
    
    return doc


def add_retangulo(doc:Drawing, pontos,largura=40,altura =10, cor=6):
    msp = doc.modelspace()
    
    point_bot = min(pontos, key=lambda ponto: (ponto[0], ponto[1]))
    point_top = max(pontos, key=lambda ponto: (ponto[0], ponto[1]))
    
    # print(f"bot: {point_bot}    top: {point_top}")
    
    vertice_bl = (point_bot[0]-largura/2,point_bot[1]-altura/2)
    vertice_br = (point_bot[0]+largura/2,point_bot[1]-altura/2)
    
    vertice_tr = (point_top[0]+largura/2,point_top[1]+altura/2)
    vertice_tl = (point_top[0]-largura/2,point_top[1]+altura/2)
        
    try:
        doc.layers.new('marker_retangle',dxfattribs={'color':cor})
    except:
        None
    
    
    vertices = [vertice_bl,vertice_br,vertice_tr,vertice_tl]
    
    
    
    
    msp.add_lwpolyline(vertices,format='xy',close=True,dxfattribs={'layer': 'marker_polyline','color':cor})
    # print(corner_1)
    ...



def grifar(doc:Drawing,positions):
    msp = doc.modelspace()
    
    try:
        doc.layers.new('marker',dxfattribs={'color':10})
    except:
        None

    for center in positions:
        msp.add_circle(center,radius=5,dxfattribs={'layer': 'marker'})   
    
    return doc

