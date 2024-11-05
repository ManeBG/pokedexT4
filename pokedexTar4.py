import requests
import os
import json

# verifica o rea la carpeta 'pokedex' si no existe
if not os.path.exists("pokedex"):
    os.makedirs("pokedex")


# Realiza la petición a la API con el nombre del Pokémon
def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)
    
    # Verifica si el Pokémon existe
    if response.status_code != 200:
        print("Error: Pokémon no encontrado. Verifica el nombre.")
        return None

    return response.json()


# Extrae la información clave del Pokémon
def procesar_datos_pokemon(datos):
    return {
        "nombre": datos["name"].capitalize(),
        "peso": datos["weight"],
        "altura": datos["height"],
        "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
        "habilidades": [habilidad["ability"]["name"] for habilidad in datos["abilities"]],
        "movimientos": [movimiento["move"]["name"] for movimiento in datos["moves"]],
        "imagen": datos["sprites"]["front_default"]
    }


# Guarda la información del Pokémon en un archivo JSON
def guardar_datos_pokemon(pokemon_info):
    nombre_archivo = f"pokedex/{pokemon_info['nombre'].lower()}.json"
    with open(nombre_archivo, "w") as archivo:
        json.dump(pokemon_info, archivo, indent=4)
    
    print(f"Información de {pokemon_info['nombre']} guardada en {nombre_archivo}.")

def pokedex():
    while True:
        nombre_pokemon = input("Introduce el nombre del Pokémon: ")
        
        datos = obtener_datos_pokemon(nombre_pokemon)
        
        if datos:
            pokemon_info = procesar_datos_pokemon(datos)
            guardar_datos_pokemon(pokemon_info)
            
            print("Información del Pokémon:")
            print(f"Nombre: {pokemon_info['nombre']}")
            print(f"Peso: {pokemon_info['peso']} hectogramos")
            print(f"Altura: {pokemon_info['altura']} decímetros")
            print(f"Tipos: {', '.join(pokemon_info['tipos'])}")
            print(f"Habilidades: {', '.join(pokemon_info['habilidades'])}")
            print(f"Movimientos: {', '.join(pokemon_info['movimientos'][:5])}...")  # Muestra solo los primeros 5 movimientos
            print(f"Imagen: {pokemon_info['imagen']}")
            break
        else:
            print("Por favor, intenta nuevamente.\n")

if __name__ == "__main__":
    pokedex()
