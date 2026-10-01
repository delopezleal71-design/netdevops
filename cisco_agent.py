import json

def auditar_cisco():
    # 1. Definimos una variable de texto que simula la respuesta JSON cruda de un equipo Cisco (RESTCONF)
    json_crudo_cisco = """
    {
        "ietf-interfaces:interfaces-state": {
            "interface": [
                {"name": "Loopback0", "oper-status": "up"},
                {"name": "GigabitEthernet1", "oper-status": "down"}
            ]
        }
    }
    """
    
    # 2. Convertimos esa cadena de texto plano en un diccionario/objeto de Python nativo
    datos = json.loads(json_crudo_cisco)
    
    # 3. Navegamos las llaves del diccionario para extraer únicamente la lista de interfaces
    lista_interfaces = datos["ietf-interfaces:interfaces-state"]["interface"]
    
    # 4. Creamos una lista vacía para almacenar los datos estandarizados
    datos_estandarizados = []
    
    # 5. Recorremos con un bucle 'for' cada interfaz de la lista original
    for interface in lista_interfaces:
        # Creamos un nuevo diccionario con una estructura limpia y homogénea
        registro = {
            "fabricante": "Cisco",
            "interfaz": interface["name"],
            "estado": interface["oper-status"]
        }
        # Agregamos este diccionario limpio a nuestra lista
        datos_estandarizados.append(registro)
        
    # 6. Devolvemos la lista final procesada. Quien llame a esta función recibirá esta lista.
    return datos_estandarizados