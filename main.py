'''
RTSP Video Stream MQTT Publisher

Description: 
This script captures video frames from an RTSP stream and publishes them to an MQTT Broker
'''

import argpase
import sys
import paho.mqtt.client as mqtt
import cv2
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

mqtt_client = mqtt.Client()
mqtt_topic_videoframes = "video_frames"
mqtt_topic_delay = "BF/image/senddelay"
mqtt_topic_command = "BF/image/sendnow"

default_delay = 5
current_delay = default_delay

def on_connect(client, userdata, flags, rc):
    # Callback function for MQTT clinet connection
    if rc == 0:
        logger.info("Connected to MQTT broker")
        mqtt_client.subscribe(mqtt_topic_delay)
        mqtt_client.subscribe(mqtt_topic_command)
    else:
        logger.error("Connection failed, rc=", rc)

def on_publish(client, userdata, mid):
    # Callback function for MQTT message publish
    global current_delay
    message = msg.payload.decode()
    logger.debug("Message received: ", message)

    if msg.topic == mqtt_topic_delay:
        try: 
            new_delay = int(message)
            if new_delay >= 0:
                current_delay = new_delay
                logger.info("Image send delay set to ", new_delay)
            else:
                logger.warning("Invali Delay Value")
        except ValueError:
            logger.error("Invalid Delay Value")
    elif msg.topic == mqtt_topic_command and message = "sendnow":
        main()

# Configure MQTT client callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.on_message = on_message

# MQTT broker settings
mqtt_broker_address = "gaztec.ddns.net"
mqtt_client.username_pw_set(username="BF-1", password="123456")

try:
    mqtt_client.connect(mqtt_broker_address, port=1883)
except ConnectionRefusedError:
    logger.error("Connection refused: The broker if offline or unreachable")
    sys.exit(1)

while not mqtt_client.is_connected:
    mqtt_client.loop_start()

def main():

    try:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            _, encoded_frame = cv2.imencode('.jpg', frame)
            mqtt_client.publish(mqtt_topic_videoframes, payload=encoded_frames.tobytes(), qos=0)
        else: 
            logger.warning("Failed to grab frame")
    except cv2.error as cv2_error:
        logger.error("OpenCV error: " cv2_error)
    except mqtt.MQTTException as mqtt_error:
        logger.error("MQTT error: ", mqtt_error)
    except Exception as error:
        logger.error("An error occurred: ", str(error))

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="RTSP Video Stream MQTT Publisher")
        parser.add_argument("rtsp_link", help="RTSP link (not mandatory if -h/--h is used)")

        args = parser.parse_args()
        rtsp_link = args.rtsp_link

        if not rtsp_link:
            logger.error("RTSP link is not provided. Use -h/--help for usage details")
            sys.exit(1)

        logger.info("RTSP link: ", rtsp_link)

        cap = cv2.VideoCapture(rtsp_link, apiPreference=cv2.CAP_FFMPEG)
        try:
            while cap.isOpened():
                main()
                time.sleep(current_delay)
        except KeyboardInterrupt:
            logger.info("Keyboard Interrupt detected. Exiting Program.")
            mqtt_client.loop_stop()
        except cv2.error as cv2_error:
            logger.error("OpenCV error: ", cv2_error)
        except mqtt.MQTTException as mqtt_error:
            logger.error("MQTT error: ", mqtt_error)
        except Exception as error:
            logger.error("An error occurred.")
            
    except argparse.ArgumentError as arg_error:
        logger.error("Arguemtn error: ", str(arg_error))
    except Exception as error: 
        logger.error("An error occurred: ", str(error))

