import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# cria a classe do programa
class CriptWords(object):

    def limpar(self, button):
        print("Limpou")

    def __init__(self):

        glade = "criptWords.glade"

        builder = Gtk.Builder.new_from_file(glade)
        builder.add_from_file(glade)

        window = builder.get_object("janela")
        window.connect("delete-event", Gtk.main_quit)

        btn_limpar = builder.get_object("btnLimpar")
        btn_limpar.connect("clicked", self.limpar)

        window.show_all()


if __name__ == '__main__':
    application = CriptWords()
    Gtk.main()
