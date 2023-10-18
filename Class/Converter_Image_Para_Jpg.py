import os
from PIL import Image

class ConversaoToJpg:

    def __init__(self, source_dir):
       self.source_dir = source_dir

    def ConversaoJpg(self):

        ArquivosOriginais = []
        x = 0

        for Arquivo in os.listdir(self.source_dir) :

            ArquivosOriginais.insert(x, Arquivo)
            x = x + 1  

        ArquivosOriginais.sort()

        # Vai percorrer cada arquivo da lista e filtrar por extensão válida e transforma o aquivo em jpg.
        for File in ArquivosOriginais :
            if File.split('.')[-1] in ('png', 'jpg', 'jpeg') :
                imagem = Image.open(os.path.join(self.source_dir, File))
                image = imagem.convert('RGB')
                
            image.save(os.path.join(str(self.source_dir), '{0}.jpg'.format(File.split('.')[-2])))

        for arquivos in ArquivosOriginais :
            if arquivos.split('.')[-1] in ('png') :
                os.remove(self.source_dir + '\\' + arquivos)
        
        return