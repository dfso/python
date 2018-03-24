import serial

class MySerial(object):

    def __init__(self):
        print("iniciou")

    def __del__(self):
        print("saiu")


def main():
     m = MySerial()
if __name__ == '__main__':
    main()