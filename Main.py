

### Main file for running simulation events ###
# Import car data
from Car import Car


CarData = Car(file_path='CarConfig.yml',name='fsae')
print(CarData.Information)
print(CarData.name)

