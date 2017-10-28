import json
import math

frames = 600

def get_frame_config(frame_number):
    if frame_number > frames:
        return ""
    with open("FSPT/scene/bunnies.json", "r") as fd:
        base = json.load(fd)
        b1 = base["animated_props"]["p1"]
        b2 = base["animated_props"]["p2"]
        b3 = base["animated_props"]["p3"]

        light = base["animated_props"]["l1"]
        light["translate"][0] = math.sin(frame_number / 60)
        light["translate"][2] = math.cos(frame_number / 60)

        b1["rotate"][0]["angle"] = frame_number / 30
        b2["rotate"][0]["angle"] = frame_number / 30
        b3["rotate"][0]["angle"] = frame_number / 30

        b1["translate"][2] = math.sin(30 * frame_number / frames)
        b2["translate"][2] = math.cos(30 * frame_number / frames)
        b3["translate"][2] = -math.cos(30 * frame_number / frames)
        return json.dumps(base)