import pandas as pd
import numpy as np
from Vento import Vento
from PosteDT import PosteDT


obj = Vento(16,26,20,135,16,18)

altura=19
esforco=1500
poste = PosteDT(altura,esforco)

print(f"Pressao de vento a 30s: {obj.pressao_vento()[0]:.2f} kgf")
print(f"Pressao de vento a 2s: {obj.pressao_vento()[1]:.2f} kgf")

print(f"\n--------Poste {altura}/{esforco}--------")
print(f"Topo a: {poste.Lado_a:.0f}      Base A: {poste.Lado_A:.0f}")
print(f"Topo b: {poste.Lado_b:.0f}      Topo B: {poste.Lado_B:.0f}")

print(f"\nAltura Total: {poste.altura:.1f} \nEngaste: {poste.engaste:.1f}")
print(f"Altura util: {poste.h_util:.1f}  \nAltura normalizada {poste.h_normal:.1f}")


print(f"\n-----------------------------")

obj.vento_estrutura(poste)