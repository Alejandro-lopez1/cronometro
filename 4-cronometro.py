import tkinter as tk #importamos el módulo Tkinter para la interfaz
import time #importamos el móduo time para trabajar con el tiempo

class Cronometro:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Cronómetro") #establece el título de la ventana

        #inicializando las variables del cronómetro
        self.tiempo_transcurrido = 0
        self.tiempo_inicio = None
        self.funcionando = False

        #creando la etiqueta para mostrar el tiempo transcurrido
        self.etiqueta_tiempo = tk.Label(ventana, text="00:00:00", font=("Arial", 30))
        self.etiqueta_tiempo.pack(pady=10)

        #crea el botón para iniciar el cronómetro
        self.boton_iniciar = tk.Button(ventana, text="Iniciar", command=self.iniciar_cronometro)
        self.boton_iniciar.pack(pady=5)

        #creando el botón para detener el cronómetro
        self.boton_detener = tk.Button(ventana, text="Detener", command=self.detener_cronometro, state=tk.DISABLED)
        self.boton_detener.pack(pady=5)

    def iniciar_cronometro(self):
        #función para iniciar el cronómetro
        if not self.funcionando:
            self.funcionando = True
            self.tiempo_inicio = time.time() - self.tiempo_transcurrido
            self.actualizar_cronometro()

            #deshabilita el boton de inicio y habilita el botón de detener
            self.boton_iniciar.config(state=tk.DISABLED)
            self.boton_detener.config(state=tk.NORMAL)

    def detener_cronometro(self):
        # Función para detener el cronómetro
        if self.funcionando:
            self.funcionando = False
            self.ventana.after_cancel(self.actualizar_cronometro)

            # Habilita el botón de inicio y deshabilita el botón de detener
            self.boton_iniciar.config(state=tk.NORMAL)
            self.boton_detener.config(state=tk.DISABLED)

    def actualizar_cronometro(self):
        #función para actualizar el tiempo transcurrido en el cronómetro
        if self.funcionando:
            self.tiempo_transcurrido = time.time() - self.tiempo_inicio

            #calcula las horas, minutos y segundos transcurridos
            horas = int(self.tiempo_transcurrido / 3600)
            minutos = int((self.tiempo_transcurrido % 3600) / 60)
            segundos = int(self.tiempo_transcurrido % 60)

            #formatea el tiempo transcurrido y actualiza la etiqueta
            tiempo_formateado = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
            self.etiqueta_tiempo.config(text=tiempo_formateado)

            #programa la próxima actualización del cronómetro después de 1 segundo
            self.ventana.after(1000, self.actualizar_cronometro)

if __name__ == "__main__":
    ventana = tk.Tk() #crea la ventana principal
    cronometro = Cronometro(ventana) #creando una instancia de la clase Cronometro
    ventana.mainloop() #ejecutamos el bucle principal de la interfaz gráfica



