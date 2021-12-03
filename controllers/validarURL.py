import requests
import re
from models import getURL 


##r = requests.get("https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=ZqW8JT1gt4U")
#print (r)

iconMP3 = 'fa fa-music'
iconMP4 = 'fa fa-video-camera'
def convert_bytes(size):
    #print(size)
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size
def ordenarMP3(formato):
    #print('ordenar')
    aux=[]
    for f in formato:
        auxF={
            'format_id':f['format_id'],
            'format_ext':'MP3',
            'format_tam':convert_bytes(f['format_tam']),
            'format_icon':iconMP3
        }
        aux.append(auxF)
    return aux

def mayorMP4(formato):
    mayor={None}
    bandera = 0
    if (len(formato)>0):
        for f in formato:
            if(f['format_tam']>bandera):
                bandera=f['format_tam']
                mayor=f
        mayor['format_tam']=convert_bytes(mayor['format_tam'])
        mayor['format_icon']=iconMP4
        mayor['format_ext']='MP4'
    return mayor
      
def ordenarMP4(formato):
    aux=[]
    c_144p=[];      c_240p =[];     c_360p =[]
    c_480p =[];     c_720p =[];     c_1080p =[]
    c_1440p =[];    c_2160p =[];    c_4320p =[]
  
    for f in formato: 
        if (f['format_note'])=='144p':
            #print('144p2')
            c_144p.append(f)
        elif (f['format_note'])=='240p':
            c_240p.append(f)
        elif (f['format_note'])=='360p':
            c_360p.append(f)
        elif (f['format_note'])=='480p':
            c_480p.append(f)
        elif (f['format_note'])=='720p':
           c_720p.append(f)
        elif (f['format_note'])=='1080p':
            c_1080p.append(f)
        elif (f['format_note'])=='1440p':
                c_1440p.append(f)
        elif (f['format_note'])=='2160p':
            c_2160p.append(f)
        elif (f['format_note'])=='4320p':
            c_4320p.append(f)
    
    aux.append(mayorMP4(c_144p));   aux.append(mayorMP4(c_240p));   aux.append(mayorMP4(c_360p));   
    aux.append(mayorMP4(c_480p));   aux.append(mayorMP4(c_720p));   aux.append(mayorMP4(c_1080p));   
    aux.append(mayorMP4(c_1440p));   aux.append(mayorMP4(c_2160p));   aux.append(mayorMP4(c_4320p));   
    return aux
    #print(aux)
        
         
def limpiarURL(url):
    validar=url.split('watch?v=')
    validar=validar[1].split('&')
    return validar[0]

def validarURL(url):
    
    validar=limpiarURL(url)
    oembed="https://www.youtube.com/oembed?format=json&url="
    r = requests.get(oembed+"https://www.youtube.com/watch?v="+validar)
    return r.status_code

   
def getFormatosSearchText(url):
    return getURL.getFormatosSearchText(url)

def formatos(data):
    detalles =[]
    detalle =data[0]
    mp3=ordenarMP3(data[1])
    mp4=ordenarMP4(data[2])
    mp4Ax=[]
    for v in mp4:
        if(len(v)>1):
            mp4Ax.append(v)  
    detalles.append(detalle);
    detalles.append(mp3);
    detalles.append(mp4Ax);
    return detalles


def getFormatosSearchID(url):
    validar = limpiarURL(url)
    dataFormats=formatos(getURL.getFormatosSearchID(validar))
    
    return dataFormats