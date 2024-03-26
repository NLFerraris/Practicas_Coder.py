import json

mi_lista=(["Homero","Marge","Bart","Lisa","Maggie"])

f = open("personajes.txt","w")

lista_convertida_json = json.dumps(mi_lista)

f.write(lista_convertida_json)

f.close()


f = open("personajes.txt","r")

contenido = f.read()

mi_lista_leida = json.loads(contenido)

f.close()

print(mi_lista_leida)

