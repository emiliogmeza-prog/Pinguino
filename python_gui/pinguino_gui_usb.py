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


def enviar(comando):
    if arduino and arduino.is_open:
        arduino.write(comando.encode("ascii"))
        log(f"Comando enviado: {comando}")
    else:
        messagebox.showwarning("Sin conexion", "Primero conecta el Arduino por USB.")


def cerrar():
    if arduino and arduino.is_open:
        arduino.close()
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Control Pinguino Robot Caminante")
ventana.geometry("420x440")
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

tk.Button(ventana, text="Modo automatico", width=28, command=lambda: enviar("A")).pack(pady=4)
tk.Button(ventana, text="Caminata continua", width=28, command=lambda: enviar("C")).pack(pady=4)
tk.Button(ventana, text="Demo", width=28, command=lambda: enviar("D")).pack(pady=4)
tk.Button(ventana, text="Aumentar distancia", width=28, command=lambda: enviar("+")).pack(pady=4)
tk.Button(ventana, text="Disminuir distancia", width=28, command=lambda: enviar("-")).pack(pady=4)

registro = tk.Text(ventana, height=8, width=48)
registro.pack(pady=10)
log("Listo. Conecta el Arduino por USB y elige el puerto COM.")

ventana.mainloop()
