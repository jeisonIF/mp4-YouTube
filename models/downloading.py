from  youtube_dl import YoutubeDL
import os
import re

    
def mp4Downloand(outtmpl,id,format):
    #print(outtmpl)
    ydl_opts = {
        'format': f'{format}+bestaudio',
        'postprocessors': [
            {
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],
        'outtmpl': f'./static/thumbnails/mp4/{outtmpl}.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([id])
        
    return f'./static/thumbnails/mp4/{outtmpl}.mp4'    

def mp3Downloand(outtmpl,id,format):
    #print('descarga mp3')
    ydl_opts = {
        'format': f'{format}',
        'postprocessors': [
            {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '190',
            },
            {
                'key': 'FFmpegMetadata',
            }
                           ],
        'outtmpl': f'./static/thumbnails/mp3/{outtmpl}.%(ext)s',
    }
    with YoutubeDL(ydl_opts) as ydl:
        descarga = ydl.download([id])
    #print(type(descarga))
    #a= 'jeison'
    
    #print(type(a))
    
    return f'./static/thumbnails/mp3/{outtmpl}.mp3'

def buscarArchivo(path,descarga):
    resultado =''
    print(f'descargas\n{descarga}')
    contenido = os.listdir(path)
    #print(len(contenido))
    for archivo in contenido:
        #print(f'carpeta\n{archivo}')
        if(archivo==descarga):
            print('Ya descargado')
            resultado = (f'{path}/{descarga}')
            
    return resultado
       
    #return archivo

    
def searchDownloand(id,title,format,ext):
#def searchDownloand(path,id,title,ext):
    path =f'./static/thumbnails/{ext}'
   
    if not os.path.exists(path):
        os.makedirs(path) 
    
    #descarga = f'{title}.{ext}'
    resultado = buscarArchivo(path,f'{title}.{ext}')
    bandera= False 
    #print(ext)
    if (resultado ==''):
        if(ext=='mp3'):
            print('formato mp3')
            resultado = mp3Downloand(title,id,format)
        else:
            resultado =  mp4Downloand(title,id,format)
            
    return resultado
                
    
def titleVideo(ID):
    videoIfo = {}
    with YoutubeDL(videoIfo) as ydl:
        meta = ydl.extract_info(
            f"https://www.youtube.com/watch?v={ID}", download=False) 
    return meta['title']


def redirecrDownloand(ID,format,ext):
    #print(ext)
    title = f'{titleVideo(ID)}({format})'
    ''' print(title)
    title = title.replace(" ","_")
    print(title) '''
    #title = re.sub('[^0-9A-Za-zÀ-ÿ\u00f1\u00d1()-.,-[]--+', ' ', title)
    title = re.sub('[|_?¿#]', ' ', title)
    '''   title = title.replace("|","_")
    title = title.replace("_"," ")
    title = title.replace("¿"," ")
    title = title.replace("?"," ") '''
    title = title.replace("  ","")
    
    
    print(ext)
    if(ext=='mp3'):
        return searchDownloand(ID,title,format,ext)
    else:
        return searchDownloand(ID,title,format,ext)
        