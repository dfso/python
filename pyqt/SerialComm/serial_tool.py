import serial.tools.list_ports
import serial


class SerialTool():

    @staticmethod
    def listar_portas():
        """Lista todas as portas Comm detectadas no sistema.
        
        Returns:
            dispositivos[str] -- uma lista contendo os nomes das portas Comm
        """

        portas = serial.tools.list_ports.comports()
        dispositivos = []

        for p in portas:
            dispositivos.append(p.device)

        return dispositivos


