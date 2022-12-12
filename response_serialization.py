import os
import sys
import json

from applnlayer.ApplnMessageTypes import ResponseMessage

def serialization(rm):

    json_buf={
        "code":rm.code,
        "contents":rm.contents
        }
    return json.dumps(json_buf)


def deserialization (buf):

    json_buf = json.loads(buf)

    rm=ResponseMessage(0,None)
    rm.code=json_buf["code"]
    rm.contents=json_buf["contents"]

    return rm
        


