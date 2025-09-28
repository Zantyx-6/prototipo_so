# ================================
# Interfaz de Usuario (Shell)
# ================================
# Proporciona una consola donde el usuario puede interactuar
# con los gestores a través del kernel.

class Shell:
    def __init__(self, kernel):
        self.kernel = kernel  # Conexión con el núcleo del SO

    def run(self):
        """Inicia el bucle de la terminal simulada."""
        print("=== Prototipo SO en Python ===")
        print("Escribe 'help' para ver comandos disponibles\n")
        while True:
            cmd = input("so> ").strip().split()
            if not cmd:
                continue
            command, *args = cmd

            # Salida del sistema
            if command == "exit":
                print("Saliendo del sistema operativo...")
                break

            # Mostrar ayuda
            elif command == "help":
                self.show_help()

            # ======= Gestor de Procesos =======
            elif command == "run":
                name = args[0] if args else "programa"
                print(self.kernel.process_manager.create_process(name))
            elif command == "ps":
                print(self.kernel.process_manager.list_processes())
            elif command == "kill":
                if args: print(self.kernel.process_manager.kill_process(int(args[0])))
                else: print("Uso: kill <pid>")

            # ======= Gestor de Memoria =======
            elif command == "mem":
                print(self.kernel.memory_manager.show_memory())
            elif command == "alloc":
                if len(args) >= 2:
                    print(self.kernel.memory_manager.allocate(int(args[0]), int(args[1])))
                else:
                    print("Uso: alloc <pid> <size>")
            elif command == "free":
                if args: print(self.kernel.memory_manager.free(int(args[0])))
                else: print("Uso: free <pid>")

            # ======= Gestor de Archivos =======
            elif command == "ls":
                print(self.kernel.file_manager.list_files())
            elif command == "write":
                if len(args) >= 2:
                    filename, content = args[0], " ".join(args[1:])
                    print(self.kernel.file_manager.write_file(filename, content))
                else:
                    print("Uso: write <archivo> <contenido>")
            elif command == "read":
                if args: print(self.kernel.file_manager.read_file(args[0]))
                else: print("Uso: read <archivo>")
            elif command == "rm":
                if args: print(self.kernel.file_manager.delete_file(args[0]))
                else: print("Uso: rm <archivo>")

            # ======= Hardware =======
            elif command == "cycle":
                print(self.kernel.run_cycle())

            # Comando no válido
            else:
                print("Comando no reconocido. Escribe 'help'.")

    def show_help(self):
        """Muestra el menú de comandos disponibles."""
        print("""
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
