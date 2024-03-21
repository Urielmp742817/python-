import RPi.GPIO as GPIO
import time

# Configurar el modo de los pines
GPIO.setmode(GPIO.BOARD)

# Definir el pin al que está conectado el pistón
piston_pin = 11

# Configurar el pin del pistón como salida
GPIO.setup(piston_pin, GPIO.OUT)

try:
    while True:
        # Mover el pistón hacia adelante
        GPIO.output(piston_pin, GPIO.HIGH)
        time.sleep(1)  # Esperar un segundo
        
        # Detener el pistón
        GPIO.output(piston_pin, GPIO.LOW)
        time.sleep(1)  # Esperar un segundo
        
        # Mover el pistón hacia atrás
        GPIO.output(piston_pin, GPIO.HIGH)
        time.sleep(1)  # Esperar un segundo
        
        # Detener el pistón
        GPIO.output(piston_pin, GPIO.LOW)
        time.sleep(1)  # Esperar un segundo
        except KeyboardInterrupt:
    # Limpiar los pines GPIO antes de salir
    GPIO.cleanup()




