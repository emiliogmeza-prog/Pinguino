"""Interfaz USB para Kagastian 5000."""

import tkinter as tk
from tkinter import messagebox

try:
    import serial
except ImportError:
    serial = None


BAUD_RATE = 9600
arduino = None


def log(message):
    registro.insert(tk.END, message + "\n")
    registro.see(tk.END)


def conectar():
    global arduino

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

        arduino = serial.Serial(puerto, BAUD_RATE, timeout=1)
        estado.config(text=f"Conectado a {puerto}", fg="green")
        log(f"Conexion abierta en {puerto} a {BAUD_RATE} baudios.")
    except Exception as error:
        estado.config(text="No conectado", fg="red")
        messagebox.showerror("Error", f"No se pudo conectar:\n{error}")


def enviar(comando, descripcion):
    if arduino and arduino.is_open:
        arduino.write(comando.encode("ascii"))
        log(f"Comando {comando}: {descripcion}")
    else:
        messagebox.showwarning("Sin conexion", "Primero conecta el Arduino por USB.")


def cerrar():
    if arduino and arduino.is_open:
        arduino.close()
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Control Pinguino Robot Caminante")
ventana.geometry("420x500")
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
entrada_puerto = tk.Entry(ventana, width=20)
entrada_puerto.insert(0, "COM5")
entrada_puerto.pack(pady=5)

tk.Button(ventana, text="Conectar", width=25, command=conectar).pack(pady=5)

estado = tk.Label(ventana, text="No conectado", fg="red")
estado.pack(pady=5)

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

registro = tk.Text(ventana, height=5, width=48)
registro.pack(pady=10)
log("Listo. Conecta el Arduino por USB y elige el puerto COM.")

ventana.mainloop()
