import sys

from PyQt5 import QtWidgets, QtCore

import gui
import serial_tool
import threads_r_w


class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):

    pyqt_version = QtCore.PYQT_VERSION_STR
    autor = "dfso"
    versao = "1.0.b / agosto-2018"
    github = "https://github.com/dfso"
    icons_web = "https://icons8.com"

    dispositivo = None
    read_thread = None
    write_thread = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # muda o style da aplicação
        QtWidgets.QApplication.setStyle(
            QtWidgets.QStyleFactory.create('Fusion')
        )

        self.actionDesconectar.setDisabled(True)
        self.line_cmd.setDisabled(True)

        self.reload_portas()

        # self.setStyleSheet(open("style.qss", "r").read())

        print(f'Usando PyQt {self.pyqt_version}')

        self.actionConectar.triggered.connect(self.conectar)
        self.actionDesconectar.triggered.connect(self.desconectar)
        self.actionReload.triggered.connect(self.reload_portas)
        self.action_sair.triggered.connect(self.close_app)
        self.action_about.triggered.connect(self.about_this_app)
        self.line_cmd.returnPressed.connect(self.enviar_cmd)
        self.action_limpar.triggered.connect(self.text_log.clear)

    def conectar(self):
        """Abre conexão com o dispositivo.
        """

        self.dispositivo = serial_tool.SerialTool.conectar(
            self.combo_portas.currentText(),
            self.combo_bauds.currentText())
        if self.dispositivo.is_open:
            self.label_estado_porta.setText("Porta aberta")
            print("Conexão estabelecida.")
            self.actionConectar.setDisabled(True)
            self.line_cmd.setEnabled(True)
            self.actionDesconectar.setEnabled(True)
        self.read_thread = threads_r_w.ReadThread(self.dispositivo)
        self.read_thread.signal.connect(self.text_log.append)
        self.read_thread.start()

    def desconectar(self):
        """Fecha a conexão com o dispositivo.
        """

        self.dispositivo.close()
        self.read_thread.stop_work()
        if self.write_thread is None:
            pass
        else:
            self.write_thread.stop_work()
        if not self.dispositivo.is_open:
            self.label_estado_porta.setText("Conexão encerrada.")
            print("Conexão encerrada.")
            self.actionConectar.setEnabled(True)
            self.actionDesconectar.setDisabled(True)
            self.line_cmd.setDisabled(True)

    def enviar_cmd(self):
        """Envia comandos para o dispositivo conectado.
        """

        self.write_thread = threads_r_w.WriteThread(
            self.dispositivo, self.line_cmd.text())
        self.write_thread.start()
        self.text_log.append("<b><font color = green>Comando: "
                             + self.line_cmd.text() + "</font></b>")

    def reload_portas(self):
        """Atualiza a lista de dispositivos detectados.
        """

        self.combo_portas.clear()
        portas = serial_tool.SerialTool.listar_portas()
        self.combo_portas.addItems(portas)

    def about_this_app(self):
        """Exibe uma mensagem com informações sobre o programa.
        """
        msg = f"""<font face="Consolas" size=4>Muito obrigado por usar nossa aplicação!
                         <p>Um controlador para sua MiniCNC.</p>
                         <p>autor: {self.autor}</p>
                         <p>versão do software: {self.versao}</p>
                         <p>Usando PyQt versão {self.pyqt_version}</p>
                         <p>Visite-nos em: <a href={self.github}>Github @dfso</a></p>
                         <p>Ícones disponíveis em: 
                         <a href={self.icons_web}>https://icons8.com/</a></p>"""
        QtWidgets.QMessageBox.about(self, "Sobre...", msg)

    def close_app(self):
        """Fecha as conexões (se abertas) e fecha o programa.
        """

        if self.dispositivo is not None:
            self.desconectar()
        print("Programa encerrado.")
        self.close()


app = QtWidgets.QApplication(sys.argv)
my_window = App()
my_window.show()
sys.exit(app.exec_())
