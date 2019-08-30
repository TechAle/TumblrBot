## example of exrapolate some elements from a site web

## library
import requests

## static ip
ip_static = "https://it.wikiquote.org/wiki/Wikiquote:Archivio_delle_citazioni_del_giorno/"
## dynamic ip
ip_dinanic = "gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split()
num = 1
## get all ip
for j in ip_dinanic:
    ## request
    r = requests.get(ip_static + j)
    ## get source
    prova_1 = r.text.split('</li>')
    ## for stop
    ok = 1
    ## analyze all pieces
    for i in range(len(prova_1)):
        ## check if have finished and if contain </ul> -> finish
        if ok and not prova_1[i].__contains__('</ul>'):
            ## save all
            with open('sentenc.txt','a') as f:
                f.write(prova_1[i][prova_1[i].find('</a>:</b>') + 10:prova_1[i].find('(<')].replace('<i>', '').replace('</i>','') + str('\n'))
                num += 1
        else:
            ok=0
