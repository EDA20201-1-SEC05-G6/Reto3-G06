"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
from datetime import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initcatalog():

    catalog = {"lista_canciones": lt.newList("ARRAY_LIST"),

                "track_id": mp.newMap(
                                maptype= "PROBING",
                                loadfactor= 0.3),

                "instrumentalness": om.newMap(omaptype= "RBT"),

                "liveness": om.newMap(omaptype= "RBT"),

                "speechiness": om.newMap(omaptype= "RBT"),

                "danceability": om.newMap(omaptype= "RBT"),

                "valence": om.newMap(omaptype= "RBT"),

                "loudness": om.newMap(omaptype= "RBT"),

                "tempo": om.newMap(omaptype= "RBT"),

                "acousticness": om.newMap(omaptype= "RBT"),

                "energy": om.newMap(omaptype= "RBT"),

                "mode": om.newMap(omaptype= "RBT"),

                "key": om.newMap(omaptype= "RBT"),
                
                "created_at": om.newMap(omaptype= "RBT"),

                "generos-intervalos": mp.newMap(30,
                                        maptype= "PROBING",
                                        loadfactor= 0.3),

                "hashtags": mp.newMap(17634,
                                maptype= "PROBING",
                                loadfactor= 0.3),

                "artist_id": mp.newMap(maptype="PROBING", 
                                loadfactor=0.3)
                }
    
    dic1 = catalog["generos-intervalos"]

    mp.put(dic1, "Reggae", (60, 90))
    mp.put(dic1, "Down-tempo", (70, 100))
    mp.put(dic1, "Chill-out", (90, 120))
    mp.put(dic1, "Hip-hop", (85, 115))
    mp.put(dic1, "Jazz and Funk", (120, 125))
    mp.put(dic1, "Pop", (100, 130))
    mp.put(dic1, "R&B", (60, 80))
    mp.put(dic1, "Rock", (110, 140))
    mp.put(dic1, "Metal", (100, 160))

    return catalog

# Funciones para agregar informacion al catalogo

def addCancion(track, catalog):

    dic = {}
    dic["instrumentalness"] = float(track["instrumentalness"])
    dic["liveness"] = float(track["liveness"])
    dic["speechiness"] = float(track["speechiness"])
    dic["danceability"] = float(track["danceability"])
    dic["valence"] = float(track["valence"])
    dic["loudness"] = float(track["loudness"])
    dic["tempo"] = float(track["tempo"])
    dic["acousticness"] = float(track["acousticness"])
    dic["energy"] = float(track["energy"])
    dic["mode"] = float(track["mode"])
    dic["key"] = float(track["key"])
    dic["artist_id"] = track["artist_id"]
    dic["tweet_lang"] = track["tweet_lang"]
    dic["track_id"] = track["track_id"]
    dic["created_at"] = track["created_at"]
    dic["lang"] = track["lang"]
    dic["time_zone"] = track["time_zone"]
    dic["user_id"] = float(track["liveness"])
    dic["id"] = float(track["liveness"])

    lt.addLast(catalog["lista_canciones"], dic)

    pos = lt.size(catalog["lista_canciones"])

    addinstrumentalness(dic, catalog, pos)
    addliveness(dic, catalog, pos)
    addspeechiness(dic, catalog, pos)
    adddanceability(dic, catalog, pos)
    addvalence(dic, catalog, pos)
    addloudness(dic, catalog, pos)
    addtempo(dic, catalog, pos)
    addacousticness(dic, catalog, pos)
    addenergy(dic, catalog, pos)
    addmode(dic, catalog, pos)
    addkey(dic, catalog, pos)
    addtrack_id(dic, catalog, pos)
    addcreated_at(dic, catalog, pos)
    addartist_id(dic, catalog, pos)

def agregarHashtag (catalog, Track):
    track_id = Track["track_id"]
    hashtag = Track["hashtag"]

    dic = catalog["track_id"]

    entry = mp.get(dic, track_id)
    entry2 = mp.get(catalog["hashtags"], hashtag)

    if entry != None and entry2 != None:
        hashtags = me.getValue(entry)[1]
        mp.put(hashtags, hashtag, None)

def cargarSentiment (catalog, hashtag):
    mapa = catalog["hashtags"]
    Hashtag = hashtag["hashtag"]

    if hashtag["vader_avg"] != "":
        promedio = float(hashtag["vader_avg"])
        mp.put(mapa, Hashtag, promedio)

# Funciones para creacion de datos

def addinstrumentalness(dic, catalog, pos):

    od = catalog["instrumentalness"]
    presencia = om.contains(od, dic["instrumentalness"])

    if presencia:
        entry = om.get(od, dic["instrumentalness"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        instrumentalness = dic["instrumentalness"]
        om.put(catalog["instrumentalness"], instrumentalness, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, instrumentalness)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addliveness(dic, catalog, pos):

    od = catalog["liveness"]
    presencia = om.contains(od, dic["liveness"])

    if presencia:
        entry = om.get(od, dic["liveness"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        liveness = dic["liveness"]
        om.put(catalog["liveness"], liveness, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, liveness)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addspeechiness(dic, catalog, pos):

    od = catalog["speechiness"]
    presencia = om.contains(od, dic["speechiness"])

    if presencia:
        entry = om.get(od, dic["speechiness"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        speechiness = dic["speechiness"]
        om.put(catalog["speechiness"], speechiness, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, speechiness)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)
    

def adddanceability(dic, catalog, pos):

    od = catalog["danceability"]
    presencia = om.contains(od, dic["danceability"])

    if presencia:
        entry = om.get(od, dic["danceability"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        danceability = dic["danceability"]
        om.put(catalog["danceability"], danceability, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, danceability)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addvalence(dic, catalog, pos):

    od = catalog["valence"]
    presencia = om.contains(od, dic["valence"])

    if presencia:
        entry = om.get(od, dic["valence"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        valence = dic["valence"]
        om.put(catalog["valence"], valence, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, valence)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addloudness(dic, catalog, pos):

    od = catalog["loudness"]
    presencia = om.contains(od, dic["loudness"])

    if presencia:
        entry = om.get(od, dic["loudness"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        loudness = dic["loudness"]
        om.put(catalog["loudness"], loudness, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, loudness)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)


def addtempo(dic, catalog, pos):

    od = catalog["tempo"]
    presencia = om.contains(od, dic["tempo"])

    if presencia:
        entry = om.get(od, dic["tempo"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        tempo = dic["tempo"]
        om.put(catalog["tempo"], tempo, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, tempo)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addacousticness(dic, catalog, pos):

    od = catalog["acousticness"]
    presencia = om.contains(od, dic["acousticness"])

    if presencia:
        entry = om.get(od, dic["acousticness"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        acousticness = dic["acousticness"]
        om.put(catalog["acousticness"], acousticness, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, acousticness)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addenergy(dic, catalog, pos):

    od = catalog["energy"]
    presencia = om.contains(od, dic["energy"])

    if presencia:
        entry = om.get(od, dic["energy"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        energy = dic["energy"]
        om.put(catalog["energy"], energy, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, energy)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addmode(dic, catalog, pos):

    od = catalog["mode"]
    presencia = om.contains(od, dic["mode"])

    if presencia:
        entry = om.get(od, dic["mode"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        mode = dic["mode"]
        om.put(catalog["mode"], mode, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, mode)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)
    
def addkey(dic, catalog, pos):

    od = catalog["key"]
    presencia = om.contains(od, dic["key"])

    if presencia:
        entry = om.get(od, dic["key"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        key = dic["key"]
        om.put(catalog["key"], key, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, key)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addtrack_id(dic, catalog, pos):

    od = catalog["track_id"]
    presencia = mp.contains(od, dic["track_id"])

    if presencia:
        entry = mp.get(od, dic["track_id"])
        lista = me.getValue(entry)[0]
        lt.addLast(lista, pos) 
    else:
        track_id = dic["track_id"]
        mp.put(catalog["track_id"], track_id, (lt.newList(datastructure="SINGLE_LINKED"), mp.newMap(maptype="PROBING", loadfactor=0.3)))
        entry = mp.get(od, track_id)
        lista = me.getValue(entry)[0]
        lt.addLast(lista, pos)

def addartist_id(dic, catalog, pos):

    od = catalog["artist_id"]
    presencia = mp.contains(od, dic["artist_id"])

    if presencia:
        entry = mp.get(od, dic["artist_id"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        artist_id = dic["artist_id"]
        mp.put(catalog["artist_id"], artist_id, lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(od, artist_id)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)

def addcreated_at(dic, catalog, pos):

    od = catalog["created_at"]
    fecha = dic["created_at"].split(" ")
    hora = fecha[1]
    hora1 = time.fromisoformat(hora)
    presencia = om.contains(od, hora1)


    if presencia:
        entry = om.get(od, hora1)
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        created_at = hora1
        om.put(catalog["created_at"], created_at, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, created_at)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)    
    


# Funciones de consulta

def req1(caracteristica, catalog, min, max):

    artistas = mp.newMap(maptype= "PROBING", loadfactor= 0.3)
    canciones = mp.newMap(maptype= "PROBING", loadfactor= 0.3)
    numEventos = 0

    llaves = om.keys(catalog[caracteristica], min, max)

    for llave in lt.iterator(llaves):

        entry = om.get(catalog[caracteristica], llave)
        eventos = me.getValue(entry)

        for evento in lt.iterator(eventos):

            
            numEventos += 1

            track = lt.getElement(catalog["lista_canciones"], evento)
            mp.put(artistas, track["artist_id"], None)
            mp.put(canciones, track["track_id"], None)

    return (numEventos, mp.size(artistas), mp.size(canciones))

def req2(catalog, minEnergy, maxEnergy, minDanceability, maxDanceability):

    canciones = mp.newMap(maptype= "PROBING", loadfactor= 0.3)

    rangoEnergy = maxEnergy - minEnergy
    rangoDanceability = maxDanceability - minDanceability

    if rangoEnergy <= rangoDanceability:

        categoria =  "energy"   
        categoria1 = "danceability"
        min = minDanceability
        max = maxDanceability    
        llaves = om.keys(catalog["energy"], minEnergy, maxEnergy)

    else:
        
        categoria =  "danceability"
        categoria1 = "energy"
        min = minEnergy
        max = maxEnergy
        llaves = om.keys(catalog["danceability"], minDanceability, maxDanceability)


    for llave in lt.iterator(llaves):

        entry = om.get(catalog[categoria], llave)
        eventos = me.getValue(entry)

        for evento in lt.iterator(eventos):

            track = lt.getElement(catalog["lista_canciones"], evento)

            category = track[categoria1]

            if category >= min and category <= max:

                mp.put(canciones, track["track_id"], track)

    return canciones

def req3(catalog, minInstrumentalness, maxInstrumentalness, minTempo, maxTempo):

    canciones = mp.newMap(maptype= "PROBING", loadfactor= 0.3)

    rangoInstrumentalness = maxInstrumentalness - minInstrumentalness
    rangoTempo = maxTempo - minTempo

    if rangoTempo <= rangoInstrumentalness:

        categoria =  "tempo"   
        categoria1 = "instrumentalness"
        min = minInstrumentalness
        max = maxInstrumentalness    
        llaves = om.keys(catalog["tempo"], minTempo, maxTempo)

    else:
        
        categoria =  "instrumentalness"
        categoria1 = "tempo"
        min = minTempo
        max = maxTempo
        llaves = om.keys(catalog["instrumentalness"], minInstrumentalness, maxInstrumentalness)


    for llave in lt.iterator(llaves):

        entry = om.get(catalog[categoria], llave)
        eventos = me.getValue(entry)

        for evento in lt.iterator(eventos):

            track = lt.getElement(catalog["lista_canciones"], evento)

            category = track[categoria1]

            if category >= min and category <= max:

                mp.put(canciones, track["track_id"], track)

    return canciones

def req4(catalog, listaGeneros):

    numEventos = 0
    datos = lt.newList(datastructure= "SINGLE_LINKED")

    for genero in listaGeneros:

        numEventosGenero = 0
        artistas = mp.newMap(maptype= "CHAINING")

        entry = mp.get(catalog["generos-intervalos"], genero)

        nombre = me.getKey(entry)
        intervalo = me.getValue(entry)

        llaves = om.keys(catalog["tempo"], intervalo[0], intervalo[1])

        for llave in lt.iterator(llaves):

            entry = om.get(catalog["tempo"], llave)

            tracks = me.getValue(entry)

            for referencia in lt.iterator(tracks):

                track = lt.getElement(catalog["lista_canciones"], referencia)

                numEventos += 1
                numEventosGenero += 1
                mp.put(artistas, track["artist_id"], None)
        
        sizeArtistas = mp.size(artistas)
        top10 = lt.subList(mp.keySet(artistas), 1, 10)

            
        lt.addLast(datos, (nombre, numEventosGenero, sizeArtistas, top10))

    return (numEventos, datos)

def req5(catalog, minimo, maximo):

    dic = catalog["created_at"]
    llaves = om.keys(dic, minimo, maximo)
    global lista
    lista = catalog["lista_canciones"]
    generos = catalog["generos-intervalos"]
    llavesGeneros = mp.keySet(generos)
    
    mapaGeneros = mp.newMap(numelements=13, loadfactor=0.3, maptype="PROBING")

    for genero in lt.iterator(llavesGeneros):
        mp.put(mapaGeneros, genero, lt.newList(datastructure="SINGLE_LINKED"))

    for llave in lt.iterator(llaves):
        entry = om.get(dic, llave)
        referencias = me.getValue(entry)

        for referencia in lt.iterator(referencias):
            track = lt.getElement(lista, referencia)
            
            for genero in lt.iterator(llavesGeneros):
                entry = mp.get(generos, genero)
                intervalo = me.getValue(entry)

                if track["tempo"] >= intervalo[0] and track["tempo"] <= intervalo[1]:
                    entry = mp.get(mapaGeneros, genero)
                    listaGenero = me.getValue(entry)
                    lt.addLast(listaGenero, referencia)
                
    keys = mp.keySet(mapaGeneros)
    listaTuplas = lt.newList(datastructure="ARRAY_LIST")

    for key in lt.iterator(keys):
        entry = mp.get(mapaGeneros, key)
        Lst = me.getValue(entry)
        tupla = (key, lt.size(Lst))
        lt.addLast(listaTuplas, tupla)

    mergeSort(listaTuplas, cmpfunction)

    entry = mp.get(mapaGeneros, lt.firstElement(listaTuplas)[0])
    lst0 = me.getValue(entry)
    lst = lt.newList(datastructure="ARRAY_LIST")

    for elemento in lt.iterator(lst0):
        lt.addLast(lst, elemento)

    global TrackId
    TrackId = catalog["track_id"]
    
    eventosUnicos = mp.newMap(maptype="PROBING", loadfactor=0.3)

    for referencia in lt.iterator(lst):
        mp.put(eventosUnicos, lt.getElement(lista, referencia)["track_id"], None)

    mergeSort(lst, cmpfunction2)

    repetidos = lt.newList(datastructure="SINGLE_LINKED")
    contador = 0
    pos = 0
    tracksVader = lt.newList(datastructure="SINGLE_LINKED")

    while contador < 10 and pos <= lt.size(lst):
        referencia = lt.getElement(lst, pos)
        pos += 1
        track_id = lt.getElement(lista, referencia)["track_id"]

        if lt.isPresent(repetidos, track_id) == 0:
            lt.addLast(repetidos, track_id)

            entrada = mp.get(catalog["track_id"], track_id)
            mapa = me.getValue(entrada)[1]

            hashtagsTrack = mp.keySet(mapa)

            contadorHashtags = 0
            promedio = 0

            for hashtag in lt.iterator(hashtagsTrack):
                Entrada = mp.get(catalog["hashtags"], hashtag)
                if Entrada != None:
                    vader = me.getValue(Entrada)
                    contadorHashtags += 1
                    promedio += vader
        
            if promedio != 0:
                promedio /= contadorHashtags
                info = (track_id, contadorHashtags, promedio)
                lt.addLast(tracksVader, info)
                contador += 1

    return (listaTuplas, mp.size(eventosUnicos), tracksVader)

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpfunction(tupla1, tupla2):

    valor = None

    elemento1 = tupla1[1]
    elemento2 = tupla2[1]

    if elemento1 > elemento2:
        valor = True

    else:
        valor = False

    return valor

def cmpfunction2(pos1, pos2):
    
    valor = None

    id1 = lt.getElement(lista, pos1)["track_id"]
    id2 = lt.getElement(lista, pos2)["track_id"]

    entry1 = mp.get(TrackId, id1)
    valor1 = me.getValue(entry1)[1]
    elemento1 = mp.size(valor1)

    entry2 = mp.get(TrackId, id2)
    valor2 = me.getValue(entry2)[1]
    elemento2 = mp.size(valor2)

    if elemento1 > elemento2:
        valor = True

    else:
        valor = False

    return valor

# Funciones de ordenamiento
def mergeSort(lista, cmpfunction):

    mg.sort(lista, cmpfunction)