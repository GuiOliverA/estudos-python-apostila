#Desafio original era para acessar o site pudim.com.br
#Porém coloquei minha playlisst do Yt Music... 
import urllib
import urllib.request
from Interno import cores

try:
    site = urllib.request.urlopen('https://music.youtube.com/playlist?list=PLQV73ueKf4E18MqD4gwPQLQrzxXFB4hix')
except urllib.error.URLError:
    print(cores.vermelho('O site não está acessível no momento...\nTente novamente mais tarde '))
else:
    print(cores.verde('A playlist do Youtube Music está acessível.'))