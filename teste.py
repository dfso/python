import serial

class MySerial(object):

    def __init__(self):
        print("iniciou")

    def __del__(self):
        print("saiu")

    def digaHello(self):
        """
        só imprime "olá mundo"
        """
        print("olá, mundo!")


def main():
     m = MySerial()
     m.digaHello()
     print(type(m))
if __name__ == '__main__':
    main()