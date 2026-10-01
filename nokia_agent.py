import json

def auditar_nokia():
    # 1. Simulación de la respuesta JSON nativa de Nokia (SR-OS RESTCONF)
    json_crudo_nokia = """
    {
        "nokia-conf:interface": [
            {"interface-name": "to-Lumen", "admin-state": "enable"},
            {"interface-name": "Test-Loop", "admin-state": "disable"}
        ]
    }
    """
    
    datos = json.loads(json_crudo_nokia)
    lista_interfaces = datos["nokia-conf:interface"]
    
    datos_estandarizados = []
    
    for interface in lista_interfaces:
        # Mapeamos 'enable' a 'up' y cualquier otra cosa (como 'disable') a 'down'
        if interface["admin-state"] == "enable":
            estado_unificado = "up"
        else:
            estado_unificado = "down"
            
        registro = {
            "fabricante": "Nokia",
            "interfaz": interface["interface-name"],
            "estado": estado_unificado
        }
        datos_estandarizados.append(registro)
        
    return datos_estandarizados