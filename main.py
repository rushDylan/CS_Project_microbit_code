from microbit import *
import csv

FILENAME = "Project_data.csv"
MIN_LIGHT_THRESHOLD = 0
MAX_LIGHT_THRESHOLD = 255

def write_to_csv(light_level):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([light_level])

num_samples = 10

def collect_light_data():
    light_data = []
    for _ in range(num_samples):
        light_data.append(display.read_light_level())
        sleep(100)
    return sum(light_data) / num_samples

while True:
    average_light = collect_light_data()

    pin1.write_digital(average_light == MAX_LIGHT_THRESHOLD)

    print("Light Level:", average_light)

    write_to_csv(average_light)

    sleep(5000)
    