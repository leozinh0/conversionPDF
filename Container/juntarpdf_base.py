import os
import PyPDF2 as pdf

def concatenaPdf(caminho):

    os.chdir(caminho)

    lista01= []
    x = 0

    for File in os.listdir(caminho) :
        f_name, f_ext = os.path.splitext(File)
        f_nome = f_name.split('.')

        File = caminho + '\\' + File

        lista01.insert(x, File)
    
        x = x + 1    

    lista = sorted(lista01)
    

    arquivos = lista
    destino = r'concatenado\Result.pdf'

    #Cria o diretório de resultado, caso não exista
    if not os.path.exists('concatenado'):
        os.makedirs(r'.\concatenado')
        print('Diretório de destino criado\nProsseguindo...')
    else:
        print('Diretório de destino já existente\nProsseguindo...')

    try:
        #Abertura dos arquivos
        pdfWriter = pdf.PdfWriter()

        #Leitura de todos os arquivos da pasta
        for j in range(0, len(arquivos)):
            pdfDoc = open(arquivos[j], 'rb')

            pdfReader = pdf.PdfReader(pdfDoc)

            #Adiciona todas as páginas de cada arquivo
            for k in range(0, len(pdfReader.pages)):
                pagina = pdfReader.pages[k]
                pdfWriter.add_page(pagina)

            pdfResultado = open(destino, 'ab')
            pdfWriter.write(pdfResultado)

            pdfDoc.close()
            pdfResultado.close()
    except Exception as exc:
        print('Administrador: verificar existência de exceções\n'+ str(exc))
        return str(exc)

    print(f'Arquivo gerado em:\n{os.getcwd()}\{destino}')
    return f'Arquivo gerado em:\n{os.getcwd()}\{destino}'

def main():
    caminho = r'Z:\Desktop\Finaly'
    response = concatenaPdf(caminho)

main()
