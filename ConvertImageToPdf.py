import os
from PIL import Image

output_dir = r'Z:\Desktop\Finaly'
source_dir = r'Z:\Desktop\pdf'

lista = []
x = 0

for Arquivo in os.listdir(source_dir) :

    lista.insert(x, Arquivo)
    lista.sort()
    
    x = x + 1  

lista.sort()

for File in lista :
    if File.split('.')[-1] in ('png', 'jpg', 'jpeg') :
        imagem = Image.open(os.path.join(source_dir, File))
        imagem_converted = imagem.convert('RGB')
        imagem_converted.save(os.path.join(output_dir, '{0}.pdf'.format(File.split('.')[-2])))

