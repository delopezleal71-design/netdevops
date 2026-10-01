import json
import requests


# 1. FUNCIÓN QUE CONSULTA LOS CONTADORES (TELEMETRÍA)
def consultar_errores_crc():
    # Simulación de la respuesta de la API de Juniper con los contadores de la interfaz ge-0/0/0
    json_juniper_counters = """
    {
        "interface-information": {
            "physical-interface": {
                "name": "ge-0/0/0",
                "input-error-list": {
                    "input-crc-errors": "142"
                }
            }
        }
    }
    """
    datos = json.loads(json_juniper_counters)
    crc_actuales = int(datos["interface-information"]["physical-interface"]["input-error-list"]["input-crc-errors"])
    return crc_actuales


# 2. FUNCIÓN QUE CONFIGURA EL APAGADO (ACCIÓN CORRECCIÓN)
def apagar_interfaz_degradada():
    print("🚨 [ACCION] Enviando Payload API a Juniper para deshabilitar la interfaz ge-0/0/0...")

    # Este es el bloque de configuración (Payload) que apaga la interfaz administrativamente
    payload_shutdown = {
        "configuration": {
            "interfaces": {
                "interface": {
                    "name": "ge-0/0/0",
                    "disable": "disable"  # Activamos el shutdown
                }
            }
        }
    }

    # En la vida real, acá ejecutaríamos el requests.post() hacia el router:
    # requests.post("https://juniper-core/api/config", json=payload_shutdown, ...)
    print("🔒 [CONFIG] Interfaz ge-0/0/0 apagada con éxito. Tráfico desviado por Backup.")


# 3. EL CEREBRO DEL SISTEMA (LA LOGICA DE NEGOCIO DE RED)
def monitoreo_inteligente_lazo_cerrado():
    UMBRAL_MAXIMO_CRC = 50
    print("🔎 Monitoreando contadores físicos de la red...")

    errores_detectados = consultar_errores_crc()
    print(f"📊 Interfaz ge-0/0/0 - Errores CRC detectados: {errores_detectados}")

    # Tomamos la decisión ingenieril basada en la condición analizada
    if errores_detectados > UMBRAL_MAXIMO_CRC:
        print(f"❌ CRÍTICO: Los errores ({errores_detectados}) superan el umbral permitido ({UMBRAL_MAXIMO_CRC}).")
        print("⚠️  Peligro de degradación de tráfico y fluctuación (flapping) de protocolos.")
        apagar_interfaz_degradada()
    else:
        print("✅ Enlace saludable. Los niveles de CRC están dentro del rango operativo.")


if __name__ == "__main__":
    monitoreo_inteligente_lazo_cerrado()