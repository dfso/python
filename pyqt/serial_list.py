# -*- coding: utf-8 -*-

'''
obter informações em https://doc.qt.io/qt-5.10/qserialportinfo.html
'''


from PyQt5 import QtSerialPort, QtCore

portas = QtSerialPort.QSerialPortInfo.availablePorts()

print("{:-^70}".format("")) #imprime o caracter '-' 70 vezes

for p in portas:
    print("nome: {} | descrição: {}".format(p.portName(), p.description()))

print("{:-^70}".format("")) #imprime o caracter '-' 70 vezes

print("Acessando a porta '/dev/ttyUSB3'")
arduino = QtSerialPort.QSerialPort("/dev/ttyUSB3")

print(arduino.portName())
print("porta aberta: {}".format(arduino.isOpen()))

baudRate = 9600
arduino.setBaudRate(baudRate)
arduino.open(QtCore.QIODevice.ReadOnly)
print("porta aberta: {}".format(arduino.isOpen()))

data = QtCore.QByteArray()

while arduino.waitForReadyRead(1):
    data.append(arduino.readAll())

temp = bytearray(data)
print(temp.decode("utf8"))
