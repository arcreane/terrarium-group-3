import mysql.connector
import paho.mqtt.client as mqtt
from datetime import datetime

mydb = mysql.connector.connect(
    host="139.162.240.68",
    user="terrariumUser",
    password="lorette",
    database="terrarium"
)


def brokerMQTT(address):
    def mysql_connection_humidityLog(payload):
        mycursor = mydb.cursor()

        sql = ("INSERT INTO humidityControl_humiditylog (date, humidity, terrarium_id)"
               "VALUES (%s, %s, %s)")
        val = (datetime.now(), payload, "1")
        mycursor.execute(sql, val)

        mydb.commit()
        print(payload)
        print(mycursor.rowcount, "record updated")
        mycursor = mydb.cursor()
        sql3 = "UPDATE humidityControl_terrarium SET currentHumidity = %s WHERE id= %s"
        val = (payload, '1')
        mycursor.execute(sql3, val)

        mydb.commit()

    def mysql_connection_valveLog(payload):
        mycursor = mydb.cursor()

        sql = ("INSERT INTO humidityControl_valvelog (date, actionRequested, terrarium_id)"
               "VALUES (%s, %s, %s)")
        val = (datetime.now(), payload, "1")
        mycursor.execute(sql, val)

        mydb.commit()
        print(payload)
        print(mycursor.rowcount, "record updated")

    def on_connect(mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def on_message(mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        mysql_connection_humidityLog(msg.payload)
        action_valve = SensorValueToValveAction(msg.payload, '1')
        mysql_connection_valveLog(action_valve)
        mqttValve.publish("humidity", action_valve)

    def on_publish(mqttc, obj, mid):
        print("mid: " + str(mid))

    def on_subscribe(mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_log(mqttc, obj, level, string):
        print(string)

    mqttSensor = mqtt.Client()
    mqttSensor.on_message = on_message
    mqttSensor.on_connect = on_connect
    mqttSensor.on_publish = on_publish
    mqttSensor.on_subscribe = on_subscribe

    mqttValve = mqtt.Client()
    mqttValve.on_message = on_message
    mqttValve.on_connect = on_connect
    mqttValve.on_publish = on_publish
    mqttValve.on_subscribe = on_subscribe

    mqttSensor.connect(address, 1883, 60)
    mqttSensor.subscribe("humidity", 0)

    mqttSensor.loop_forever()


def SensorValueToValveAction(sensor_value=int(), terrarium_id=str()):
    max_humidity = int()
    min_humidity = int()
    animalID = int()
    mycursor = mydb.cursor(buffered=True)

    sql = "SELECT animal_id FROM humidityControl_terrarium WHERE id=%s"
    val = (terrarium_id,)
    mycursor.execute(sql, val)
    animalID = mycursor.fetchall()
    sql1 = "SELECT maxHumidity, minHumidity FROM humidityControl_animaltohumidity WHERE id=%s"
    val = (animalID,)
    mycursor.execute(sql1, val)
    max_humidity = mycursor.fetchone(1)
    min_humidity = mycursor.fetchone(2)

    if int(sensor_value) >= int(max_humidity):
        action = animalID
        return action
    elif int(sensor_value) <= int(min_humidity):
        action = 1
        return action
    else:
        action = 2
        return action


while True:
    brokerMQTT("139.162.240.68")
