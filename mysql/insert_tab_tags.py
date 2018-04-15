# -*- coding: utf-8 -*-

from conecta import Conecta

conex = Conecta.conecta("ACESSO_RFID")

cur = conex.cursor()

query = """INSERT INTO TAGS VALUES({}, "{}", {});""".format(
    "NULL", "294569", "1")

print(query)

cur.execute(query)
conex.commit()

cur.close()
conex.close()
