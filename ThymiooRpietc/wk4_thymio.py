from pythymiodw import *
from time import sleep
from firebase import firebase

url = 'https://lol123-c47e1.firebaseio.com' # URL to Firebase database
token = 'NMx1wXVgr5tP1u4rzKH98kHC2lHyz95B2jklRjvy' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

robot = ThymioReal() # create an eBot object

no_movements = True

while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here
    movement_list=firebase.get('/movement_list')
    
    if movement_list == 0:
        robot.sleep(0.5)
    else:
        no_movements=False

# Write the code to control the eBot here
data = firebase.get('/movement_list')
print(data)
print(firebase.get('/'))
firebase.put('/','movement_list',None)#deletes existing data from the firebase
sleep(1)
print(firebase.get('/'))
#ls = data['movement_list']
for i in data:
    if i == 'left':
        robot.wheels(-100,100)
        sleep(1)
    if i == 'up':
        robot.wheels(100,100)
        sleep(1)
    if i == 'right':
        robot.wheels(100,-100)
        sleep(1)
robot.quit()

##def two(speed, duration):
##    
##    robot.wheels(speed, speed)
##    robot.sleep(duration)
##
##    robot.wheels(100,100)
##    robot.sleep(1)
##    
##def one(speed, duration):
##    
##    robot.wheels(speed, speed)
##    robot.sleep(duration)
##    
##    robot.wheels(-100,100)
##    robot.sleep(1)
##
##def three(speed, duration):
##    
##    robot.wheels(speed, speed)
##    robot.sleep(duration)
##    
##    robot.wheels(100,-100)
##    robot.sleep(1)
##
##for val in movement_list:
##    if val == one:
##        return one
##    elif val == two:
##        return two
##    else:
##        return three
    
# 2'up' movement => robot.wheels(100, 100)
# 1'left' movement => robot.wheels(-100, 100)
# 3'right' movement => robot.wheels(100, -100)
