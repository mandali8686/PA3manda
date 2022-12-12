import os
import sys
import json

from applnlayer.ApplnMessageTypes import HealthStatusMessage

def serialization(hs):

    json_buf={
        "msg_type":hs.msg_type,
        "dispenser":hs.dispenser,
        "icemaker":hs.icemaker,
        "lightbulb":hs.lightbulb,
        "fridge_temp":hs.fridge_temp,
        "freezer_temp": hs.freezer_temp,
        "sensor_status":hs.sensor_status,
        "power":hs.power
        }
    return json.dumps(json_buf)


def deserialization (buf):

    json_buf = json.loads(buf)

    hs=HealthStatusMessage()
    hs.msg_type=json_buf["msg_type"]
    hs.dispenser=json_buf["dispenser"]
    hs.icemaker=json_buf["icemaker"]
    hs.lightbulb=json_buf["lightbulb"]
    hs.fridge_temp=json_buf["fridge_temp"]
    hs.freezer_temp=json_buf["freezer_temp"]
    hs.sensor_status=json_buf["sensor_status"]
    hs.power=json_buf["power"]

    return hs
        


