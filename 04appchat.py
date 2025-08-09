import openai
import openai
import tkinter as tk
from tkinter import scrolledtext

# ✅ Tu API Key de OpenAI
openai.api_key = "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"  # ← Reemplaza esto con tu clave real

# Función para enviar mensaje a OpenAI
def enviar_mensaje():
    mensaje_usuario = entrada.get()
    if not mensaje_usuario.strip():
        return

    chat_box.insert(tk.END, "Tú: " + mensaje_usuario + "\n")
    entrada.delete(0, tk.END)

    try:
        respuesta = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un asistente de viajes útil que ayuda a planificar vacaciones, recomendar destinos, y dar consejos sobre presupuestos y clima."},
                {"role": "user", "content": mensaje_usuario}
            ]
        )
        respuesta_texto = respuesta.choices[0].message.content
        chat_box.insert(tk.END, "Asistente: " + respuesta_texto + "\n")
    except Exception as e:
        chat_box.insert(tk.END, "Error: " + str(e) + "\n")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Chat de Viajes con OpenAI")

# Crear caja de chat
chat_box = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=60, height=20)
chat_box.pack(padx=10, pady=10)

# Entrada de texto
entrada = tk.Entry(ventana, width=50)
entrada.pack(padx=10, pady=5)

# Botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=5)

ventana.mainloop()
