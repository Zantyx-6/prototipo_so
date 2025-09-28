# ================================
# Punto de Entrada del Sistema
# ================================
# Este archivo inicializa el hardware, el kernel y la shell.
# Sirve como "arranque" del sistema operativo prototipo.

from hardware.hardware import Hardware
from kernel.kernel import Kernel
from interface.shell import Shell

if __name__ == "__main__":
    # Crear hardware simulado
    hardware = Hardware()
    # Crear kernel que gestiona todo
    kernel = Kernel(hardware)
    # Iniciar shell para interacción con usuario
    shell = Shell(kernel)
    shell.run()
