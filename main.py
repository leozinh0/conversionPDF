import PySimpleGUI as sg
from Class import renomear_arquivo
from Class import Convert_Image_To_Pdf
from Class import juntar_pdf

yes = 'Yes'

sg.theme('Black')

layout_esquerdo = [
    [sg.Image(filename =r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo.png',
              size = (350, 220),
              pad= (10,10))
    ]
]

layout_Direito = [
    [sg.Text('Caminho de origem:')],
    [sg.Input(key='IptOrigem'), sg.Button('Procurar', key='btnProcurarOrigem')],
    [sg.Text('Caminho de destino:')],
    [sg.Input(key='IptDestino'), sg.Button('Procurar', key='btnProcurarDestino')],
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
    'Converter para PDF',
    layout,
    icon = r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico'    
)

while True:
    event, values = window.read()

    try:
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            if yes == sg.popup_yes_no('Você tem certeza?',  icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico', modal= True):
                break

        match(event):
            case 'btnProcurarOrigem':
                window['IptOrigem'].update(sg.popup_get_folder('Escolha a pasta de Origem', icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico'))

            case 'btnProcurarDestino':
                window['IptDestino'].update(sg.popup_get_folder('Escolha a pasta de Destino',  icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico'))

            case 'Converter':
                if values['IptOrigem'] == '' and values['IptDestino'] == '':
                    sg.popup_no_buttons('Você esqueceu de preencher todos os campos', 
                                        auto_close= True, 
                                        auto_close_duration=5,  
                                        icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico'
                                        )

                elif values['IptOrigem'] == '':
                    sg.popup_no_buttons('Você esqueceu de escolher a pasta de Origem', auto_close= True, auto_close_duration=5,  icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico')

                elif values['IptDestino'] == '':
                    sg.popup_no_buttons('Você esqueceu de escolher a pasta de Destino', auto_close= True, auto_close_duration=5, icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico')

                elif values['IptOrigem'] != '' and values['IptDestino'] != '':
                    Renomear = renomear_arquivo.RenomearArquivos(sourceFolder= values['IptOrigem'])
                    Renomear.Renomear()

                    Transformar = Convert_Image_To_Pdf.ConversaoToPdf(source_dir= values['IptOrigem'])
                    Transformar.Conversao()

                    JuntarPdf = juntar_pdf.JuntarPdfs(destiny_dir= values['IptDestino'])
                    JuntarPdf.Juntar()

                window['IptOrigem'].update('') 
                window['IptDestino'].update('') 

                JuntarPdf.ApagarPastaTemporaria()
    except Exception as e:
        sg.popup_scrolled(str(e), no_titlebar= False, icon= r'Z:\\vscode-workspace\\python\\conversionPDF\\Assets\\Logo2.ico')

window.close()