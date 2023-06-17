import pyfiglet
from termcolor import colored

#titulo simple para los script
print('*' * 50)
print('{:^50}'.format('TITULO 1'))
print('*' * 50)

#titulo con color amarillo, negrita y aumentamos el tamaño de fuente
print('*' * 50)
print('{:^50}'.format('\u001b[1m' + '\u001b[33m' + 'TITULO 2' + '\u001b[0m', font_size=24))
print('*' * 50)

#titulo con la libreria pyfliget
titulo = pyfiglet.figlet_format('TITULO 3')
print(titulo)

#titulo usando libreria termcolor
titulo = colored('TITULO 4', 'yellow', attrs=['bold'])
print(titulo)