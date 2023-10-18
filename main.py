import os
import tempfile
import PySimpleGUI as sg
from Class import renomear_arquivo
from Class import Converter_Image_Para_Pdf
from Class import juntar_pdf 
from Class import Converter_Image_Para_Jpg 

sg.theme('Black')

layout_esquerdo = [
    [sg.Image(filename= "Logo.png",
              size= (350, 220),
              pad= (10,10)
             )
    ]
]

layout_Direito = [
    [sg.Text('Nome do Arquivo:')],
    [sg.Input(key= 'edtNomeArquivo')],
    [sg.Text('Caminho de origem:')],
    [sg.Input(key= 'edtOrigem', default_text= 'Z:\\Desktop\\Origem'), sg.Button('Procurar', key= 'btnProcurarOrigem')],
    [sg.Text('Caminho de destino:')],
    [sg.Input(key= 'edtDestino', default_text= 'Z:\\Desktop\\Result'), sg.Button('Procurar', key= 'btnProcurarDestino')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('@Leozinho_otto'),sg.Push(), sg.Button('Cancelar'), sg.Button('Converter')]
]

layout = [
    [sg.Column(layout_esquerdo), sg.VSeparator(pad= (20)), sg.Column(layout_Direito)]
]

window = sg.Window(
    'Converter para PDF',
    layout,
    icon= r'Logo2.ico'
)

while True:
    event, values = window.read()

    try:
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break

        match(event):
            case 'btnProcurarOrigem':
                window['edtOrigem'].update(sg.popup_get_folder('Escolha a pasta de Origem',
                                                               keep_on_top= True, 
                                                               icon= r'Logo2.ico'))

            case 'btnProcurarDestino':
                window['edtDestino'].update(sg.popup_get_folder('Escolha a pasta de Destino', 
                                                                keep_on_top= False,
                                                                icon= r'Logo2.ico'))

            case 'Converter':
                if values['edtOrigem'] == '' and values['edtDestino'] == '' and values['edtNomeArquivo'] == '':
                    sg.popup_no_buttons('Você esqueceu de preencher todos os campos!', 
                                        auto_close= True, 
                                        auto_close_duration= 2,  
                                        icon= r'Logo2.ico',
                                        title= 'AVISO')
                    
                elif values['edtOrigem'] == '':
                    sg.popup_no_buttons('Você esqueceu de escolher a pasta de Origem!', 
                                        auto_close= True, 
                                        auto_close_duration= 2,
                                        icon= r'Logo2.ico',
                                        title= 'AVISO')

                elif values['edtDestino'] == '':
                    sg.popup_no_buttons('Você esqueceu de escolher a pasta de Destino!', 
                                        auto_close= True, 
                                        auto_close_duration= 2, 
                                        icon= r'Logo2.ico',
                                        title= 'AVISO')

                elif values['edtNomeArquivo'] == '':
                    sg.popup_no_buttons('Você esqueceu de informar o nome do arquivo!', 
                                        auto_close= True,
                                        auto_close_duration= 2, 
                                        icon= r'Logo2.ico',
                                        title= 'AVISO',)
                    
               

                elif values['edtOrigem'] != '' and values['edtDestino'] != '' and values['edtNomeArquivo'] != '':

                    caminhoDaPastaTemporay = tempfile.gettempdir() + '\\' + 'ConversionPdf'
                
                    if not os.path.exists(caminhoDaPastaTemporay):
                        os.mkdir(caminhoDaPastaTemporay)

                    ConverterJpg = Converter_Image_Para_Jpg.ConversaoToJpg(source_dir= values['edtOrigem'])
                    ConverterJpg.ConversaoJpg()

                    Renomear = renomear_arquivo.RenomearArquivos(sourceFolder= values['edtOrigem']) 
                    Renomear.Renomear()

                    ConverterPdf = Converter_Image_Para_Pdf.ConversaoToPdf(source_dir= values['edtOrigem'], temp_Dir= caminhoDaPastaTemporay)
                    ConverterPdf.ConversaoPdf()

                    Juntar = juntar_pdf.JuntarPdfs(destiny_dir= values['edtDestino'], temp_Dir= str(caminhoDaPastaTemporay))
                    Juntar.Juntar(nomeArquivo= values['edtNomeArquivo'])

                    Juntar.ApagarPastaTemporaria()

                    window['edtNomeArquivo'].update('') 
    except Exception as MsgError:
        sg.popup_scrolled(str(MsgError),
                          title= 'Error',
                          icon= r'Logo2.ico',
                          size= (50, 10))

window.close()