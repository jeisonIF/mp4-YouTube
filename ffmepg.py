from  youtube_dl import YoutubeDL
from ffmpeg import video 

""" iconMP3 = '<i class="fa fa-music" aria-hidden="true"></i>'
iconMP4 = '<i class="fa fa-video-camera" aria-hidden="true"></i>'
def convert_bytes(size):
    #print(size)
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size
def ordenarMP3(formato):
    print('ordenar')
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
        
            


a=
[
    {'id': 'OA9Uo76iD74', 'title': 'EL Joven | Que PIERDE EL CONTROL! | Hundred | RESUMEN! 🌀', 'thumbnails': 'https://i.ytimg.com/vi/OA9Uo76iD74/maxresdefault.jpg'}, [{'format_id': '249', 'format_ext': 'webm', 'format_tam': 4758584, 'format_note': 'tiny'}, {'format_id': '250', 'format_ext': 'webm', 'format_tam': 6331112, 'format_note': 'tiny'}, {'format_id': '140', 'format_ext': 'm4a', 'format_tam': 12133898, 'format_note': 'tiny'}, {'format_id': '251', 'format_ext': 'webm', 'format_tam': 12189108, 'format_note': 'tiny'}], [{'format_id': '160', 'format_ext': 'mp4', 'format_tam': 4519842, 'format_note': '144p'}, {'format_id': '394', 'format_ext': 'mp4', 'format_tam': 5741956, 'format_note': '144p'}, {'format_id': '278', 'format_ext': 'webm', 'format_tam': 6387660, 'format_note': '144p'}, {'format_id': '133', 'format_ext': 'mp4', 'format_tam': 8870963, 'format_note': '240p'}, {'format_id': '395', 'format_ext': 'mp4', 'format_tam': 8938213, 'format_note': '240p'}, {'format_id': '242', 'format_ext': 'webm', 'format_tam': 10713938, 'format_note': '240p'}, {'format_id': '134', 'format_ext': 'mp4', 'format_tam': 15513869, 'format_note': '360p'}, {'format_id': '396', 'format_ext': 'mp4', 'format_tam': 15711924, 'format_note': '360p'}, {'format_id': '243', 'format_ext': 'webm', 'format_tam': 20479822, 'format_note': '360p'}, {'format_id': '135', 'format_ext': 'mp4', 'format_tam': 24488269, 'format_note': '480p'}, {'format_id': '397', 'format_ext': 'mp4', 'format_tam': 26201021, 'format_note': '480p'}, {'format_id': '244', 'format_ext': 'webm', 'format_tam': 32956314, 'format_note': '480p'}, {'format_id': '136', 'format_ext': 'mp4', 'format_tam': 41440286, 'format_note': '720p'}, {'format_id': '398', 'format_ext': 'mp4', 'format_tam': 50697812, 'format_note': '720p'}, {'format_id': '247', 'format_ext': 'webm', 'format_tam': 56321410, 'format_note': '720p'}, {'format_id': '399', 'format_ext': 'mp4', 'format_tam': 89459072, 'format_note': '1080p'}, {'format_id': '248', 'format_ext': 'webm', 'format_tam': 95164781, 'format_note': '1080p'}, {'format_id': '137', 'format_ext': 'mp4', 'format_tam': 117216990, 'format_note': '1080p'}, {'format_id': '18', 'format_ext': 'mp4', 'format_tam': 41011264, 'format_note': '360p'}
]
]


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
 """

def download(url):
    """ with YoutubeDL({'format':'251','outtmpl': '/%(title)s.mp3',}) as ydl:
            ydl.download([url]) """
    with YoutubeDL({'format':'[height=720]','outtmpl': '/%(title)s.mp4',}) as ydl:
            ydl.download([url])
                 
            
url= 'https://www.youtube.com/watch?v=OA9Uo76iD74'
download(url);
