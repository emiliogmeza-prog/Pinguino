"""Interfaz USB para Kagastian 5000."""

import tkinter as tk
from tkinter import messagebox, scrolledtext

try:
    import serial
    from serial.tools import list_ports
except ImportError:
    serial = None
    list_ports = None


BAUD_RATE = 9600
arduino = None
reader_job = None


def log(message):
    """Agrega un mensaje al registro visible y desplaza al final."""
    registro.insert(tk.END, message + "\n")
    registro.see(tk.END)


def listar_puertos():
    """Detecta puertos seriales y propone el primero disponible."""
    if list_ports is None:
        return

    puertos = [puerto.device for puerto in list_ports.comports()]
    if puertos:
        entrada_puerto.delete(0, tk.END)
        entrada_puerto.insert(0, puertos[0])
        log("Puertos disponibles: " + ", ".join(puertos))
    else:
        log("No se detectaron puertos seriales.")


def conectar():
    """Abre el puerto elegido sin bloquear la interfaz."""
    global arduino, reader_job

    if serial is None:
        messagebox.showerror(
            "Falta pyserial",
            "Instala la libreria con:\n\npip install pyserial"
        )
        return

    puerto = entrada_puerto.get().strip()
    if not puerto:
        messagebox.showwarning("Puerto requerido", "Escribe un puerto, por ejemplo COM5.")
        return

    try:
        if arduino and arduino.is_open:
            arduino.close()

        arduino = serial.Serial(puerto, BAUD_RATE, timeout=0.05)
        estado.config(text=f"Conectado a {puerto}", fg="green")
        log(f"Conexion abierta en {puerto} a {BAUD_RATE} baudios.")
        if reader_job is None:
            leer_serial()
    except Exception as error:
        estado.config(text="No conectado", fg="red")
        messagebox.showerror("Error", f"No se pudo conectar:\n{error}")


def desconectar():
    """Libera el puerto y restablece los indicadores visuales."""
    global arduino

    if arduino and arduino.is_open:
        arduino.close()
        log("Conexion serial cerrada.")

    arduino = None
    estado.config(text="No conectado", fg="red")
    distancia.config(text="Distancia: -- cm")


def leer_serial():
    """Consulta periodicamente la telemetria usando el ciclo de Tkinter."""
    global reader_job, arduino

    try:
        if arduino and arduino.is_open:
            while arduino.in_waiting:
                mensaje = arduino.readline().decode("utf-8", errors="replace").strip()
                if not mensaje:
                    continue

                log("Arduino: " + mensaje)
                if mensaje.startswith("Distancia:"):
                    distancia.config(text=mensaje)
    except (OSError, serial.SerialException) as error:
        log(f"Error de lectura serial: {error}")
        desconectar()

    # after evita un bucle bloqueante y mantiene la ventana responsiva.
    reader_job = ventana.after(100, leer_serial)


def enviar(comando, descripcion):
    """Envia un caracter del protocolo y registra la accion."""
    if arduino and arduino.is_open:
        try:
            arduino.write(comando.encode("ascii"))
            log(f"PC -> Arduino [{comando}]: {descripcion}")
        except (OSError, serial.SerialException) as error:
            log(f"No se pudo enviar el comando: {error}")
            desconectar()
    else:
        messagebox.showwarning("Sin conexion", "Primero conecta el Arduino por USB.")


def cerrar():
    """Cancela la lectura programada y cierra recursos antes de salir."""
    global reader_job

    if reader_job is not None:
        ventana.after_cancel(reader_job)
        reader_job = None
    desconectar()
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Control Pinguino Robot Caminante")
ventana.geometry("620x670")
ventana.minsize(580, 620)
ventana.protocol("WM_DELETE_WINDOW", cerrar)

titulo = tk.Label(
    ventana,
    text="Pinguino Robot Caminante",
    font=("Arial", 14, "bold")
)
titulo.pack(pady=10)

descripcion = tk.Label(
    ventana,
    text="Control por Serial USB para robot con patas, motorreductor y L293D.",
    wraplength=360
)
descripcion.pack(pady=5)

tk.Label(ventana, text="Puerto Arduino, ejemplo COM5:").pack(pady=5)
entrada_puerto = tk.Entry(ventana, width=24)
entrada_puerto.insert(0, "COM5")
entrada_puerto.pack(pady=5)

controles_conexion = tk.Frame(ventana)
controles_conexion.pack(pady=5)

tk.Button(
    controles_conexion,
    text="Buscar puertos",
    width=15,
    command=listar_puertos
).pack(side=tk.LEFT, padx=3)

tk.Button(
    controles_conexion,
    text="Conectar",
    width=15,
    command=conectar
).pack(side=tk.LEFT, padx=3)

tk.Button(
    controles_conexion,
    text="Desconectar",
    width=15,
    command=desconectar
).pack(side=tk.LEFT, padx=3)

estado = tk.Label(ventana, text="No conectado", fg="red")
estado.pack(pady=5)

distancia = tk.Label(
    ventana,
    text="Distancia: -- cm",
    font=("Arial", 12, "bold"),
    fg="#1f4d78"
)
distancia.pack(pady=5)

tk.Button(
    ventana,
    text="Automatico: frena con sensor",
    width=30,
    command=lambda: enviar("A", "camina y se detiene si detecta un obstaculo")
).pack(pady=4)

tk.Button(
    ventana,
    text="Caminata continua",
    width=30,
    command=lambda: enviar("C", "camina de forma continua para probar el mecanismo")
).pack(pady=4)

tk.Button(
    ventana,
    text="Detener robot",
    width=30,
    command=lambda: enviar("S", "detiene el motor y deja el robot en reposo")
).pack(pady=4)

tk.Button(
    ventana,
    text="Prueba corta",
    width=30,
    command=lambda: enviar("D", "hace una prueba corta de movimiento")
).pack(pady=4)

tk.Button(
    ventana,
    text="+ Frenar mas lejos",
    width=30,
    command=lambda: enviar("+", "aumenta la distancia a la que frena")
).pack(pady=4)

tk.Button(
    ventana,
    text="- Frenar mas cerca",
    width=30,
    command=lambda: enviar("-", "disminuye la distancia a la que frena")
).pack(pady=4)


tk.Label(
    ventana,
    text="Registro de eventos y telemetria:",
    font=("Arial", 10, "bold")
).pack(anchor="w", padx=20, pady=(12, 3))

registro = scrolledtext.ScrolledText(
    ventana,
    width=57,
    height=9,
    state=tk.NORMAL,
    wrap=tk.WORD
)
registro.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 12))

log("Listo. Conecta el Arduino por USB y elige el puerto COM.")

ventana.mainloop()
