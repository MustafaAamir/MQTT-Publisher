# RTSP Video Stream MQTT Publisher
This script captures video frames from an RTSP stream and publishes them to an MQTT broker. It provides a flexible and customizable solution for streaming video frames over MQTT, allowing for remote monitoring and integration with other systems.

## Table of Contents
1. Description
2. Requirements
3. Installation
4. Usage
5. MQTT Topics
6. Customization
7. Troubleshooting
8. Contributing
9. License
10. Description
    
The RTSP Video Stream MQTT Publisher script serves as a bridge between an RTSP video stream source and an MQTT broker. It captures video frames from the RTSP stream and publishes them to an MQTT topic, allowing subscribers to receive and process these frames. Additionally, the script supports dynamic configuration of frame sending delay through MQTT commands.

### Requirements
To run this script, you need:

Python 3.x (Tested on Python 3.6 and above)
paho-mqtt library 
`pip install paho-mqtt`
opencv-python library 
`pip install opencv-python`
An MQTT broker (e.g., Mosquitto) accessible from the network
Installation
Clone or download the repository to your local machine.

Install the required Python packages using the following commands
`pip install -r requirements.txt`

### Usage
Run the script with the following command, providing at least one RTSP link:

`python rtsp_video_mqtt_publisher.py <RTSP_LINK_1> [RTSP_LINK_2 ...] [-vs]`
Replace `<RTSP_LINK_1>`, `<RTSP_LINK_2>`, etc., with the actual RTSP stream URLs.
Use the `-vs` flag to display the video locally while streaming (optional).
The script will capture frames from the RTSP stream and publish them to the MQTT broker.

You can adjust the sending delay for frames by sending an MQTT message to the BF/image/senddelay topic. The payload should contain an integer representing the delay in seconds.

To trigger immediate frame sending, send an MQTT message with the payload sendnow to the BF/image/sendnow topic.

## MQTT Topics
video_frames: The MQTT topic where video frames are published.
BF/image/senddelay: Send an MQTT message with an integer payload to set the frame sending delay.
BF/image/sendnow: Send an MQTT message with the payload sendnow to trigger immediate frame sending.
## Customization
You can customize the MQTT broker settings by modifying the `mqtt_broker_address`, `mqtt_client.username_pw_set()`, and port values in the script.

Modify the default delay by changing the default_delay value.

Customize error handling, logging, and exception messages as needed.

## Troubleshooting
If you encounter any issues while running the script, consider the following:

- Ensure that the RTSP links are valid and accessible.
- Verify that the MQTT broker is running and accessible from the network.
- Check the script's logging for error messages and debugging information.

## Contributing
Contributions to this project are welcome. You can contribute by submitting bug reports, feature requests, or pull requests. Please review the Contributing Guidelines for more information.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code according to the terms of the license.
