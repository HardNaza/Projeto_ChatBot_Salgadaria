# CÓDIGO ONDE É REALIZADA A CONSULTA DA DISTANCIA ENTRE ORIGEM E DESTINO UTILIZANDO O GOOGLE MAPS
# NECESSITA DE CRIAÇÃO DA API DO GOOGLE MAPS, SERÁ COBRADO UM VALOR PARA ISSO
import requests

def obter_distancia(endereco_origem, endereco_destino):
    # Obter as coordenadas de latitude e longitude para os endereços
    params = {
        'key': 'Chave_API_google_maps',
        'address': endereco_origem
    }
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)
    data = response.json()
    coordenadas_origem = data['results'][0]['geometry']['location']

    params['address'] = endereco_destino
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)
    data = response.json()
    coordenadas_destino = data['results'][0]['geometry']['location']

    # Obter as direções e a distância entre as coordenadas
    params = {
        'key': 'Chave_API_google_maps',
        'origin': f"{coordenadas_origem['lat']},{coordenadas_origem['lng']}",
        'destination': f"{coordenadas_destino['lat']},{coordenadas_destino['lng']}"
    }
    response = requests.get('https://maps.googleapis.com/maps/api/directions/json', params=params)
    data = response.json()
    distancia = data['routes'][0]['legs'][0]['distance']['text']

    return distancia

# Exemplo de uso
endereco_origem = 'Av. Paulista, 123, São Paulo, SP'
endereco_destino = 'Rua Augusta, 456, São Paulo, SP'

distancia = obter_distancia(endereco_origem, endereco_destino)
print(f"A distância entre os endereços é: {distancia}")