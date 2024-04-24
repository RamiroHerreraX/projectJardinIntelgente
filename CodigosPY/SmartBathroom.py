from machine import Pin, PWM, I2C
import ssd1306
from time import sleep
import network
from umqtt.simple import MQTTClient

# Configuración de pines para el sensor PIR, el relé y el LED RGB
pir_pin = Pin(22, Pin.IN)    # Pin del sensor PIR
relay_pin = Pin(14, Pin.OUT)  # Pin de control del relé
red_pin = 17  # Pin del LED rojo del KY-016 RGB
green_pin = 15  # Pin del LED verde del KY-016 RGB

# Configuración del display OLED
i2c = I2C(0, scl=Pin(4), sda=Pin(16))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuración de PWM para el LED RGB
green_pwm = PWM(Pin(green_pin), freq=5000)
red_pwm = PWM(Pin(red_pin), freq=5000)

# Función para mostrar un mensaje en toda la pantalla del OLED
def mostrar_mensaje(mensaje):
    display.fill(0)
    display.text(mensaje, 0, 0)
    display.show()

# Configuración de MQTT
MQTT_BROKER = "test.mosquitto.org"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ceramica/equipo1"
MQTT_PORT = 1883

def conectar_wifi():
    print("Conectando WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Red', '123456789')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Conectada!")

def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.connect()
    return client

def publicar_mensaje(client, msg):
    client.publish(MQTT_TOPIC, msg)

def verificar_funcionamiento(client):
    while True:
        pir_value = pir_pin.value()  # Lectura del sensor PIR
        if pir_value == 1:  # Si está ocupado
            
            mensaje = "OCUPADO"
            msg = "1"
            client.publish(MQTT_TOPIC, msg)
            mostrar_mensaje(mensaje.center(16))  # Centra el mensaje horizontalmente
            red_pwm.duty(1023)  # Encender LED rojo
            green_pwm.duty(0)  # Apagar LED verde
            relay_pin.value(1)  # Activar el relé (cierra el circuito)
            sleep(180)  # Mantener el relé activado durante 1 minuto
            relay_pin.value(0)  # Desactivar el relé después de 1 minuto
            msg = "0"
            client.publish(MQTT_TOPIC, msg)
            
        else:  # Si está disponible
            mensaje = "DISPONIBLE"
            mostrar_mensaje(mensaje.center(16))  # Centra el mensaje horizontalmente
            red_pwm.duty(0)  # Apagar LED rojo
            green_pwm.duty(1023)  # Encender LED verde
            relay_pin.value(0)  # Desactivar el relé (abre el circuito)
            
        
        sleep(1)
        
        
        

# Bucle principal
print('Programa iniciado. Presiona CTRL+C para salir.')
conectar_wifi()
client = conectar_mqtt()
verificar_funcionamiento(client)

