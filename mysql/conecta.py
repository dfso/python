# -*- coding: utf-8 -*-
import mysql.connector

class Conecta:

    @staticmethod
    def conecta(banco):
        """Conecta ao banco de dados

        Arguments:
            banco {[str]} -- [nome da base de dados]
        Returns:
            [conn] -- [a conexão com o banco]
        """

        conn = mysql.connector.connect(
            user='root',
            password='123',
            host='127.0.0.1',
            database=banco
        )
        return conn
    