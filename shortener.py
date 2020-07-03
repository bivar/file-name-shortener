import glob
import os

def rename(name_size):

    mylist = [f for f in glob.glob("*")]

    for file in mylist:
        index = file.find(".")
        extension = file[index:]
        os.rename(file, (file[:name_size] + extension))


if __name__ == "__main__":
    name_size = int(input("Quantos caracteres você deseja ter no nome do arquivo?"))
    rename(name_size)
