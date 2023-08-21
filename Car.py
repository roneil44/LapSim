import yaml
import math

from yaml import load

# Load car setup into a new class

class Car:
    def __init__(self, file_path, name='Car1'):
        # initialize new instance of car
        self.file_path = file_path
        self.name = name

        # automatically load car data
        self.Information = self.load_car(file_path)

    def load_car(self, file_path):
        # takes a file path and loads data from yaml config file into Car class
        with open(file_path, 'r') as file:
            CarDetails = yaml.safe_load(file)
        return(CarDetails)