from django.db import models
from django.urls import reverse
import mysql.connector
import paho.mqtt.client as mqtt
from datetime import datetime

from humidityControl.models import HumidityLog, ValveLog, Terrarium
from celery.task.schedules import crontab
from celery.decorators import periodic_task

@periodoc_task(run_every=(crontab(second='*/20')), name="broker", ignore_result=True)
def brokerMQTT(address):
    def mysql_connection_humidityLog(payload):
        HumidityLog.objects.create(terrarium_id='7', date=datetime.now(), humidity=payload)

    def mysql_connection_valveLog(payload):
        ValveLog.objects.create(terrarium_id='7', date=datetime.now(), actionRequested=payload)

    def on_connect(mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def on_message(mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        mysql_connection_humidityLog(msg.payload)
        action_valve = SensorValueToValveAction(int(msg.payload), 10)
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


def SensorValueToValveAction(sensor_value=int(), terrarium_id=int()):
    action = int
    max_humidity = Terrarium.objects.get(pk=terrarium_id).animal.maxHumidity
    min_humidity = Terrarium.objects.get(pk=terrarium_id).animal.minHumidity
    if sensor_value > max_humidity:
        action = 0
    elif sensor_value < min_humidity:
        action = 1
    return action


while True:
    brokerMQTT("139.162.240.68")
