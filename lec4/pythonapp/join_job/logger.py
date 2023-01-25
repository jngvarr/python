from datetime import datetime as dt
from time import time
import os

path = os.path.dirname(os.path.abspath(__file__))

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path+'\log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path+'\log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(path+'\log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))
