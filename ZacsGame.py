import requests 
import json
from math import sqrt 

import json
import requests
url = "http://10.88.111.131:8080/"
payload={"name":"Alessandro","token":"123"}
requests.post(url + "connect",json.dumps(payload))
print('Player Created')

all_treasures = requests.get(url+ "treasure")
all_treasures = all_treasures.json()
payload = {"name":"Alessandro","token":"246"}
token = "123" 

my_position = requests.get(url+ "players")
resp = my_position.json()
resp_filt = [x for x in resp if x['name'] == 'Alessandro'][0]
myposition = resp_filt['position']
print(myposition)

def move(direction,distance):
    RightList = range(distance)
    for number in RightList: 
       payload = {"token":token, "direction":direction}
       response = requests.post(url+"move", json = payload)

def distance(xy): 
    return sqrt(xy[0]**2 + xy[1]**2)

def relative_distance(myposition, treasure_position):
    x_offset = treasure_position[0] - myposition[0]
    y_offset = treasure_position[1] - myposition[1]
    return [x_offset, y_offset]


all_distances = [distance(relative_distance(myposition, treasure)) for treasure in all_treasures]

while len(all_treasures) > 0:
    all_distances = [distance(relative_distance(myposition, treasure)) for treasure in all_treasures]
    closest = [all_distances.index(x) for x in all_distances if x == min(all_distances)][0]
    print("Position of closest treasure in the list of treasures is {0}, trying to grab it".format(closest))
    xyaim = relative_distance(myposition, all_treasures[closest])
    xaim = xyaim[0]
    yaim = xyaim[1]
    if xaim < 0:
        move("left", abs(xaim))
    if xaim > 0:
        move("right",abs(xaim))
    if yaim < 0:
        move("down",abs(yaim))
    if yaim > 0: 
        move("up", abs(yaim))
    print("grabbed {0} successfully".format(closest))
    all_treasures.pop(closest)
    print("Removed treasure {0} from the list of treasures".format(closest))
    my_position = requests.get(url+"players")
    resp = my_position.json()
    resp_filt = [x for x in resp if x['name'] == 'Alessandro'][0]
    myposition = resp_filt['position']
    print("My new position is: {0}".format(myposition))


# make_player = {'name': 'Alessandro', 'token': '123'}
# response = requests.post(url+"connect") json=json.loads(make_player))
# print(response.text)

