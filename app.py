from flask import Flask, render_template, request, redirect, flash, url_for
from controllers.download import  descargaMp3
from controllers.validarURL import getFormatosSearchID, getFormatosSearchText, validarURL


	
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 

@app.get("/")
def home():
    return render_template('base/base.html')

@app.get("/video")
def video():
    
    detailSearch = request.args.get("detailSearch")

    if  detailSearch.rfind('youtube.com/watch')>0:
        if(validarURL(detailSearch)==200):
            #print('linea 21')
            dataSearch = getFormatosSearchID(detailSearch)
            return render_template('detalleVideo.html',dataSearch=dataSearch)
        
        else:
            flash('Este vídeo ya no está disponible ')
            print('No encontrado')
            return render_template('base/base.html')
    else:
        #print('busqueda detalle')
        dataSearch = getFormatosSearchText(detailSearch)
        return render_template('resultados.html',dataSearch = dataSearch)



@app.get("/detalle")
def infoVideo():
    return render_template('resultados.html')


@app.get("/info-descarga")
def detailVideo():
    detailSearch = request.args.get("detailSearch")
    detailSearch = 'https://www.youtube.com/watch?v='+detailSearch
    #print('jeisonnnnnnnnn')
    #print(detailSearch)
    dataSearch = getFormatosSearchID(detailSearch)
    #print(dataSearch)
    return render_template('detalleVideo.html',dataSearch=dataSearch)


@app.get("/key-download")
def succsess():
    data= request.args.to_dict()
  
    return descargaMp3(data)


'''def busqueda(id):
    detailSearch=[]
    api_key = 'AIzaSyDr2LafAtuqd2ftGGykRfuLVOiguq4-rn0'
    youtube = build('youtube', 'v3', developerKey=api_key)
    req = youtube.search().list(part='snippet',
                            q=id,
                            type='video',
                            maxResults=2)
    res = req.execute()
    #print(res['items'])
    for item in res['items']:
        #print(cont, len(res['items']))
        
        
        #print(item['id']['videoId'])
        detailVideo = {
            'id'    :   item['id']['videoId'],
            'info':
                {
                    'title'      :  item['snippet']['title'],
                    'thumbnail'  :  item['snippet']['thumbnails']['high']['url'],
                    'description':  item['snippet']['description']
                }
        }
        detailSearch.append(detailVideo)
        
        
        #print(busqueda)
        #return busqueda
    return detailSearch
#data=busqueda('LUIS ENRIQUE - Yo No Se Mañana')
'''
""" for item in data:
    print(item['id']) """
#print(busqueda)
""" print(len(data))
print(data[0]['id']) """

app.run(
        debug=True,
        host='localhost',
        port=5000
        )