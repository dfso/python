# -*- coding: utf-8 -*-

from conecta import Conecta

conex = Conecta.conecta("ACESSO_RFID")

cur = conex.cursor()

query = 'INSERT INTO USUARIOS VALUES({}, \"{}\");'.format(
    "NULL", "Dênison Fábio")

print(query)

cur.execute(query)
conex.commit()

cur.close()
conex.close()
