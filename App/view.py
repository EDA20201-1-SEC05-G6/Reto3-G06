"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Salir del programa")
    print("1- Cargar información en el catálogo")
    print("2- Consultar eventos de escucha por caracteristicas de contenido en un rango determinado")
    print("3- Consultar canciones por energía y bailabilidad en rangos determinados")
    print("4- Consultar canciones por por instrumentalidad y tiempo en rangos determinados")
    print("5- Consultar el número de canciones y artistas por género")
    print("6- Consultar el ranking de generos más escuchado en un rango de horas junto con sus respectivos valores de sentimiento.")



catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        catalog = controller.loadCatalog(catalog)
        print("Total de eventos de escucha: ", lt.size(catalog["lista_canciones"]))
        print("Total de artistas únicos: ", mp.size(catalog["artist_id"]))
        print("Total de pistas de audio únicas cargadas: ", mp.size(catalog["track_id"]))
        print("5 primeros:")
        for i in range(0, 5):
            dic = lt.getElement(catalog["lista_canciones"], i)
            print("track_id: " + dic["track_id"])
            print ("instrumentalness: " + str(dic["instrumentalness"]))
            print ("liveness: " + str(dic["liveness"]))
            print ("speechiness: " + str(dic["speechiness"]))
            print ("danceability: " + str(dic["danceability"]))
            print ("valence: " + str(dic["valence"]))
            print ("loudness: " + str(dic["loudness"]))
            print ("tempo:" + str(dic["tempo"]))
            print ("acousticness: " + str(dic["acousticness"]))
            print ("energy: " + str(dic["energy"]))
            print ("mode: " + str(dic["mode"]))
            print ("key: " + str(dic["key"]))
            print ("artist_id: " + dic["artist_id"])
            print ("tweet_lang: " + dic["tweet_lang"])
            print ("created_at: " + dic["created_at"])
            print ("lang: " + dic["lang"])
            print ("time_zone: " + dic["time_zone"])
            print ("user_id: " + str(dic["liveness"]))
            print ("id: " + str(dic["liveness"]) + "\n")
        
        print("5 últimos:")
        for i in range(lt.size(catalog["lista_canciones"]) - 4, lt.size(catalog["lista_canciones"]) + 1):
            dic = lt.getElement(catalog["lista_canciones"], i)
            print("track_id: " + dic["track_id"])
            print ("instrumentalness: " + str(dic["instrumentalness"]))
            print ("liveness: " + str(dic["liveness"]))
            print ("speechiness: " + str(dic["speechiness"]))
            print ("danceability: " + str(dic["danceability"]))
            print ("valence: " + str(dic["valence"]))
            print ("loudness: " + str(dic["loudness"]))
            print ("tempo:" + str(dic["tempo"]))
            print ("acousticness: " + str(dic["acousticness"]))
            print ("energy: " + str(dic["energy"]))
            print ("mode: " + str(dic["mode"]))
            print ("key: " + str(dic["key"]))
            print ("artist_id: " + dic["artist_id"])
            print ("tweet_lang: " + dic["tweet_lang"])
            print ("created_at: " + dic["created_at"])
            print ("lang: " + dic["lang"])
            print ("time_zone: " + dic["time_zone"])
            print ("user_id: " + str(dic["liveness"]))
            print ("id: " + str(dic["liveness"]) + "\n")

    elif int(inputs[0]) == 2:
        print("\ninstrumentalness: ")
        print("Altura: ", om.height(catalog["instrumentalness"]))
        print("Número de elementos: ", om.size(catalog["instrumentalness"]), "\n")
        
        print("liveness: ")
        print("Altura: ", om.height(catalog["liveness"]))
        print("Número de elementos: ", om.size(catalog["liveness"]), "\n")

        print("speechiness: ")
        print("Altura: ", om.height(catalog["speechiness"]))
        print("Número de elementos: ", om.size(catalog["speechiness"]), "\n")

        print("danceability: ")
        print("Altura: ", om.height(catalog["danceability"]))
        print("Número de elementos: ", om.size(catalog["danceability"]), "\n")

        print("valence: ")
        print("Altura: ", om.height(catalog["valence"]))
        print("Número de elementos: ", om.size(catalog["valence"]), "\n")

        print("loudness: ")
        print("Altura: ", om.height(catalog["loudness"]))
        print("Número de elementos: ", om.size(catalog["loudness"]), "\n")

        print("tempo: ")
        print("Altura: ", om.height(catalog["tempo"]))
        print("Número de elementos: ", om.size(catalog["tempo"]), "\n")

        print("acousticness: ")
        print("Altura: ", om.height(catalog["acousticness"]))
        print("Número de elementos: ", om.size(catalog["acousticness"]), "\n")

        print("energy: ")
        print("Altura: ", om.height(catalog["energy"]))
        print("Número de elementos: ", om.size(catalog["energy"]), "\n")

        print("mode: ")
        print("Altura: ", om.height(catalog["mode"]))
        print("Número de elementos: ", om.size(catalog["mode"]), "\n")

        print("key: ")
        print("Altura: ", om.height(catalog["key"]))
        print("Número de elementos: ", om.size(catalog["key"]), "\n")

    else:
        sys.exit(0)
sys.exit(0)
