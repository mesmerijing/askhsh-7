import urllib.request
import json

with urllib.request.urlopen("https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY") as url:
    data = json.loads(url.read().decode())

# for key, value in data.items():
#     print(key)

total_elements = data['page']['total_elements']

total_hazardous_objects = 0
max_objects_velocity = float(0)
max_diameter = -1
max_velocity_Obj_Name = ''
max_diameter_Obj_Name = ''

for i in data['near_earth_objects']:
    if i['is_potentially_hazardous_asteroid']:
        total_hazardous_objects += 1
    # print(float(i['close_approach_data'][0]['relative_velocity']['kilometers_per_second']))
    # print(max_objects_velocity)
    if float(i['close_approach_data'][0]['relative_velocity']['kilometers_per_second']) > float(max_objects_velocity):
        max_objects_velocity = i['close_approach_data'][0]['relative_velocity']['kilometers_per_second']
        max_velocity_Obj_Name = i['name']

print("Object ",max_velocity_Obj_Name," has max velocity of ", max)
print(total_hazardous_objects)
