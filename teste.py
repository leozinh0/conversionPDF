import PyPDF2
import os

merge = PyPDF2.PdfMerger()

lista = []
caminho = 'Z:\Desktop\Finaly'
x = 0

for arquivo in os.listdir(caminho):
    if '.pdf' in arquivo:
        var = caminho + '\\' + arquivo

    lista.insert(x,var)
    x += 1    


for i in range(0, len(lista)):
    merge.append(PyPDF2.PdfReader(lista[i], "rb")) #f"Z:\Desktop\Finaly\Teste/{arquivo}", "rb"


merge.write(os.path.join("Result.pdf"))
