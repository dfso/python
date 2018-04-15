from conecta import Conecta

BD = "ACESSO_RFID"

conex = Conecta.conecta(BD)

cur = conex.cursor()
query = "select * from USUARIOS;"

cur.execute(query)
for (id, nome) in cur:
    print("{}, {}".format(id, nome))


cur.close()
conex.close()
