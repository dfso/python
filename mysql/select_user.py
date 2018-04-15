# -*- coding: utf-8 -*-

from conecta import Conecta

conex = Conecta.conecta("ACESSO_RFID")

cur = conex.cursor()

query = """SELECT U.NOME, T.TAG FROM USUARIOS AS U INNER JOIN TAGS AS T
ON U.IDUSUARIO = T.ID_USUARIO;"""

#print(query)

cur.execute(query)

for (nome, tag) in cur:
    print("{}, {}".format(nome, tag))

cur.close()
conex.close()