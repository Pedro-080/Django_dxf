from Functions import  *
import ezdxf




if __name__ == "__main__":
    
    doc = ezdxf.new()
    msp = doc.modelspace()
    closed_polyline = msp.add_lwpolyline([(0, 0), (0, 5), (5, 5), (5, 0)],close=True)
    # msp.add_lwpolyline()
    
    
    # Itera sobre as polilinhas no desenho
    for entity in msp:
        if entity.dxftype() == 'LWPOLYLINE':
            if entity.closed:
                # print(f"Polilinha fechada com pontos {entity.get_points()}")
                for point in entity.get_points():
                    print(f"Coordenadas x, y: {point[0]}, {point[1]}")
            else:
                print(f"Polilinha aberta com pontos {entity.get_points()}")


    ...