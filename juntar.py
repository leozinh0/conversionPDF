import PyPDF2
import os

source_dir = r'Z:\Desktop\Finaly'

os.chdir(source_dir)

lista = []
x = 0

for File in os.listdir(source_dir) :
    f_name, f_ext = os.path.splitext(File)
    f_nome = f_name.split('.')

    File = source_dir + '/' + File
    lista.insert(x, File)
    lista.sort(key=len)
 
    x = x + 1    

for pdf in lista:
    merge = PyPDF2.PdfMerger()
    writer = PyPDF2.PdfWriter()

    pdfDoc = open(pdf, 'rb')

    pdfReader = PyPDF2.PdfReader(pdfDoc)

    for k in range(0, len(pdfReader.pages)):
        pagina = pdfReader.pages[k]
        writer.add_page(pagina)

    merge.append(pdfReader)

    merge.write(r"Z:\Desktop\Finaly\merge.pdf")

    pdfDoc.close()
    merge.close()
