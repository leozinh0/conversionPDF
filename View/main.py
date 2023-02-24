#from renomear_arquivo import RenomearArquivos
#from Convert_Image_To_Pdf import ConversaoToPdf
#from juntar_pdf import JuntarPdf
import PySimpleGUI as sg

sg.theme('Black')

layout_esquerdo = [
    [sg.Image(filename =r'.\\Assets\\Logo.png',
              size = (350, 220),
              pad= (10,10))
    ]
]

layout_Direito = [
    [sg.Text('Caminho de origem:')],
    [sg.Input(), sg.Button('Procurar')],
    [sg.Text('Caminho de destino:')],
    [sg.Input(), sg.Button('Procurar')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Push(), sg.Button('Cancelar'), sg.Button('Converter')]
]

layout = [
    [sg.Column(layout_esquerdo), sg.VSeparator(pad= (20)), sg.Column(layout_Direito)]
]

window = sg.Window(
    'Converter para PDF', #110
    layout    
)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Cancelar':
        print(sg.popup_yes_no('Você tem certeza?'))
        
        if event == 'Yes':
            break
        
#sg.popupGetFolder('Escolher a pasta')

window.close()


#Renomear = RenomearArquivos(sourceFolder= 'Z:\Desktop\pdf')
#Renomear.Renomear()

#Transformar = ConversaoToPdf(output_dir = r'Z:\Desktop\Finaly', source_dir = r'Z:\Desktop\pdf')
#Transformar.Conversao()

#Juntar = JuntarPdfs(source_dir= 'Z:\Desktop\Finaly')
#Juntar.Juntar()