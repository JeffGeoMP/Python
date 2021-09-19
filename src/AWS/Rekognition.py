#Importacion de Libreria de AWS para Python
import boto3

#Importacion de Variables de .env
from decouple import config

#Libreria para manejo de Imagenes
import base64

Rekognition = boto3.client(
    'rekognition',
    aws_access_key_id = config('REK_ACCESS_KEY_ID'),
    aws_secret_access_key = config('REK_SECRET_ACCESS_KEY'),
    region_name = config('REK_REGION'),
)


def DetectLabels(Image64):
    Imagebytes = bytes(Image64, 'utf-8')
    Binary = base64.decodebytes(Imagebytes)
    
    resp = Rekognition.detect_labels(
        Image = {
            'Bytes': Binary
        },
        MaxLabels = 20
    )

    result = {}
    result['Resultados'] = []
    for label in resp['Labels']:
        result['Resultados'].append( {
            'Atributo': label['Name'],
            'Confianza' : str(label['Confidence'])
        })
    
    return result

    