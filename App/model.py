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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
from datetime import datetime
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

                "intervalos-generos": om.newMap(omaptype= "RBT"),

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

    dic2 = catalog["intervalos-generos"]
    om.put(dic2, 60, ("Reggae", "R&B"))
    om.put(dic2, 70, ("Reggae", "R&B", "Down-tempo"))
    om.put(dic2, 80, ("Reggae", "R&B", "Down-tempo"))
    om.put(dic2, 90, ("Reggae", "Down-tempo", "Chill-out", "Hip-hop"))
    om.put(dic2, 100, ("Down-tempo", "Chill-out", "Hip-hop", "Pop", "Metal"))
    om.put(dic2, 110, ("Chill-out", "Hip-hop", "Pop", "Metal", "Rock"))
    om.put(dic2, 120, ("Chill-out", "Pop", "Metal", "Rock", "Jazz and Funk"))
    om.put(dic2, 130, ("Pop", "Metal", "Rock"))
    om.put(dic2, 140, ("Metal", "Rock"))
    om.put(dic2, 150, ("Metal"))
    om.put(dic2, 160, ("Metal"))

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
    fecha = Track["created_at"]
    hashtag = Track["hashtag"]

    dic = catalog["track_id"]

    entry = mp.get(dic, track_id)

    if entry != None:
        referencias = me.getValue(entry)

        canciones = catalog["lista_canciones"]

        pos = 1
        while pos <= lt.size(referencias):
            referencia = lt.getElement(referencias, pos)
            cancion = lt.getElement(canciones, referencia)
            
            if fecha == cancion["created_at"]:
                cancion["hashtag"] = hashtag
                pos = lt.size(referencias) + 1

            else: pos += 1
    
    else: pass

def cargarSentiment (catalog, hashtag):
    mapa = catalog["hashtags"]
    Hashtag = hashtag["hashtag"]
    promedio = hashtag["vader_avg"]

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
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        track_id = dic["track_id"]
        mp.put(catalog["track_id"], track_id, lt.newList(datastructure="SINGLE_LINKED"))
        entry = mp.get(od, track_id)
        lista = me.getValue(entry)
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
    presencia = om.contains(od, dic["created_at"])

    if presencia:
        entry = om.get(od, dic["created_at"])
        lista = me.getValue(entry)
        lt.addLast(lista, pos) 
    else:
        created_at = dic["created_at"]
        om.put(catalog["created_at"], created_at, lt.newList(datastructure="SINGLE_LINKED"))
        entry = om.get(od, created_at)
        lista = me.getValue(entry)
        lt.addLast(lista, pos)    
    


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
