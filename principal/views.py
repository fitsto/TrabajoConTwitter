# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse
#from django.shortcuts import render_to_response
from twython import Twython


def listUrl(request):
    twitter = Twython()
    listaTwitter = []
    contador = 0
    for page in range(1, 4):

        user_timeline = twitter.getUserTimeline(screen_name="cvander", count="200", page=page, include_entities = "true")
        for t in user_timeline:
            if t['text'].find("http") >= 0:
                if contador > 0:
                    contadorIgualdad = 0
                    for posicion in range(0, len(listaTwitter)):
                        if listaTwitter[posicion]['url'] == t['entities']['urls'][0]['expanded_url']:
                            contadorIgualdad += 1
                            auxPosicion = posicion

                    if contadorIgualdad > 0:
                        listaTwitter[auxPosicion]['retwits'] += t['retweet_count']
                    else:
                        listaTwitter.append({
                            'retwits': t['retweet_count'],
                            'url': t['entities']['urls'][0]['expanded_url']})
                else:
                    listaTwitter.append({
                        'retwits': t['retweet_count'],
                        'url': t['entities']['urls'][0]['expanded_url']})
                    contador += 1

        user_timeline2 = twitter.getUserTimeline(screen_name="freddier", count="200", page=page, include_entities = "true")
        for t2 in user_timeline2:
            if t2['text'].find("http") >= 0:
                if contador > 0:
                    contadorIgualdad = 0
                    for posicion in range(0, len(listaTwitter)):
                        if listaTwitter[posicion]['url'] == t2['entities']['urls'][0]['expanded_url']:
                            contadorIgualdad += 1
                            auxPosicion = posicion

                    if contadorIgualdad > 0:
                        listaTwitter[auxPosicion]['retwits'] += t2['retweet_count']
                    else:
                        listaTwitter.append({
                            'retwits': t2['retweet_count'],
                            'url': t2['entities']['urls'][0]['expanded_url']})
                else:
                    listaTwitter.append({
                        'retwits': t2['retweet_count'],
                        'url': t2['entities']['urls'][0]['expanded_url']})
                    contador += 1
    listaOrdenada = quicksort(listaTwitter, 0, len(listaTwitter) - 1, 'desc')
    #assert False
    t = get_template('lista_url.html')
    c = RequestContext(request, {'twits': listaOrdenada})
    html = t.render(c)
    return HttpResponse(html)


def quicksort(datos, primero, ultimo, ordenacion='asc'):
    i = primero
    j = ultimo
    posicion_pivote = (primero + ultimo) / 2
    pivote = datos[posicion_pivote]
    while i <= j:
        if ordenacion == 'asc':
            while datos[i] < pivote:
                i += 1
            while datos[j] > pivote:
                j -= 1
        if ordenacion == 'desc':
            while datos[i] > pivote:
                i += 1
            while datos[j] < pivote:
                j -= 1
        if i <= j:
            aux = datos[i]
            datos[i] = datos[j]
            datos[j] = aux
            i += 1
            j -= 1
    if primero < j:
        datos = quicksort(datos, primero, j, ordenacion)
    if ultimo > i:
        datos = quicksort(datos, i, ultimo, ordenacion)
    return datos


def verTwitter(request):
    twitter = Twython()
    recorretwiter = []
    for page in range(1, 4):
        user_timeline = twitter.getUserTimeline(screen_name="cvander", count="200", page=page, include_entities = "true")
        for t in user_timeline:
            if t['text'].find("http") >= 0:
                recorretwiter.append({
                    'text': t['text'],
                    'user': "cvander",
                    'retwits': t['retweet_count'],
                    'url': t['entities']['urls'][0]['expanded_url'],
                    'fecha': t['created_at']})
        user_timeline2 = twitter.getUserTimeline(screen_name="freddier", count="200", page=page, include_entities = "true")
        for t2 in user_timeline2:
            if t2['text'].find("http") >= 0:
                recorretwiter.append({
                    'text': t2['text'],
                    'user': "freddier",
                    'retwits': t2['retweet_count'],
                    'url': t2['entities']['urls'][0]['expanded_url'],
                    'fecha': t2['created_at']})

    t = get_template('twitter.html')
    c = RequestContext(request, {'user_timeline': recorretwiter})
    html = t.render(c)
    return HttpResponse(html)
