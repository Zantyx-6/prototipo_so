# ================================
# Gestor de Memoria
# ================================
# Simula la asignación y liberación de bloques de memoria.
# La memoria está representada en la capa de hardware.

class MemoryManager:
    def __init__(self, hardware):
        self.hardware = hardware  # Dependencia hacia el hardware

    def allocate(self, pid, size):
        """
        Asigna 'size' bloques de memoria al proceso 'pid'.
        Busca bloques libres en la RAM simulada.
        """
        free_blocks = [i for i, block in enumerate(self.hardware.memory) if block == "[Libre]"]
        if len(free_blocks) < size:
            return "Error: Memoria insuficiente"

        # Marcar bloques como ocupados por el proceso
        for i in free_blocks[:size]:
            self.hardware.memory[i] = f"PID{pid}"
        return f"{size} bloques asignados a PID {pid}"

    def free(self, pid):
        """
        Libera todos los bloques de memoria ocupados por un proceso.
        """
        released = 0
        for i, block in enumerate(self.hardware.memory):
            if block == f"PID{pid}":
                self.hardware.memory[i] = "[Libre]"
                released += 1
        return f"{released} bloques liberados para PID {pid}"

    def show_memory(self):
        """Muestra el estado actual de la memoria RAM."""
        return " | ".join(self.hardware.memory)
