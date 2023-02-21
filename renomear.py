import os

Folder = r'Z:\Desktop\pdf'
os.chdir(Folder)

x = 0

padrao1 = '0'
padrao2 = '00'

for f in os.listdir(Folder) : 
    f_name, f_ext = os.path.splitext(f)
    f_nome = f_name.split('.')

    F_Nome = str(x)
    
    if x <= 9:
        F_Nome = padrao2 + str(x)

    if x >= 10:
       F_Nome = padrao1 + str(x)
    
    if x >= 100:
      F_Nome = str(x)  

    new_name = (f'{F_Nome}{f_ext}')

    os.rename(f, new_name)
    
    x = x + 1

    print(new_name)
        
