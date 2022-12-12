import os
import sys
import json


from applnlayer.ApplnMessageTypes import GroceryOrderMessage


def serialize(gom):

    json_buf ={
        "msg_type":gom.msg_type,
        "tomato":gom.tomato,
        "cucumber":gom.cucumber,
        "onion":gom.onion,
        "green_bean":gom.green_bean,
        "broccoli":gom.broccoli,
        "jalapineo":gom.jalapineo,
        "coke":gom.coke,
        "beer":gom.beer,
        "diet_coke":gom.diet_coke,
        "sprite":gom.sprite,
        "root_beer":gom.root_beer,
        "lemonade":gom.lemonade,
        "milk":gom.milk,
        "bread":gom.bread,
        "meat":gom.meat
        }
    return json.dumps(json_buf)


def deserialization (buf):

    json_buf=json.loads (buf)

    gom=GroceryOrderMessage()
    gom.msg_type=json_buf["msg_type"]
    gom.tomato=json_buf["tomato"]
    gom.cucumber=json_buf["cucumber"]
    gom.onion=json_buf["onion"]
    gom.green_bean=json_buf["green_bean"]
    gom.broccoli=json_buf["broccoli"]
    gom.jalapineo=json_buf["jalapineo"]
    gom.coke=json_buf["coke"]
    gom.beer=json_buf["beer"]
    gom.diet_coke=json_buf["diet_coke"]
    gom.sprite=json_buf["sprite"]
    gom.root_beer=json_buf["root_beer"]
    gom.lemonade=json_buf["lemonade"]
    gom.milk=json_buf["milk"]
    gom.bread=json_buf["bread"]
    gom.meat=json_buf["meat"]

    return gom
