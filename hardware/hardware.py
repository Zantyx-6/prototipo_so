# ================================
# Capa de Hardware (Simulado)
# ================================
# Esta capa representa los recursos básicos de la máquina.
# No es hardware real, sino un modelo simplificado.

class Hardware:
    def __init__(self):
        # Memoria RAM simulada: 64 bloques
        self.memory = ["[Libre]"] * 64  
        # Disco simulado: diccionario clave-valor
        self.disk = {}                  
        # Contador de ciclos de CPU
        self.cpu_cycle = 0              

    def execute_cycle(self):
        """
        Simula la ejecución de un ciclo de CPU.
        Aumenta el contador y devuelve un mensaje.
        """
        self.cpu_cycle += 1
        return f"Ciclo {self.cpu_cycle} ejecutado"
