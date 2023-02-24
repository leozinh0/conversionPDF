import os

class RenomearArquivos:

# Caminho da pasta que se encontras os arquivos

  def __init__(self, sourceFolder):
    self.sourceFolder = sourceFolder 

  def Renomear(self):

    os.chdir(self.sourceFolder)

    #Variável de incremento
    x = 0

    standard1 = '0'
    standard2 = '00'

    # Vai percorrer cada arquivo dentro da pasta e renomear de acordo com incremento
    # em que for esteja de acordo com a quantidade de arquivos no total
    for file in os.listdir(self.sourceFolder) : 
      file_name, file_ext = os.path.splitext(file)

      F_Nome = str(x)
        
      if x <= 9:
        F_Nome = standard2 + str(x)

      if x >= 10:
        F_Nome = standard1 + str(x)
        
      if x >= 100:
        F_Nome = str(x)  

      new_name = (f'{F_Nome}{file_ext}')
      os.rename(file, new_name)
        
      x = x + 1

    return