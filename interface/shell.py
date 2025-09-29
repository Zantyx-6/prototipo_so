# ================================
# Interfaz de Usuario (Shell)
# ================================
# Proporciona una consola donde el usuario puede interactuar
# con los gestores a través del kernel.

from colorama import init, Fore, Style
import pyfiglet
import time
from tqdm import tqdm

init(autoreset=True)  # Reinicia colores automáticamente

class Shell:
    def __init__(self, kernel):
        self.kernel = kernel  # Conexión con el núcleo del SO

    def boot_sequence(self):
        """Simula el arranque del sistema con animación."""
        mensajes = [
            "Inicializando hardware...",
            "Cargando kernel...",
            "Montando sistema de archivos...",
            "Sistema listo. Bienvenido!"
        ]
        for msg in mensajes:
            print(Fore.YELLOW + msg)
            time.sleep(0.8)

        # Barra de carga
        for _ in tqdm(range(100), desc="Arrancando SO", ncols=70, colour="green"):
            time.sleep(0.01)

    def run(self):
        """Inicia el bucle de la terminal simulada."""
        
        # Mostrar arranque
        self.boot_sequence()

        # Logo ASCII
        ascii_banner = pyfiglet.figlet_format("PROTO_SO")
        print(Fore.CYAN + Style.BRIGHT + ascii_banner)

        print(Fore.GREEN + "Escribe 'help' para ver comandos disponibles\n")

        while True:
            cmd = input(Fore.MAGENTA + "so> " + Style.RESET_ALL).strip().split()
            if not cmd:
                continue
            command, *args = cmd

            # Salida del sistema
            if command == "exit":
                print(Fore.RED + "Saliendo del sistema operativo...")
                break

            # Mostrar ayuda
            elif command == "help":
                self.show_help()

            # ======= Gestor de Procesos =======
            elif command == "run":
                name = args[0] if args else "programa"
                print(Fore.YELLOW + str(self.kernel.process_manager.create_process(name)))
            elif command == "ps":
                print(Fore.CYAN + str(self.kernel.process_manager.list_processes()))
            elif command == "kill":
                if args:
                    print(Fore.RED + str(self.kernel.process_manager.kill_process(int(args[0]))))
                else:
                    print("Uso: kill <pid>")

            # ======= Gestor de Memoria =======
            elif command == "mem":
                print(Fore.CYAN + str(self.kernel.memory_manager.show_memory()))
            elif command == "alloc":
                if len(args) >= 2:
                    print(Fore.YELLOW + str(self.kernel.memory_manager.allocate(int(args[0]), int(args[1]))))
                else:
                    print("Uso: alloc <pid> <size>")
            elif command == "free":
                if args:
                    print(Fore.YELLOW + str(self.kernel.memory_manager.free(int(args[0]))))
                else:
                    print("Uso: free <pid>")

            # ======= Gestor de Archivos =======
            elif command == "ls":
                print(Fore.CYAN + str(self.kernel.file_manager.list_files()))
            elif command == "write":
                if len(args) >= 2:
                    filename, content = args[0], " ".join(args[1:])
                    print(Fore.YELLOW + str(self.kernel.file_manager.write_file(filename, content)))
                else:
                    print("Uso: write <archivo> <contenido>")
            elif command == "read":
                if args:
                    print(Fore.CYAN + str(self.kernel.file_manager.read_file(args[0])))
                else:
                    print("Uso: read <archivo>")
            elif command == "rm":
                if args:
                    print(Fore.RED + str(self.kernel.file_manager.delete_file(args[0])))
                else:
                    print("Uso: rm <archivo>")

            # ======= Hardware =======
            elif command == "cycle":
                print(Fore.WHITE + str(self.kernel.run_cycle()))

            # Comando no válido
            else:
                print(Fore.RED + "Comando no reconocido. Escribe 'help'.")

    def show_help(self):
        """Muestra el menú de comandos disponibles."""
        print(Fore.CYAN + """
Comandos disponibles:
  run <nombre>       - Crea un proceso
  ps                 - Lista procesos
  kill <pid>         - Elimina un proceso
  alloc <pid> <n>    - Asigna memoria a proceso
  free <pid>         - Libera memoria de proceso
  mem                - Muestra la RAM simulada
  write <f> <c>      - Escribe archivo
  read <f>           - Lee archivo
  rm <f>             - Elimina archivo
  ls                 - Lista archivos
  cycle              - Ejecuta un ciclo de CPU
  help               - Muestra este menú
  exit               - Salir
""")
