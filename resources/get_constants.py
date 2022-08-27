import json
import os
import pathlib

os.chdir(pathlib.Path(__file__).parent.absolute())

with open(r'track_list.json','r') as track_list:
    TRACK_LIST_LIST = json.loads(track_list.read())

NUMBER_OF_TRACKS = sum([len(sublist) for sublist in TRACK_LIST_LIST])

TRACK_LIST = [track for tracklist in TRACK_LIST_LIST for track in tracklist]