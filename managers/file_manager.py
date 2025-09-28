# ================================
# Gestor de Archivos
# ================================
# Permite crear, leer, eliminar y listar archivos.
# Los archivos se almacenan en el "disco" simulado.

class FileManager:
    def __init__(self, hardware):
        self.hardware = hardware  # Uso del disco del hardware

    def write_file(self, filename, content):
        """Escribe un archivo en el disco (clave = nombre, valor = contenido)."""
        self.hardware.disk[filename] = content
        return f"Archivo '{filename}' escrito"

    def read_file(self, filename):
        """Lee un archivo del disco. Devuelve error si no existe."""
        return self.hardware.disk.get(filename, "Error: Archivo no encontrado")

    def delete_file(self, filename):
        """Elimina un archivo si existe en el disco."""
        if filename in self.hardware.disk:
            del self.hardware.disk[filename]
            return f"Archivo '{filename}' eliminado"
        return "Error: Archivo no encontrado"

    def list_files(self):
        """Lista todos los archivos almacenados en el disco."""
        if not self.hardware.disk:
            return "No hay archivos en el disco"
        return "\n".join(self.hardware.disk.keys())
