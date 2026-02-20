from datetime import time
import os
from clases import Auto, Server, Queue

def crear_directorio_csv():
    """Crea el directorio csv si no existe"""
    if not os.path.exists('csv'):
        os.makedirs('csv')
        print("Directorio 'csv' creado")

def crear_autos():
    """Ejemplo de inserción de datos de autos"""
    print("=== INSERTANDO DATOS DE AUTOS ===")
    
    # Resetear contador para empezar desde 1
    Auto.reset_id_counter(1)
    
    # Crear instancias de autos con datos de ejemplo
    autos = [
        Auto(time(0, 0, 0), time(0, 0, 0), 2, "Auto inicio de medicion pvi S2 1"),
        Auto(time(0, 0, 22), time(0, 9, 36), 2, "Van negra"),
        Auto(time(0, 0, 0), time(0, 0, 44), 1, "Auto pvi S1 1"),
        Auto(time(0, 1, 56), time(0, 18, 55), 3, "Mazda gris"),
        Auto(time(0, 0, 0), time(0, 2, 16), 2, "Auto pvi S2 2"),
        Auto(time(0, 0, 0), time(0, 3, 0), 1, "Auto pvi S1 2"),
        Auto(time(0, 3, 0), time(0, 13, 18), 1, "Susuki gris"),
        Auto(time(0, 5, 55), time(0, 17, 16), 2, "Null"),
        Auto(time(0, 0, 0), time(0, 6, 35), 2, "Auto pvi S2 3"),
        Auto(time(0, 6, 35), time(0, 11, 31), 2, "Sedan blanco"),
        Auto(time(0, 0, 0), time(0, 7, 25), 3, "Auto pvi S3 1"),
        Auto(time(0, 7, 25), time(0, 23, 29), 1, "Chino rojo"),
        Auto(time(0, 12, 17), time(0, 20, 14), 3, "Kia gris"),
        Auto(time(0, 13, 54), time(0, 24, 19), 2, "Maxus blanca"),
        Auto(time(0, 19, 31), time(0, 29, 44), 3, "City negro"),
        Auto(time(0, 20, 30), time(0, 31, 22), 2, "Hyundai rojo"),
        Auto(time(0, 20, 54), time(0, 44, 10), 1, "Toyota rojo"),
        Auto(time(0, 25, 49), time(0,  34, 20), 3, "Susuki negro"),
        Auto(time(0, 26, 10), time(0, 48, 47), 1, "MG blanco"),
        Auto(time(0, 31, 51), time(0, 42, 36), 3, "Chev gris"),
        Auto(time(0, 32, 58), time(0, 45, 38), 2, "Minivan gris"),
        Auto(time(0, 41, 10), time(0, 53, 40), 1, "Camioncito"),
        Auto(time(0, 44, 23), time(0, 54, 11), 2, "Chev negro"),
        Auto(time(0, 53, 50), time(1, 4, 35), 1, "Chino blanco"),
        Auto(time(1, 0, 52), time(1, 11, 0), 1, "Dodge roja")
    ]
    
    # Mostrar algunos autos creados
    print("Autos creados:")
    for auto in autos[:3]:  # Mostrar solo los primeros 3
        print(f"  {auto}")
    print(f"  ... y {len(autos)-3} más")
    
    # Exportar a CSV
    Auto.export_to_csv_dict(autos, 'csv/autos_datos.csv')
    print(f"✅ Exportados {len(autos)} autos a 'csv/autos_datos.csv'")
    
    return autos

def insert_servers(autos):
    """Ejemplo de inserción de datos de servidores"""
    print("\n=== INSERTANDO DATOS DE SERVIDORES ===")
    
    # Crear servidores automáticamente desde los autos
    servers = Server.create_servers_from_autos(autos)
    
    # Mostrar información de servidores
    print("Servidores creados:")
    for server in servers:
        print(f"  {server}")
    
    # Exportar cada servidor por separado
    for server in servers:
        filename = f'csv/servidor_{server.server_id}_registros.csv'
        Server.export_server_to_csv(server, filename)
        print(f"✅ Exportado servidor {server.server_id} a '{filename}'")
    
    # Exportar todos los servidores juntos
    Server.export_all_servers_to_csv(servers, 'csv/todos_servidores.csv')
    print("✅ Exportados todos los servidores a 'csv/todos_servidores.csv'")
    
    return servers

def insert_colas():
    """Ejemplo de inserción de observaciones de cola"""
    print("\n=== INSERTANDO OBSERVACIONES DE COLA ===")
    
    # Resetear contador para empezar desde 1
    Queue.reset_id_counter(1)
    
    # Crear observaciones de cola con datos de ejemplo
    observaciones = [
        Queue(time(0, 0, 0), 2, 1, 1),
        Queue(time(0, 13, 0), 1, 1, 1),
        Queue(time(0, 20, 0), 0, 0, 1),
        Queue(time(0, 20, 30), 1, 1, 2),
        Queue(time(0, 25, 10), 1, 1, 2),
        Queue(time(0, 27, 0), 1, 1, 0),
        Queue(time(0, 30, 30), 1, 1, 1),
        Queue(time(0, 35, 0), 1, 1, 0),
        Queue(time(0, 37, 0), 1, 1, 0),
        Queue(time(0, 44, 0), 1, 1, 0),
        Queue(time(0, 53, 0), 2, 0, 0),
        Queue(time(0, 45, 38), 0, 0, 0),
        Queue(time(0, 46, 31), 1, 0, 0),
        Queue(time(1, 0, 0), 0, 0, 0),
    ]
    
    # Mostrar algunas observaciones
    print("Observaciones de cola creadas:")
    for obs in observaciones[:3]:  # Mostrar solo las primeras 3
        print(f"  {obs} - Total: {obs.total_cola}")
    print(f"  ... y {len(observaciones)-3} más")
    
    # Exportar a CSV
    Queue.export_to_csv_dict(observaciones, 'csv/observaciones_cola.csv')
    print(f"✅ Exportadas {len(observaciones)} observaciones a 'csv/observaciones_cola.csv'")
    
    return observaciones

def mostrar_resumen(autos, servers, observaciones):
    """Muestra un resumen de todos los datos insertados"""
    print("\n" + "="*50)
    print("RESUMEN DE DATOS INSERTADOS")
    print("="*50)
    print(f"📊 Total de autos procesados: {len(autos)}")
    print(f"🏢 Total de servidores activos: {len(servers)}")
    print(f"📈 Total de observaciones de cola: {len(observaciones)}")
    
    # Estadísticas por servidor
    print("\nDistribución por servidor:")
    for server in servers:
        print(f"  Servidor {server.server_id}: {len(server.registros)} autos atendidos")
    
    # Archivos CSV generados
    print(f"\n📁 Archivos CSV generados en carpeta 'csv':")
    csv_files = [
        "autos_datos.csv",
        "todos_servidores.csv", 
        "observaciones_cola.csv"
    ]
    for server in servers:
        csv_files.append(f"servidor_{server.server_id}_registros.csv")
    
    for filename in csv_files:
        print(f"  ✅ {filename}")

def main():
    """Función principal para ejecutar todos los ejemplos"""
    print("🚀 INICIANDO INSERCIÓN DE DATOS PARA ANÁLISIS ESTOCÁSTICO")
    print("="*60)
    
    # Crear directorio
    crear_directorio_csv()
    
    # Insertar datos de cada clase
    autos = crear_autos()
    servers = insert_servers(autos)
    observaciones = insert_colas()
    
    # Mostrar resumen
    mostrar_resumen(autos, servers, observaciones)
    
    print("\n🎉 ¡Inserción de datos completada exitosamente!")
    print("Los archivos CSV están listos para el análisis de métricas del sistema.")

if __name__ == "__main__":
    main()