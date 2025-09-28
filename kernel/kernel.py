# ================================
# Núcleo (Kernel)
# ================================
# El Kernel es el encargado de coordinar la interacción
# entre el hardware y los gestores del sistema operativo.

from managers.process_manager import ProcessManager
from managers.memory_manager import MemoryManager
from managers.file_manager import FileManager

class Kernel:
    def __init__(self, hardware):
        # Guardamos referencia al hardware
        self.hardware = hardware
        # Inicializamos cada gestor
        self.process_manager = ProcessManager()
        self.memory_manager = MemoryManager(hardware)
        self.file_manager = FileManager(hardware)

    def run_cycle(self):
        """Ejecuta un ciclo de CPU en el hardware."""
        return self.hardware.execute_cycle()
