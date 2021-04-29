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
from datetime import time
import random
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
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
       
       caracteristica = input("Ingrese la característica de contenido que desea consultar -> ")
       min = float(input("Ingrese el extremo inferior del intervalo que desea consultar -> "))
       max = float(input("Ingrese el extremo superior del intervalo que desea consultar -> "))


       resultado = controller.req1(caracteristica, catalog, min, max)

       print("Numero de eventos de escucha encontrados: " + str(resultado[0]))
       print("Numero de artistas únicos encontrados: " + str(resultado[1]))
       print("Numero de canciones únicas encontradas: " + str(resultado[2]))

    elif int(inputs[0]) == 3:

        minEnergy = float(input("Ingrese el valor inferior del intervalo que desea consultar para la categoría de energy -> "))
        maxEnergy = float(input("Ingrese el valor superior del intervalo que desea consultar para la categoría de energy -> "))
        minDanceability = float(input("Ingrese el valor inferior del intervalo que desea consultar para la categoría de danceability -> "))
        maxDanceability = float(input("Ingrese el valor superior del intervalo que desea consultar para la categoría de danceability -> "))

        resultado = controller.req2(catalog, minEnergy, maxEnergy, minDanceability, maxDanceability)

        print("\nLa energía está entre " + str(minEnergy) + " y " + str(maxEnergy) + " y la bailabilidad está entre " + str(minDanceability) + " y " + str(maxDanceability))
        print("Total de pistas únicas encontradas: " + str(mp.size(resultado)))

        llaves = mp.keySet(resultado)

        for i in range(1,6):
            
            n = random.randint(1, mp.size(resultado))

            llave = lt.getElement(llaves, n)
            track = me.getValue(mp.get(resultado, llave))

            print("Track " + str(i))

            print(track["track_id"] + " con energía " + str(track["energy"]) + " y bailabilidad " + str(track["danceability"]))


    elif int(inputs[0]) == 4:

        minInstrumentalness = float(input("Ingrese el valor inferior del intervalo que desea consultar para la categoría de instrumentalness -> "))
        maxInstrumentalness = float(input("Ingrese el valor superior del intervalo que desea consultar para la categoría de instrumentalness -> "))
        minTempo = float(input("Ingrese el valor inferior del intervalo que desea consultar para la categoría de tempo -> "))
        maxTempo = float(input("Ingrese el valor superior del intervalo que desea consultar para la categoría de tempo -> "))
        
        output = controller.req3(catalog, minInstrumentalness, maxInstrumentalness, minTempo, maxTempo)

        print("\nLa instrumentalidad está entre " + str(minInstrumentalness) + " y " + str(maxInstrumentalness) + " y el tempo está entre " + str(minTempo) + " y " + str(maxTempo))
        print("Total de pistas únicas encontradas: " + str(mp.size(output)))

        llaves = mp.keySet(output)

        for i in range(1,6):
            
            n = random.randint(1, mp.size(output))

            llave = lt.getElement(llaves, n)
            track = me.getValue(mp.get(output, llave))

            print("Track " + str(i))

            print(track["track_id"] + " con instrumentalidad " + str(track["instrumentalness"]) + " y tempo " + str(track["tempo"]))

    elif int(inputs[0]) == 5:

        print("¿Desea incorporar un género personalizado en su busqueda? ")
        print("Si (1)")
        print("No (2)")

        opcion = input()

        if opcion == "1":

            nombreGenero = input("Ingrese el nombre de su nuevo género -> ")
            min = float(input("Ingrese el limite inferior del intervalo de tempo que corresponde a su nuevo género -> "))
            max = float(input("Ingrese el limite superior del intervalo de tempo que corresponde a su nuevo género -> "))

            mp.put(catalog["generos-intervalos"], nombreGenero, (min, max))

        generos = input("Ingrese los generos que desea consultar (separados por comas sin espacios) -> ")
        listaGeneros = generos.split(",")

        resultado = controller.req4(catalog, listaGeneros)

        print("Total de eventos de escucha cargados: " + str(resultado[0]))

        for elemento in lt.iterator(resultado[1]):

            print("Genero: " + elemento[0])
            tempo = me.getValue(mp.get(catalog["generos-intervalos"], elemento[0]))
            print("Tempo: " + str(tempo[0]) + " - " + str(tempo[1]))
            print("Numero de eventos de escucha para este genero: " + str(elemento[1])) 
            print("Numero de artistas únicos para este genero: " + str(elemento[2]))
            print("10 primeros artistas para este género: ")

            for artista in lt.iterator(elemento[3]):

                print(artista)

            print("\n")
        
    elif int(inputs[0]) == 6:
        minimo = time.fromisoformat(input("Ingrese el limite inferior del intervalo de tiempo que desea consultar->"))
        maximo = time.fromisoformat(input("Ingrese el limite superior del intervalo de tiempo que desea consultar->"))

        output = controller.req5(catalog, minimo, maximo)

        total = 0
        for tupla in lt.iterator(output[0]):
            total += tupla[1]

        print("\nEntre " + str(minimo) + " y " + str(maximo) + " hay un total de " + str(total) + " reproducciones.")
        print("\nTop Géneros\n")
        
        n = 0
        for tupla in lt.iterator(output[0]):
            n += 1
            print("Top " + str(n) + ": " + tupla[0] + " con " + str(tupla[1]) + " reproducciones.")

        print("\n" + lt.firstElement(output[0])[0] + " tiene " + str(output[1]) + " tracks únicos.")

        print("Top 10 tracks:")

        n = 0
        for tupla in lt.iterator(output[2]):
            n += 1
            print("Top " + str(n) + " track: " + tupla[0] + " con " + str(tupla[1]) + " hashtags " + " y VADER = " + str(tupla[2]))

    else:
        sys.exit(0)
sys.exit(0)

#REVISAR DISCREPANCIAS DE RESULTADOS REQ5 Y EJ