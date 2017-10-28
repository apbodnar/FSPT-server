import json
import math

frames = 600

def get_frame_config(frame_number):
    if frame_number > frames:
        return ""
    with open("FSPT/scene/mirror.json", "r") as fd:
        base = json.load(fd)
        bunny = base["animated_props"]["b1"]
        mirror = base["animated_props"]["p3"]
        left = base["animated_props"]["p1"]
        right = base["animated_props"]["p2"]
        floor = base["animated_props"]["p4"]
        bunny["rotate"][0]["angle"] = frame_number/30
        floor['reflectance'] = [
            0.5 * (math.sin(-frame_number/10) + 1),
            0.5 * (math.cos(frame_number / 10) + 1),
            0.5 * (math.sin(frame_number / 10) + 1)
        ]
        left['emittance'] = [
            2 * (math.sin(frame_number/60) + 1),
            2 * (math.cos(frame_number / 60) + 1),
            2 * (math.sin(-frame_number / 60) + 1)
        ]
        right['emittance'] = [
            2 * (math.cos(frame_number/60) + 1),
            2 * (math.sin(frame_number / 60) + 1),
            2 * (math.cos(-frame_number / 60) + 1)
        ]
        mirror['roughness'] = 0.125 * (math.sin(frame_number / 60) + 1)
        return json.dumps(base)