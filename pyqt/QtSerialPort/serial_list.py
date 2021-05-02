# -*- coding: utf-8 -*-

'''
obter informações em https://doc.qt.io/qt-5.10/qserialportinfo.html
'''


from PyQt5 import QtSerialPort

portas = QtSerialPort.QSerialPortInfo.availablePorts()

print("{:-^70}".format("")) #imprime o caracter '-' 70 vezes

for p in portas:
    print("nome: {} | descrição: {}".format(p.portName(), p.description()))

print("{:-^70}".format("")) #imprime o caracter '-' 70 vezes

