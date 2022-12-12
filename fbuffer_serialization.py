import os
import sys
#sys.path.append(os.path.join(os.path.dirname(_file_), '/home/Apps/flatbuffers/python'))
sys.path.append(os.path.join (os.path.dirname(__file__), '/home/Apps/flatbuffers/python'))
import flatbuffers
import time
import numpy as np
import zmq

from applnlayer.ApplnMessageTypes import GroceryOrderMessage
from applnlayer.ApplnMessageTypes import HealthStatusMessage
from applnlayer.ApplnMessageTypes import ResponseMessage

import GroceryAppProto.grocery_Message as gom
import GroceryAppProto. milktypeAndQuantity as mktq
import GroceryAppProto.breadtypeAndQuantity as bdtq
import GroceryAppProto.meattypeAndQuantity as mttq
import HealthAppProto.health_Message as hs
import ResponseAppProto.response_Message as rm

def grocery_serialization (order):

    builder=flatbuffers.Builder (0)

    name_field=builder.CreateString(order.msg_type)
    milk_name=builder.CreateString(order.milk[0])
    bread_name=builder.CreateString(order.bread[0])
    meat_name=builder.CreateString(order.meat[0])
    mktq.Start (builder)
    mktq.AddType(builder,milk_name)
    mktq.AddQuantity(builder,order.milk[1])
    milkType=mktq.End(builder)
    
    bdtq.Start (builder)
    bdtq.AddType(builder,bread_name)
    bdtq.AddQuantity(builder,order.bread[1])
    breadType=bdtq.End(builder)
    
    mttq.Start (builder)
    mttq.AddType(builder,meat_name)
    mttq.AddQuantity(builder,order.meat[1])
    meatType=mttq.End(builder)
    

    gom.Start (builder)
    gom.AddMsgType(builder,name_field)
    gom.AddTomato(builder,order.tomato)
    gom.AddCucumber(builder,order.cucumber)
    gom.AddOnion(builder,order.onion)
    gom.AddGreenBean(builder,order.green_bean)
    gom.AddBroccoli(builder,order.broccoli)
    gom.AddJalapineo(builder,order.jalapineo)
    gom.AddCoke(builder,order.coke)
    gom.AddBeer(builder,order.beer)
    gom.AddDietCoke(builder,order.diet_coke)
    gom.AddSprite(builder,order.sprite)
    gom.AddRootBeer(builder,order.root_beer)
    gom.AddLemonade(builder,order.lemonade)
    gom.AddMilk(builder,milkType)
    gom.AddBread(builder,breadType)
    gom.AddMeat(builder,meatType)
    serialized_gom=gom.End(builder)

    builder.Finish(serialized_gom)

    buf=builder.Output()

    return buf

def grocery_serialize_to_frames (order):
    print("serialize grocery order to iterable list")
    return [grocery_serialization(order)]



def grocery_deserialize(buf):

    order=GroceryOrderMessage()
    packet=gom.grocery_Message.GetRootAs(buf,0)
    order.msg_type=packet.MsgType
    order.tomato=packet.Tomato
    order.cucumber=packet.Cucumber
    order.onion=packet.Onion
    order.green_bean=packet.GreenBean
    order.broccoli=packet.Broccoli
    order.jalapineo=packet.Jalapineo
    order.coke=packet.Coke
    order.beer=packet.Beer
    order.diet_coke=packet.DietCoke
    order.sprite=packet.Sprite
    order.root_beer=packet.RootBeer
    order.lemonade=packet.Lemonade
    order.milk=packet.Milk
    order.bread=packet.Bread
    order.meat=packet.Meat

    return order

def grocery_deserialize_from_frames(recvd_seq):

    assert(len(recvd_seq)==1)
    order=grocery_deserialize(recvd_[0])

    return order

def health_serialize(status):
    
    builder=flatbuffers.Builder (0)

    name_field=builder.CreateString(status.msg_type)
    dispenser_field=builder.CreateString(status.dispenser)
    lightbulb_field=builder.CreateString(status.lightbulb)
    sensor_field=builder.CreateString(status.sensor_status)

    hs.Start(builder)
    hs.AddMsgType(builder,name_field)
    hs.AddDispenser(builder,dispenser_field)
    hs.AddIcemaker(builder,status.icemaker)
    hs.AddLightbulb(builder,lightbulb_field)
    hs.AddFridgeTemp(builder,status.fridge_temp)
    hs.AddFreezerTemp(builder,status.freezer_temp)
    hs.AddSensorStatus(builder,sensor_field)
    hs.AddPower(builder,status.power)
    
    serialized_hs=hs.End(builder)

    builder.Finish(serialized_hs)

    buf=builder.Output()

    return buf


def health_serialize_to_frames (status):
    print("serialize health status to iterable list")
    return [health_serialize(status)]



def health_deserialize(buf):

    status=HealthStatusMessage()
    packet=hs.health_Message.GetRootAs(buf,0)
    status.msg_type=packet.MsgType
    status.dispenser=packet.Dispenser
    status.icemaker=packet.Icemaker
    status.lightbulb=packet.Lightbulb
    status.fridge_temp=packet.FridgeTemp
    status.freezer_temp=packet.FreezerTemp
    status.sensor_status=packet.SensorStatus
    status.power=packet.Power
   

    return status


def health_deserialize_from_frames(recvd_seq):

    assert(len(recvd_seq)==1)
    status=health_deserialize(recvd_[0])

    return status

def response_serialize (response):

    builder=flatbuffers.Builder (0)

    name_field=builder.CreateString(response.contents)
    name_code=builder.CreateString(response.code)

    rm.Start(builder)
    rm.AddCode(builder,name_code)
    rm.AddContents(builder, name_field)
    serialized_rm=rm.End(builder)

    builder.Finish(serialized_rm)

    buf=builder.Output()

    return buf


def response_serialize_to_frames (response):
    print("serialize health status to iterable list")
    return [response_serialize(response)]


def response_deserialize(buf):

    response=ResponseMessage(0,None)
    packet=rm.response_Message.GetRootAs(buf,0)
    response.code=packet.Code
    response.contents=packet.Contents

    return response


def response_deserialize_from_frames(recvd_seq):

    assert(len(recvd_seq)==1)
    response=response_deserialize(recvd_[0])

    return response
    


    

