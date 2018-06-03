#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial.tools.list_ports

import serial
import syslog
import time

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p[0])

porta = '/dev/ttyUSB0'

arduino = serial.Serial(porta, 9600, timeout=1)
time.sleep(2)  # wait for Arduino


while (True):
    dados = arduino.readline()
    if dados:
        print("Temperatura: ")
        print(dados)
