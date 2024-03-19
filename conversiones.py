import sys

sol = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar = float(sys.argv[3])

peso_chileno = int(sys.argv[4])

tasas = {'Sol Peruano' : sol,
         'Peso Argentino' : peso_argentino,
         'Dolar' : dolar
}

print(f"Los {peso_chileno} pesos chilenos equivalen a:")
print(f"{tasas['Sol Peruano'] * peso_chileno} soles")
print(f"{tasas['Peso Argentino'] * peso_chileno} pesos argentinos")
print(f"{tasas['Dolar'] * peso_chileno} dólares")