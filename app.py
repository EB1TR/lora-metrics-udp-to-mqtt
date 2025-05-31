# -*- coding: utf-8 -*-
# pylint: disable=locally-disabled, multiple-statements
# pylint: disable=fixme, line-too-long, invalid-name
# pylint: disable=W0703
# pylint: disable=W0605

# Libreria estándar ----------------------------------------------------------------------------------------------------
#
import socket
import sys
# ----------------------------------------------------------------------------------------------------------------------

# Paquetes instalados --------------------------------------------------------------------------------------------------
#
import paho.mqtt.client as mqtt
# ----------------------------------------------------------------------------------------------------------------------

# Importaciones locales ------------------------------------------------------------------------------------------------
#
import settings
# ----------------------------------------------------------------------------------------------------------------------

# Entorno --------------------------------------------------------------------------------------------------------------
#
UDP_PORT = settings.Config.UDP_PORT
UDP_IP = settings.Config.UDP_IP
MQTT_HOST = settings.Config.MQTT_HOST
MQTT_PORT = settings.Config.MQTT_PORT
MQTT_TOPIC = settings.Config.MQTT_TOPIC
# ----------------------------------------------------------------------------------------------------------------------


def main():
    # Conectar al broker MQTT ------------------------------------------------------------------------------------------
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.connect(MQTT_HOST, MQTT_PORT, 60)
    mqtt_client.loop_start()

    print("conectado a MQTT")

    # Crear socket UDP -------------------------------------------------------------------------------------------------
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.bind((UDP_IP, UDP_PORT))

    print(f"Escuchando UDP en {UDP_IP}:{UDP_PORT} y publicando en MQTT {MQTT_TOPIC}")

    try:
        while True:
            data, addr = udp_sock.recvfrom(4096)
            message = data.decode(errors='replace')
            print(f"Mensaje recibido de {addr}: {message.strip()}")
            mqtt_client.publish(MQTT_TOPIC, message)
    except KeyboardInterrupt:
        print("Parando: Usuario")
        sys.exit(0)
    except EOFError:
        text = 'EOFError: %s' % EOFError
        print(text)
        print("Parando: EOFError")
        sys.exit(0)
    except OSError:
        text = 'OSError: %s' % OSError
        print("Parando: OSError")
        print(text)
        sys.exit(0)
    except Exception as e:
        text = 'Excepción general: %s' % e
        print("Parando: General")
        print(text)
        sys.exit(0)
    finally:
        udp_sock.close()
        mqtt_client.loop_stop()
        mqtt_client.disconnect()

if __name__ == '__main__':
    main()