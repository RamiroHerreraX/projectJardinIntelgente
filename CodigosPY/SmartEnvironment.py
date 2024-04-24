from machine import Pin, SoftI2C, ADC
from time import sleep
import ssd1306
import dht
from umqtt.simple import MQTTClient
import network

# Configuración de MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_POTHO_TOPIC = "utng/ceramica/potho"
MQTT_HUMI_TOPIC = "utng/ceramica/humi"
MQTT_FIRE_TOPIC = "utng/ceramica/fire"
MQTT_PORT = 1883

# Función para conectar a WiFi
def conectar_wifi():
    print("Conectando a WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Red', '123456789')  # Cambiar según tu red WiFi
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.5)
    print("Conectado a WiFi")

# Función para manejar los mensajes MQTT recibidos
def llegada_mensaje(topic, msg):
    print("Mensaje recibido:", msg)

# Función para suscribirse a MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID,
                        MQTT_BROKER, 
                        user=MQTT_USER,
                        password=MQTT_PASSWORD)
    client.set_callback(llegada_mensaje)  # Configurar la función de devolución de llamada
    client.connect()
    client.subscribe(MQTT_POTHO_TOPIC)
    client.subscribe(MQTT_HUMI_TOPIC)
    client.subscribe(MQTT_FIRE_TOPIC)
    return client

conectar_wifi()

client = subscribir()

sensor = dht.DHT11(Pin(5))

led = 15
led = Pin(led, Pin.OUT)

pin_fotoresistor = 34
adc = ADC(Pin(pin_fotoresistor))
adc.atten(ADC.ATTN_11DB)

KY026d = 16
digital_sensor = Pin(KY026d, Pin.IN)

zumbador_pin = 17
zumbador = Pin(zumbador_pin, Pin.OUT)

i2c = SoftI2C(sda=Pin(21), scl=Pin(19))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Ciclo principal
while True:
    sensor.measure()
    temperatura = sensor.temperature()
    humedad = sensor.humidity()
    
    valor_fotoresistor = adc.read()
    
    valor = digital_sensor.value()
    
    if valor_fotoresistor < 500:
        led.value(1)
        client.publish(MQTT_POTHO_TOPIC, str(valor_fotoresistor))
    else:
        led.value(0)
        client.publish(MQTT_POTHO_TOPIC, str(valor_fotoresistor))
    
    if valor == 1:
        zumbador.value(1)
        display.fill(0)
        display.text('Fuego', 0, 0, 6)
        display.show()
        client.publish(MQTT_FIRE_TOPIC, str(valor))
    elif temperatura >= 40:
        zumbador.value(1)
        display.fill(0)
        display.text('Temperatura alta', 0, 0, 6)
        display.show()
        client.publish(MQTT_HUMI_TOPIC, str(temperatura))
    else:
        zumbador.value(0)
        display.fill(0)
        display.text('Temperatura: %d C' % temperatura, 0, 0, 6)
        display.text('Humedad: %d %%' % humedad, 0, 20)
        display.show()
        client.publish(MQTT_FIRE_TOPIC, str(valor))
        client.publish(MQTT_HUMI_TOPIC, str(temperatura))
    
    # Publicar datos MQTT
    client.check_msg()
    
    sleep(5)
