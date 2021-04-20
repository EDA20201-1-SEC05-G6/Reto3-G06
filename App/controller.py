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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo

def loadCatalog(catalog):

    catalog = model.initcatalog()

    user_track_hashtag_timestamp_file = cf.data_dir + "user_track_hashtag_timestamp-small.csv"
    user_file = csv.DictReader(open(user_track_hashtag_timestamp_file, encoding="utf-8"),
                                delimiter=",")
    
    context_content_features_file = cf.data_dir + "context_content_features-small.csv"
    context_file = csv.DictReader(open(context_content_features_file, encoding="utf-8"),
                                delimiter=",")

    sentiment_values_file = cf.data_dir + "sentiment_values.csv"
    sentiment_file = csv.DictReader(open( sentiment_values_file, encoding="utf-8"),
                                delimiter=",")

    for track in context_file:

        model.addCancion(track, catalog)

    return catalog



    

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
