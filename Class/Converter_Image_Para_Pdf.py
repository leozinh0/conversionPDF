import os
from PIL import Image
from tempfile import TemporaryDirectory

class ConversaoToPdf:

    def __init__(self, source_dir, temp_Dir):
       self.source_dir = source_dir
       self.temp_Dir = temp_Dir

    def ConversaoPdf(self):

        lista = []
        x = 0

        # Vai adicionar todos os arquivos na Lista para que fique na ordem correta para tranformar em pdf
        # Para que quando chegue a etapa de juntar todos arquivos não fique na ordem incorreta.
        for Arquivo in os.listdir(self.source_dir) :

            lista.insert(x, Arquivo)
            x = x + 1  

        #Irá deixar deixar os arquivos em ordem graças a renomeação numerada corretamente.
        lista.sort()

        # Vai percorrer cada arquivo da listae e filtrar por extensão válida e transforma o aquivo em pdf.
        for File in lista :
            if File.split('.')[-1] in ('jpg') :
                imagem = Image.open(os.path.join(self.source_dir, File))
                imagem_converted = imagem.convert('RGB')
                
            imagem_converted.save(os.path.join(str(self.temp_Dir), '{0}.pdf'.format(File.split('.')[-2])))
        
        return