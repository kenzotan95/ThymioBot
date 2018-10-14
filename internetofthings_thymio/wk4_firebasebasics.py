from firebase import firebase

url = "https://dw-iot-test.firebaseio.com/" # URL to Firebase database
token = "xm1xX28S9hfstimrwGA1fJBHCXCt76wHkhrEXNXS" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

print("Reading from my database.")
print(firebase.get('/age')) # get the value from node age
print(firebase.get('/name')) # get the value from node name
print(firebase.get('/facts_about_me')) # get the value from node facts_about_me
firebase.put('/', 'lazy', True) # put the value True into node lazy
firebase.put('/', 'pie', 3.14) # put the value 3.14 into node pie
