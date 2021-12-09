from  youtube_dl import YoutubeDL



#youtube-dl --get-duration "https://www.youtube.com/watch?v=cRWr4VNqIjY"
def getFormatosSearchText(url):
    videoIfo = {}
    detailSearch=[]
    
    with YoutubeDL(videoIfo) as ydl:
        meta = ydl.extract_info(
            f"ytsearch10:{url}", download=False) 
        #print('jeison')
        
    #print(type(meta))
  
    for item in meta['entries']:
        tmThumbnails =len(item['thumbnails'])-1
        #print(item['duration'])
        videoIfo={
            'id':item['id'],
            'title':(item['title'][:40])+"....",
            'thumbnail':item['thumbnails'][tmThumbnails]['url'],
            'description': (item['description'][:100])
        }
        detailSearch.append(videoIfo)
        
        #print(detailSearch)
    
    return detailSearch


def getFormatosSearchID(url):
    videoIfo = {}
    detailSearch=[]
    videoCalidad = {}
    mp3=[]
    mp4=[]

    with YoutubeDL(videoIfo) as ydl:
        meta = ydl.extract_info(
            f"https://www.youtube.com/watch?v={url}", download=False) 
    #print(type(meta))
    tmThumbnails =len(meta['thumbnails'])-1
    idVideo= meta['id']
    videoIfo={
        'id':idVideo,
        'title':meta['title'],
        'thumbnails':meta['thumbnails'][tmThumbnails]['url']
    }
    
    
    #print(convert_bytes((meta['formats'][0]['filesize'])))
    
    #detailSearch.append(videoIfo)
    #print(meta['formats'])
    for formato in meta['formats']:
        if (formato['filesize']!=None):
            if(formato['format_note']=='tiny'):
                #print(formato['filesize'])
                mp3.append({
                    'format_id':formato['format_id'],
                    'format_ext':formato['ext'],
                    'format_tam':formato['filesize'],
                    'format_note':formato['format_note']
                })
            else:
                mp4.append({
                    'format_id':formato['format_id'],
                    'format_ext':formato['ext'],
                    'format_tam':formato['filesize'],
                    'format_note':formato['format_note'],
                })
        """ videoIfo={
            
            'format_id':formato['format_id'],
            'format_note':formato['format_note']
        }"""
    

    detailSearch.append(videoIfo) 
    detailSearch.append(mp3)
    detailSearch.append(mp4)
    
       
    #print(detailSearch)
       
    
    return detailSearch
#getFormatosSearchID('3YqPKLZF_WU')