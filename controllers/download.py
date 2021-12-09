from controllers.validarURL import limpiarURL
from flask import jsonify
import requests

from models.downloading import redirecrDownloand, titleVideo
def validarURL(id):
    
    oembed="https://www.youtube.com/oembed?format=json&url="
    r = requests.get(oembed+"https://www.youtube.com/watch?v="+id)
    return r.status_code

def descargaMp3(request):
    detailSearch=request['detailSearch']
    format = request['key-id']
    ext= request['key-ext']
    if(validarURL(detailSearch)==200):
        return jsonify(
            {
                'estado':'200',
                'url': redirecrDownloand(
                    detailSearch,
                    format,
                    ext
                           ),
                'title':titleVideo(detailSearch)
            }) 
    else:
        return jsonify(
            {
                'estado':'400',
                'url': 'url no corecta'
            })   
            