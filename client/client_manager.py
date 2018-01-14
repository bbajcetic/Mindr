import yaml
import requests
import json
from nwhacks2018.client.ernn.constants import *


class ClientHelper:
    duration = 1
    update_frequency = 15
    time_since_update = 0
    trigger_threshold = 0.8
    total_run_time = 0
    client_id = "00:00:00:00:00:00"

    def __init__(self):
        self.load_config()

    def end_execution(self):
        self.save_config()

    def update(self, results):
        print("UPDATING!!!!!!!")
        payload = dict(zip(EMOTIONS, results))
        #PUSH TO SERVER
        url = ''
        r = requests.post(url, data=json.dumps(self.client_id, payload))
        if r.status_code == 200:
            print("something may have happened, and it may have been a positive or negative experience")

        self.time_since_update = 0
        self.total_run_time += self.update_frequency

    def emergency_update(self, results, frame):
        print("emergencyUpdate")
        payload = dict(zip(EMOTIONS, results))
        #PUSH TO SERVER
        url = ''
        r = requests.post(url, data=json.dumps(self.client_id, payload, frame))
        if r.status_code == 200:
            print("something may have happened, and it may have been a positive or negative experience")


    def increment_time(self):
        if self.total_run_time / 60 >= self.duration:
            self.end_execution()
        self.time_since_update += 1

    def set_update_frequency(self, frequency):
        self.update_frequency = frequency

    def set_duration(self, hours):
        self.duration = hours

    def set_emergency_threshold(self, severity):
        if severity == 0:
            self.trigger_threshold = 0.8
        elif severity == 1:
            self.trigger_threshold = 0.6
        else:
            self.trigger_threshold = 0.4

    def load_config(self):
        try:
            data = open('data.yml', 'r')
            #data = yaml.load(stream)
            self.update_frequency = data["update_frequency"]
            self.duration = data["run_time"]
            self.trigger_threshold = data["trigger_threshold"]
        except IOError:
            self.update_frequency = 15
            self.duration = 1
            self.trigger_threshold = 0.8

    def save_config(self):
        data = dict(
            update_frequency=self.update_frequency,
            run_time=self.duration,
            sensitivity=self.trigger_threshold
        )
        with open('data.yml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)