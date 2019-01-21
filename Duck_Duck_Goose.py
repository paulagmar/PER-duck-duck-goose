numero=int(input('Introduce un número: '))
nombres=['Laura','Ruben','Carla','Lorena','Ines','Carlos','Carol']

def duck_duck_goose(nombres,numero):
    if numero<len(nombres):
        print(nombres[numero], 'hola')
    else:
        return
    return

duck_duck_goose(nombres,numero)
