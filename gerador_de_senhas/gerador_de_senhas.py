#!/usr/bin/python3
import gi
import random
gi.require_version("Gtk", "3.0")
<<<<<<< HEAD
from gi.repository import Gtk, Gdk
=======
from gi.repository import Gtk
>>>>>>> 3951cca778187b879279ad68881eed20a8367084


# cria a classe do programa
class GeradorDeSenhas(Gtk.Window):

    glade = "gerador_de_senhas.glade"

    builder = Gtk.Builder.new_from_file(glade)
    builder.add_from_file(glade)

<<<<<<< HEAD
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    entry_tamanho = builder.get_object("entry_tamanho")
    entry_saida = builder.get_object("entry_saida")
    btn_limpar = builder.get_object("btn_limpar")
    btn_copiar = builder.get_object("btn_copiar")
=======
    entry_tamanho = builder.get_object("entry_tamanho")
    entry_saida = builder.get_object("entry_saida")
    btn_limpar = builder.get_object("btn_limpar")
>>>>>>> 3951cca778187b879279ad68881eed20a8367084

#==============================================================================
#   gera a tabela ascII
#==============================================================================
    def get_tabela(self):
        asc = []
        for i in range(33, 126):
            asc += chr(i)

        return asc

    def gerar_senha(self, button):

        tabela = self.get_tabela()
        try:
            tamanho = int(self.entry_tamanho.get_text())
        except ValueError as e:
            print(str(e))
<<<<<<< HEAD
            #exit(0)
=======
            exit(1)
>>>>>>> 3951cca778187b879279ad68881eed20a8367084

        senha = ''

        try:
            for x in range(tamanho):
                senha += tabela[int(random.random() * 94)]
        except IndexError as erro:
            print(str(erro))
            senha = ''
            self.entry_saida.set_text(str(erro))
            pass

        print("Sua senha: %s" % senha)
        self.entry_saida.set_text(senha)

<<<<<<< HEAD
    def copy_to(self, widget):
        self.clipboard.set_text(self.entry_saida.get_text(), -1)
        print("Senha copiada para clipboard")

=======
>>>>>>> 3951cca778187b879279ad68881eed20a8367084
    def limpar(self, sinal):
        self.entry_saida.set_text("")

    def __init__(self):

        window = self.builder.get_object("janela")
        window.connect("delete-event", Gtk.main_quit)

        btn_gerar = self.builder.get_object("btn_gerar")
        btn_gerar.connect("clicked", self.gerar_senha)
<<<<<<< HEAD

        self.btn_copiar.connect("clicked", self.copy_to)

=======
>>>>>>> 3951cca778187b879279ad68881eed20a8367084
        self.btn_limpar.connect("clicked", self.limpar)

        self.entry_tamanho.connect("activate", self.gerar_senha)

        window.show_all()


if __name__ == '__main__':
    programa = GeradorDeSenhas()
    Gtk.main()
