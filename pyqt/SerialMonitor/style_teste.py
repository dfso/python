from PyQt5 import QtGui, QtWidgets

def style_app():
    styles = QtWidgets.QStyleFactory.keys()
    print(styles)

style_app()