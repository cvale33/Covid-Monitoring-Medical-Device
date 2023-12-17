# Covid-Monitoring-Medical-Device

**Project Description**

This project aims to develop an IoT device designed to evaluate an individual's COVID-19 risk by analyzing their daily activities and interactions. The device is engineered to promote compliance with public health guidelines, ultimately mitigating the transmission of the virus. Using electromagnetic radiation, it detects nearby individuals, measures their body temperature, and ensures a safe distance of at least two meters from the user. Additionally, the device tracks the user's location to assess potential exposure to COVID-19. Leveraging the gathered data, the device informs the user of their current risk level and issues warnings in case of possible exposure.

**Components**

The sensors gather data and send it to the Raspberry Pi, which then sends the information through a payload to the IoT Hub. This data is updated every two seconds and displayed to the user through the IoT Hub. The implementation of this process is included in the SensorToCloud.py file. For more detailed information, please refer to the Project Design PDF and Project Proposal PDF.

**How to set it up**

Setting up a Raspberry Pi according to the provided diagram involves both hardware and software tasks. Assemble the required components, connect GPIO pins as per the diagram, and install Raspbian OS on an SD card. After the initial boot and setup, update the OS, and install necessary packages such as RPi.GPIO for GPIO access and Azure IoT Device SDK for Azure integration. Create an Azure account, set up an IoT Hub service, and generate a connection key for device authentication. Modify the Python code to include the generated connection key, then run the script on the Raspberry Pi to collect data from sensors and send it to the Azure IoT Hub for processing. The exact steps and configurations may vary based on your project's specifics, so consulting relevant documentation is essential for a successful setup and data collection process.

**Technologies Used**

- Python: Used to gather the data from the GPIO pins and calculate the distance measured by the ultrasonic sensor using the pulse duration.
- Raspberry Pi 3 model B (Raspian OS): The GPIO pins were utilized to retrieve data and supply power to the sensors mounted on the breadboard.
- Libraries: Python Library, Raspberry Pi GPIO Library, the Azure IoT Device SDK (both the regular and asynchronous versions), gpsd-py3 for handling GPS data
- Sensors: GPS, PIR and Ultrasonic
- Azure Cloud IoT Hub, AMQP Protocol was used for communication
- Power BI Data Visualization

 <img width="806" alt="Screen Shot 2023-12-17 at 6 42 15 PM" src="https://github.com/cvale33/Covid-Monitoring-Medical-Device/assets/151482050/f5fc762a-f066-4eb9-b172-eb3a95c245b0">
<img width="831" alt="Screen Shot 2023-12-17 at 6 43 12 PM" src="https://github.com/cvale33/Covid-Monitoring-Medical-Device/assets/151482050/566166c1-6b9c-4d8d-80e1-014f9d7f64bd">
