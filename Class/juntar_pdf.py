import PyPDF2
import os

class JuntarPdfs:

    def __init__(self, source_dir):
        self.source_dir = source_dir

    def Juntar(self):
        lista = []
        x = 0

        merge = PyPDF2.PdfMerger()

        # Vai percorrer todos os arquivos da pasta e fazer uma filtragem para apenas arquivos que são pdf.
        # E armazenar dentro da lista em ordem o caminho do arquivo mais o nome do mesmo para que o append 
        # Possa achar e adicionar o arquivo com garantia. 
        for arquivo in os.listdir(self.source_dir):
            if '.pdf' in arquivo:
                var = self.source_dir + '\\' + arquivo

            lista.insert(x,var)
            x += 1    

        # Vai percorrer a lista e para cada arquivo o 'PdfReader' vai lê o binário do arquivo e fazer append
        # do arquivo lido. 
        for i in range(0, len(lista)):
            merge.append(PyPDF2.PdfReader(lista[i], "rb")) 

        # Vai adicionar os arquivos da lista com o caminho especificado, caso não exista esse arquivo,
        # vai ser criado antes de adicionar nele.                
        return merge.write(os.path.join("Z:\\Desktop\\Result\\Result.pdf"))
