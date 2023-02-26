import PyPDF2
import os
class JuntarPdfs:

    def __init__(self, destiny_dir):
        self.destiny_dir = destiny_dir

    def Juntar(self):
        lista = []
        x = 0

        merge = PyPDF2.PdfMerger()

        # Vai percorrer todos os arquivos da pasta e fazer uma filtragem para apenas arquivos que são pdf.
        # E armazenar dentro da lista em ordem o caminho do arquivo mais o nome do mesmo para que o append 
        # Possa achar e adicionar o arquivo com garantia. 
        for arquivo in os.listdir(r'Z:\\Desktop\\Temporary'):
            if '.pdf' in arquivo:
                var = r'Z:\\Desktop\\Temporary' + '\\' + arquivo

            lista.insert(x,var)
            x += 1    

        # Vai percorrer a lista e para cada arquivo o 'PdfReader' vai lê o binário do arquivo e fazer append
        # do arquivo lido. 
        for i in range(0, len(lista)):
            merge.append(PyPDF2.PdfReader(lista[i], "rb")) 

        # Vai adicionar os arquivos da lista com o caminho especificado, caso não exista esse arquivo,
        # vai ser criado antes de adicionar nele.                
        return merge.write(os.path.join(self.destiny_dir + '\\' +'Result.pdf'))
    
    def ApagarPastaTemporaria(self):

        caminhoPasyaTemporaria = r'Z:\\Desktop\\Temporary'        
        lista = []
        y = 0

        for arquivo in os.listdir(caminhoPasyaTemporaria):
            
            var = caminhoPasyaTemporaria + '\\' + arquivo

            lista.insert(y,var)
            y += 1  

        for arquivo in lista:
            os.remove(arquivo)
        
        dirPath = caminhoPasyaTemporaria
        os.rmdir(dirPath)

