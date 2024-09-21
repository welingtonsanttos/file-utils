import os
from datetime import datetime
from zipfile import ZipFile
import zipfile
import mss
from datetime import datetime



#environments
path = os.getcwd()
pathfolder = r"Compactar"
getnow = datetime.now()
acthour = datetime.strftime(getnow, "%H%M%S")

class filesoptions():
        
    def compactFiles():
        # join caminho + filename
        zipName = os.path.join(pathfolder, 'screenZip.zip')

        # Cria o arquivo ZIP e adiciona todos os arquivos da pasta "Compactar"
        with zipfile.ZipFile(zipName, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(pathfolder):
                for filename in filenames:
                    # Evita adicionar o próprio arquivo ZIP ao arquivo compactado
                    if filename != 'screenZip.zip':
                        pathfilenamefull = os.path.join(foldername, filename)
                        # Adiciona o arquivo ao ZIP com o caminho relativo
                        zipf.write(pathfilenamefull, os.path.relpath(pathfilenamefull, pathfolder))

    
    def deletFiles():
        pathfolder = r"Compactar"
        for foldername, subfolders, filenames in os.walk(pathfolder):
            for filename in filenames:
                fullnm = os.path.join(foldername, filename)
                if filename != 'screenZip.zip':
                    os.remove(fullnm)
    
    def ScreenShots():
        with mss.mss() as sct:
            sct.shot(output=f"{pathfolder}\screenshot{acthour}.png")



if __name__ == "__main__":
    c = filesoptions 
    c.compactFiles()