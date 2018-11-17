import sys
import threading
import time

import thread_ui
from PyQt5 import QtWidgets


class Teste(thread_ui.UiMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_ui(self)

        print(self.get_alive_threads())
        print(self.get_current_thread())
        self.btn_start.clicked.connect(self.start_work)


    def work(self, progressbar):
        progress = 0.00
        print("thread iniciada.")
        print(self.get_current_thread())
        while progress < 100.00:
            progress += 0.00001
            progressbar.setValue(progress)

    def start_work(self):
        time0 = time.time()

        thread_0 = threading.Thread(name="thread_proggress_1",
            target=self.work, args=(self.progressBar_1,))
        thread_0.start()
        print(self.get_alive_threads())
        time.sleep(1)
        #thread_0.join()

        thread_1 = threading.Thread(name="thread_proggress_2",
            target=self.work, args=(self.progressBar_2,))
        thread_1.start()
        print(self.get_alive_threads())
        time.sleep(1)
        #thread_1.join()

        thread_2 = threading.Thread(name="thread_proggress_3",
            target=self.work, args=(self.progressBar_3,))
        thread_2.start()
        print(self.get_alive_threads())
        thread_2.join()

        time1 = time.time()

        print(self.get_alive_threads())
        print(self.get_current_thread())
        print(self.calculate_exec_time(time0, time1))

    def stop_all_threads(self):
        pass

    def get_alive_threads(self):
        return(f"total de threads ativas: {threading.active_count()}")

    def get_current_thread(self):
        return(f"thread atual: {threading.current_thread()}")

    def calculate_exec_time(self, start, end):
        return(f"tempo de execução total: {end - start} segundos")



app = QtWidgets.QApplication(sys.argv)
window = Teste()
window.show()
sys.exit(app.exec_())
