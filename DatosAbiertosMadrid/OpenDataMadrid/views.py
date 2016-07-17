from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime
import csv
from pymongo import MongoClient

# Create your views here.
client = MongoClient()
db = client.test
sugerencias = db.sugerencias
headers_c = db.headers

def search(request):
    headers = []
    count = 0
    doc = sugerencias.find_one()
    # for key in doc:
    #     if (key =="_id"):
    #         pass
    #     else:
    #         count = count + 1
    #         headers_c.insert_one({"key":key})
    for h in headers_c.find():
        headers.append(h["key"])
    keyword = request.GET.get('search_query', '')
    # length = len(q_attr)
    # attr = q_attr[0]
    # keyword = str(q_attr[1:length])
    docSugerencias = list(sugerencias.find({'$text':{'$search': keyword}}))
    return render_to_response('search.html',{
            'headers_list':headers,
            'year':datetime.now().year,
            'list':docSugerencias
    })
def home(request):
    """Renders the home page."""
    headers = []
    count = 0
    doc = sugerencias.find_one()
    for key in doc:
        if (key =="_id"):
            pass
        else:
            headers.append(key)
    docSugerencias = list(sugerencias.find({},{"_id":0}))
    # csvfile =  open('C:/Users/luisdeolpy/Documents/Python Scripts/DatosAbiertosMadrid/OpenDataMadrid/OD_SYRT_RECIBIDAS.csv', 'rt', encoding='latin-1')
    # spamreader = csv.reader(csvfile, delimiter=';')
    # headers = next(spamreader,None)
    # for row in spamreader:
    #     sugerencias.insert_one({"FECHA_PRES":row[0],
    #                             "HORA_PRES":row[1],
    #                             "NUMFIRMAS":row[2],
    #                             "ID_TIPOCANALENTRADA":row[3],
    #                             "DESC_TIPOCANALENTRADA":row[4],
    #                             "ID_CANALENTRADA":row[5],
    #                             "DESC_CANALENTRADA":row[6],
    #                             "ID_TIPOSOLICITUD":row[7],
    #                             "DESC_TIPOSOLICITUD":row[8],
    #                             "ID_PROCEDIMIENTO":row[9],
    #                             "DESC_PROCEDIMIENTO":row[10],
    #                             "ID_MATERIA":row[11],
    #                             "DESC_MATERIA_COMPLETO":row[12],
    #                             "ID_SUBMATERIA":row[13],
    #                             "DESC_SUBMATERIA_COMPLETO":row[14],
    #                             "ID_ESTADO":row[15],
    #                             "DESC_ESTADO":row[16],
    #                             "NUMEXPEDIENTE":row[17]})
    #     row_list.append(row)
    return render_to_response('index.html',{
            'headers_list':headers,
            'year':datetime.now().year,
            'list':docSugerencias
    })