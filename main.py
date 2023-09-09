import RPi.GPIO as GPIO
import time

# Configura los pines del sensor ultrasónico
TRIG = 23
ECHO = 24

# Configura los pines de los motores del carro
motor_izquierdo_pin1 = 17
motor_izquierdo_pin2 = 18
motor_derecho_pin1 = 22
motor_derecho_pin2 = 27

# Inicializa los pines de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(motor_izquierdo_pin1, GPIO.OUT)
GPIO.setup(motor_izquierdo_pin2, GPIO.OUT)
GPIO.setup(motor_derecho_pin1, GPIO.OUT)
GPIO.setup(motor_derecho_pin2, GPIO.OUT)

# Función para medir la distancia con el sensor ultrasónico
def medir_distancia():
    GPIO.output(TRIG, False)
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distancia = pulse_duration * 17150
    return distancia

try:
    while True:
        distancia = medir_distancia()
        print("Distancia:", distancia, "cm")
        
        # Si la distancia es menor a 20 cm, gira a la derecha
        if distancia < 20:
            GPIO.output(motor_izquierdo_pin1, GPIO.HIGH)
            GPIO.output(motor_izquierdo_pin2, GPIO.LOW)
            GPIO.output(motor_derecho_pin1, GPIO.HIGH)
            GPIO.output(motor_derecho_pin2, GPIO.LOW)
        else:
            # Si no hay obstáculos cercanos, avanza recto
            GPIO.output(motor_izquierdo_pin1, GPIO.HIGH)
            GPIO.output(motor_izquierdo_pin2, GPIO.LOW)
            GPIO.output(motor_derecho_pin1, GPIO.HIGH)
            GPIO.output(motor_derecho_pin2, GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.cleanup()
