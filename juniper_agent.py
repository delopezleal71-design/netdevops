import json

def auditar_juniper():
    # 1. Simulación de la respuesta JSON nativa de Juniper (JunOS REST API)
    json_crudo_juniper = """
    {
        "configuration": {
            "interfaces": {
                "interface": [
                    {"name": "ge-0/0/0", "description": "Uplink", "disable": null},
                    {"name": "ge-0/0/1", "description": "Client", "disable": "disable"}
                ]
            }
        }
    }
    """
    
    # 2. Convertimos el texto a diccionario de Python
    datos = json.loads(json_crudo_juniper)
    
    # 3. Extraemos la lista de interfaces según la jerarquía de Juniper
    lista_interfaces = datos["configuration"]["interfaces"]["interface"]
    
    datos_estandarizados = []
    
    # 4. Procesamos cada interfaz para homogeneizar el resultado
    for interface in lista_interfaces:
        # En Juniper determinamos el estado operativo evaluando si existe la llave "disable"
        if interface.get("disable") is not None:
            estado_unificado = "down"
        else:
            estado_unificado = "up"
            
        registro = {
            "fabricante": "Juniper",
            "interfaz": interface["name"],
            "estado": estado_unificado
        }
        datos_estandarizados.append(registro)
        
    return datos_estandarizados