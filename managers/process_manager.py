# ================================
# Gestor de Procesos
# ================================
# Controla la creación, listado y eliminación de procesos.
# Cada proceso se identifica con un PID único.

class ProcessManager:
    def __init__(self):
        # Diccionario para almacenar procesos en ejecución
        self.processes = {}
        # Contador de PID (Process ID)
        self.pid_counter = 1

    def create_process(self, name):
        """Crea un nuevo proceso y le asigna un PID."""
        pid = self.pid_counter
        self.processes[pid] = {"name": name, "status": "ejecutando"}
        self.pid_counter += 1
        return f"Proceso '{name}' creado con PID {pid}"

    def list_processes(self):
        """Devuelve un listado de procesos en ejecución."""
        if not self.processes:
            return "No hay procesos en ejecución"
        return "\n".join([f"PID {pid}: {p['name']} ({p['status']})"
                          for pid, p in self.processes.items()])

    def kill_process(self, pid):
        """Elimina un proceso según su PID."""
        if pid in self.processes:
            del self.processes[pid]
            return f"Proceso {pid} eliminado"
        return f"No existe el proceso con PID {pid}"
