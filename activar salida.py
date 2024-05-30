from gpiozero import OutputDevice
import time

# Configuración de pines
RELE_PIN = 12 # Por ejemplo, el pin 12

# Configuración del dispositivo de salida
electrovalvula = OutputDevice(RELE_PIN)

# Funciones para controlar la electroválvula
def abrir_vlv():
    electrovalvula.on()
    time.sleep(0.5)  # Espera para asegurar la activación completa del relé

def cerrar_vlv():
    electrovalvula.off()
    time.sleep(0.5)  # Espera para asegurar la desactivación completa del relé

# Ejemplo de uso
abrir_vlv()
time.sleep(5)  # Espera 5 segundos
cerrar_vlv()