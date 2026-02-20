from datetime import time
import csv

class Auto:
    _next_id = 1

    def __init__(self, entrada, salida, server, descripcion):
        self.id = Auto._next_id
        Auto._next_id += 1
        self.entrada = entrada
        self.salida = salida
        self.server = server
        self.descripcion = descripcion

    def __str__(self):
        return f"Auto #{self.id}: Entrada: {self.entrada}, Salida: {self.salida}, Server: {self.server}, Descripcion: {self.descripcion}"
    
    def __repr__(self):
        return f"Auto(id={self.id}, entrada={self.entrada}, salida={self.salida}, server={self.server}, descripcion='{self.descripcion}')"

    def to_dict(self):
        """Convierte el objeto a diccionario para CSV"""
        return {
            'id': self.id,
            'entrada': self.entrada,
            'salida': self.salida,
            'server': self.server,
            'descripcion': self.descripcion
        }
    
    def to_csv_row(self):
        """Devuelve una lista para escribir directamente como fila CSV"""
        return [self.id, self.entrada, self.salida, self.server, self.descripcion]
    
    @classmethod
    def get_csv_headers(cls):
        """Devuelve los headers para el CSV"""
        return ['id', 'entrada', 'salida', 'server', 'descripcion']
    
    @classmethod
    def export_to_csv(cls, autos_list, filename):
        """Exporta una lista de autos a CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Escribir headers
            writer.writerow(cls.get_csv_headers())
            
            # Escribir datos
            for auto in autos_list:
                writer.writerow(auto.to_csv_row())
    
    @classmethod
    def export_to_csv_dict(cls, autos_list, filename):
        """Alternativa usando DictWriter (más legible)"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = cls.get_csv_headers()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for auto in autos_list:
                writer.writerow(auto.to_dict())

    @classmethod
    def reset_id_counter(cls, start_value=1):
        cls._next_id = start_value

    @classmethod
    def get_next_id(cls):
        return cls._next_id
    

class Server:
    def __init__(self, server_id):
        self.server_id = server_id
        self.registros = []  # Lista de registros de autos atendidos
    
    def agregar_registro(self, auto_id, tiempo_llegada, tiempo_salida):
        """Agrega un registro de atención para este servidor"""
        registro = {
            'auto_id': auto_id,
            'tiempo_llegada': tiempo_llegada,
            'tiempo_salida': tiempo_salida,
            'server_id': self.server_id
        }
        self.registros.append(registro)
    
    def agregar_auto(self, auto):
        """Agrega un auto completo al servidor (extrae los tiempos)"""
        self.agregar_registro(auto.id, auto.entrada, auto.salida)
    
    def __str__(self):
        return f"Server {self.server_id}: {len(self.registros)} registros"
    
    def __repr__(self):
        return f"Server(id={self.server_id}, registros={len(self.registros)}, descripcion='{self.descripcion}')"
    
    def to_csv_data(self):
        """Convierte todos los registros del servidor a formato CSV"""
        return self.registros
    
    @classmethod
    def get_csv_headers(cls):
        """Headers para CSV de registros de servidor"""
        return ['auto_id', 'tiempo_llegada', 'tiempo_salida', 'server_id']
    
    @classmethod
    def export_server_to_csv(cls, server, filename):
        """Exporta los registros de UN servidor a CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.get_csv_headers())
            
            writer.writeheader()
            for registro in server.registros:
                writer.writerow(registro)
    
    @classmethod
    def export_all_servers_to_csv(cls, servers_list, filename):
        """Exporta registros de TODOS los servidores a un CSV consolidado"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.get_csv_headers())
            
            writer.writeheader()
            for server in servers_list:
                for registro in server.registros:
                    writer.writerow(registro)
    
    @classmethod
    def create_servers_from_autos(cls, autos_list):
        """Factory method: crea servidores automáticamente desde lista de autos"""
        servers_dict = {}
        
        for auto in autos_list:
            server_id = auto.server
            
            # Crear servidor si no existe
            if server_id not in servers_dict:
                servers_dict[server_id] = cls(server_id)
            
            # Agregar el auto al servidor
            servers_dict[server_id].agregar_auto(auto)
        
        return list(servers_dict.values())
    
class Queue:
    _next_id = 1

    def __init__(self, tiempo_registro, cola_servidor1, cola_servidor2, cola_servidor3):
        self.id = Queue._next_id
        Queue._next_id += 1
        self.tiempo_registro = tiempo_registro
        self.cola_servidores = (cola_servidor1, cola_servidor2, cola_servidor3)
        
    def __str__(self):
        return f"Queue #{self.id}: Tiempo: {self.tiempo_registro}, Colas: {self.cola_servidores}"
    
    def __repr__(self):
        return f"Queue(id={self.id}, tiempo={self.tiempo_registro}, colas={self.cola_servidores})"
    
    @property
    def cola_servidor1(self):
        """Getter para cola del servidor 1"""
        return self.cola_servidores[0]
    
    @property
    def cola_servidor2(self):
        """Getter para cola del servidor 2"""
        return self.cola_servidores[1]
    
    @property
    def cola_servidor3(self):
        """Getter para cola del servidor 3"""
        return self.cola_servidores[2]
    
    @property
    def total_cola(self):
        """Total de vehículos en cola en todo el sistema"""
        return sum(self.cola_servidores)
    
    def to_dict(self):
        """Convierte el objeto a diccionario para CSV"""
        return {
            'id': self.id,
            'tiempo_registro': self.tiempo_registro,
            'cola_servidor1': self.cola_servidores[0],
            'cola_servidor2': self.cola_servidores[1],
            'cola_servidor3': self.cola_servidores[2],
            'total_cola': self.total_cola
        }
    
    def to_csv_row(self):
        """Devuelve una lista para escribir directamente como fila CSV"""
        return [
            self.id,
            self.tiempo_registro,
            self.cola_servidores[0],
            self.cola_servidores[1],
            self.cola_servidores[2],
            self.total_cola
        ]
    
    @classmethod
    def get_csv_headers(cls):
        """Devuelve los headers para el CSV"""
        return ['id', 'tiempo_registro', 'cola_servidor1', 'cola_servidor2', 'cola_servidor3', 'total_cola']
    
    @classmethod
    def export_to_csv(cls, queue_list, filename):
        """Exporta una lista de observaciones de cola a CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Escribir headers
            writer.writerow(cls.get_csv_headers())
            
            # Escribir datos
            for queue_obs in queue_list:
                writer.writerow(queue_obs.to_csv_row())
    
    @classmethod
    def export_to_csv_dict(cls, queue_list, filename):
        """Alternativa usando DictWriter (más legible)"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = cls.get_csv_headers()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for queue_obs in queue_list:
                writer.writerow(queue_obs.to_dict())
    
    @classmethod
    def reset_id_counter(cls, start_value=1):
        cls._next_id = start_value

    @classmethod
    def get_next_id(cls):
        return cls._next_id
    
