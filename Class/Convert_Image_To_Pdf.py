import os
from PIL import Image

class ConversaoToPdf:

    def __init__(self, output_dir, source_dir):
        self.output_dir = output_dir
        self.source_dir = source_dir

    def Conversao(self):
        #Pasta que serão de entrada e saída dos arquivos
        #output_dir = r'Z:\Desktop\Finaly'
        #source_dir = r'Z:\Desktop\pdf'

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
            if File.split('.')[-1] in ('png', 'jpg', 'jpeg') :
                imagem = Image.open(os.path.join(self.source_dir, File))
                imagem_converted = imagem.convert('RGB')
                imagem_converted.save(os.path.join(self.output_dir, '{0}.pdf'.format(File.split('.')[-2])))
        
        return

