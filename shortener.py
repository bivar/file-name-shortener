import glob
import os
from tkinter import *

class App:
    def __init__(self, master=None):
        # Fonte
        self.font = ["Yu Gothic UI Semibold", "12"]
        # Widget 1 - Texto de boas vindas
        self.wdg_info = Frame(master)
        self.wdg_info.pack()
        self.msg = Label(self.wdg_info,
                    text = "Olá! Certifique-se de que não há outros diretórios em sua pasta.")
        self.msg["font"] = self.font
        self.msg.pack()

        # Widget 2 - Texto de pergunta
        self.wdg_quest = Frame(self.wdg_info)
        self.wdg_quest.pack()
        self.msg = Label(self.wdg_quest,
                    text = "Quantos caracteres você deseja que os novos nomes tenham?")
        self.msg["font"] = self.font
        self.msg.pack()

        # Widget 3 - Texto de indicação da entrada do usuário
        self.nameLabel = Label(self.wdg_quest,text="Insira aqui: ", font=self.font)
        self.nameLabel.pack()

        # Widget 4 - Caixa de input
        self.caracters = Entry(self.wdg_quest)
        self.caracters["width"] = 10
        self.caracters["font"] = self.font
        self.caracters.pack()

        # Widget 5 - Botão
        self.button = Button(self.wdg_quest)
        self.button["text"] = "Renomear!"
        self.button["font"] = self.font
        self.button.pack()
        self.button["command"] = self.rename

        # Widget 6 - Mensagem de renomeado
        self.msg_done = Label(self.wdg_quest,
                            text = "")
        self.msg_done["font"] = self.font
        self.msg_done.pack()

    def rename(self):
        name_size = int(self.caracters.get())

        mylist = [f for f in glob.glob("*")]
        count = 0

        duplicates = []

        for file in mylist:
            index = file.find(".")
            file_index = mylist.index(file)
            name = file[:name_size] + file[index:]
            if ((file == "shortener.py") or (file == "shortener.exe")):
                pass
            else:
                path = './' + name
                if(os.path.isfile(path)):
                    duplicates.append(file)
                    pass
                else:
                    os.rename(file, name)

        for dup in duplicates:
            print(dup)
            count += 1
            index = dup.find(".")
            dup_name = dup[:name_size] + str(count) + dup[index:]
            os.rename(dup, dup_name)

        self.msg_done["text"] = ("Concluído! Os nomes foram encurtados para", name_size, "caracteres.")


def app():
    root = Tk()
    root.title("File Name Shortener - by Bivar")
    App(root)
    root.mainloop()


if __name__ == "__main__":
    app()
