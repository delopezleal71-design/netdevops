import csv

from cisco_agent import auditar_cisco
from juniper_agent import auditar_juniper
from nokia_agent import auditar_nokia

def ejecutar_auditoria_global():
    print("⏳ Iniciando auditoría automatizada multi-proveedor...")
    
    # 2. Ejecutamos cada agente y guardamos sus listas de datos estandarizados
    datos_cisco = auditar_cisco()
    datos_juniper = auditar_juniper()
    datos_nokia = auditar_nokia()
    
    # 3. Consolidamos todo en una sola lista unificada de la red
    # Sumar listas en Python junta todos sus elementos en una lista más grande
    inventario_global = datos_cisco + datos_juniper + datos_nokia
    
    # 4. Definimos el nombre del archivo físico que vamos a crear
    nombre_archivo_reporte = "reporte_cumplimiento_red.csv"
    
    # 5. Definimos los nombres de las columnas que tendrá nuestro reporte
    columnas = ["fabricante", "interfaz", "estado"]
    
    print(f"💾 Generando archivo de reporte: {nombre_archivo_reporte}...")
    
    # 6. Abrimos el archivo en modo escritura ('w' de write) con codificación UTF-8
    with open(nombre_archivo_reporte, mode="w", newline="", encoding="utf-8") as archivo_csv:
        # Creamos el objeto escritor de CSV y le pasamos los nombres de las columnas
        escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)
        
        # Escribimos la fila de los títulos (encabezados)
        escritor.writeheader()
        
        # Escribimos de forma masiva todas las filas de nuestro inventario global
        escritor.writerows(inventario_global)
        
    print("✅ Proceso finalizado con éxito. El reporte fue guardado.")

# Este bloque le indica a Python que si ejecutamos este archivo directamente, 
# debe arrancar ejecutando la función que programamos arriba.
if __name__ == "__main__":
    ejecutar_auditoria_global()