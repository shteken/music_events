import pandas as pd
import pathlib
import json
import uuid
import datetime
import time
import random

users_file = pathlib.Path('./source_files/users.csv')
tracks_file = pathlib.Path('./source_files/tracks.csv')
df_users = pd.read_csv(users_file)
df_tracks = pd.read_csv(tracks_file)
max_event_rate = 10

def events(event_rate):
    def generate_event():
        df_random_user = df_users.sample(1).reset_index(drop=True)
        df_random_track = df_tracks.sample(1).reset_index(drop=True)
        df_event = pd.concat([df_random_user, df_random_track], axis=1)
        print(df_event)
        event = df_event.to_dict(orient='records')[0]
        event['eventID'] = str(uuid.uuid4())
        event['timestamp'] = str(datetime.datetime.utcnow())
        return json.dumps(event)

    for _ in range(event_rate):
        print(generate_event())

while True:
    n = random.randint(0, max_event_rate)
    m = random.uniform(0, 1)
    events(n)
    time.sleep(m)