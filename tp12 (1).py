class Curso:
    def __init__(self, nombre, nivel, docente):
        self.nombre = nombre
        self.nivel = nivel
        self.docente = docente

    def iniciar_clase(self):
        print(f"La clase de {self.nombre} ha comenzado.")

    def terminar_trimestre(self):
        print(f"El trimestre del curso {self.nivel} ha finalizado.")


class Computadora:
    def __init__(self, marca, ram, estado="apagada"):
        self.marca = marca
        self.ram = ram
        self.estado = estado

    def encender(self):
        self.estado = "encendida"
        print("La computadora está encendida.")

    def instalar_programa(self, programa):
        print(f"Instalando el programa {programa}...")


class TelefonoMovil:
    def __init__(self, bateria, sistema_operativo, numero):
        self.bateria = bateria
        self.sistema_operativo = sistema_operativo
        self.numero = numero

    def llamar(self, destino):
        print(f"Llamando al número {destino}...")

    def enviar_mensaje(self, texto):
        print(f"Mensaje enviado: {texto}")


class Profesor:
    def __init__(self, nombre, materia, antiguedad):
        self.nombre = nombre
        self.materia = materia
        self.antiguedad = antiguedad

    def calificar_trabajo(self):
        print(f"{self.nombre} está calificando trabajos.")

    def dar_clase(self):
        print(f"{self.nombre} está dando clase de {self.materia}.")


class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de {self.artista}.")

    def pausar(self):
        print(f"'{self.titulo}' ha sido pausada.")


class ListaDeCompras:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nombre_producto):
        self.productos.append(nombre_producto)
        print(f"Producto agregado: {nombre_producto}")

    def ver_productos(self):
        print("Productos en la lista:", self.productos)


class EstanteDeLibros:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.libros = []

    def prestar_libro(self, titulo):
        if titulo in self.libros:
            self.libros.remove(titulo)
            print(f"Libro prestado: {titulo}")
        else:
            print("El libro no está disponible.")

    def verificar_disponibilidad(self, titulo):
        if titulo in self.libros:
            print("El libro está disponible.")
        else:
            print("No está disponible.")


class BilleteraElectronica:
    def __init__(self, usuario, saldo, moneda):
        self.usuario = usuario
        self.saldo = saldo
        self.moneda = moneda

    def transferir(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Transferencia realizada. Saldo actual: {self.saldo} {self.moneda}")
        else:
            print("Error: saldo insuficiente.")

    def recibir_pago(self, monto):
        self.saldo += monto
        print(f"Pago recibido. Saldo actual: {self.saldo} {self.moneda}")


class HistorialMedico:
    def __init__(self, paciente, grupo_sanguineo, alergias):
        self.paciente = paciente
        self.grupo_sanguineo = grupo_sanguineo
        self.alergias = alergias
        self.diagnosticos = []

    def agregar_diagnostico(self, descripcion):
        self.diagnosticos.append(descripcion)
        print("Diagnóstico agregado correctamente.")

    def mostrar_alergias(self):
        print("Alergias del paciente:", self.alergias)
