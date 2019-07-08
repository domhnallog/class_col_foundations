###  Domhnall O'Donnchadha
###  20190604
###  Homework 3, Part 2

# 1. Let's say we are terrible doctors and we have a patient. Define a dictionary called patient that works with the following code:
#   print("Doctor, it looks like the patient named", patient['name'], "is complaining about", patient['complaint'])
patient1 = {
  'name': 'Bart Simpson',
  'complaint': 'recurrent neck pain'
}
print(f"Doctor, it looks like the patient named {patient1['name']} is complaining about {patient1['complaint']}.")

# 2. We aren't really listening to their complaint, but as more test results come in, we'll add these things to the patient's record. Add to the patient dictionary, do not create a new dictionary - each one of these should be added to existing dict on a separate line.
patient1['heart rate'] = 70
patient1['temperature'] = 98.6
patient1['infection'] = False

# 3. Now let's be doctors! Diagnose the patient, and store your diagnosis in a key called 'diagnosis':
#     If their temperature is above 102 but they do not have an infection, they have heat stroke.
#     If they have a temperature above 102 and they have an infection, they have the flu.
#     If they have an infection but a normal temperature, it's probably a cold.
#     If none of the above, tell them to take an aspirin and call you in the morning.
if patient1['temperature'] > 102: 
  if patient1['infection'] == True:
    patient1['diagnosis'] = 'flu'
  else:
    patient1['diagnosis'] = 'heat stroke'
elif patient1['temperature'] <= 102:
  if patient1['infection'] == True: 
    patient1['diagnosis'] = 'probably a cold'
  else:
    patient1['diagnosis'] = 'unknown; take an aspirin and call me in the morning'

print(f"Your diagnosis is {patient1['diagnosis']}.")

# 4. Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an infection or not (this will be a list of dictionaries). Use a for loop to diagnose each of them.

patients = [{
    'name': 'Barry Duffman',
    'complaint': 'uncontrolled voice modulation',
    'heart rate' : 152,
    'temperature' : 103.5,
    'infection': False
  }, {
    'name': 'Jeff Albertson',
    'complaint': 'chest pains',
    'heart rate' : 130,
    'temperature' : 101.0,
    'infection': False
  }, {
    'name': 'Marvin Monroe',
    'complaint': 'body aches, touch of agoraphobia',
    'heart rate' : 95,
    'temperature' : 102.2,
    'infection': True
  }]
# patients = [patient1, patient2, patient3, patient4]

for patient in patients:
  if patient['temperature'] > 102: 
    if patient['infection'] == True:
      patient['diagnosis'] = 'flu'
    else:
      patient['diagnosis'] = 'heat stroke'
  elif patient['temperature'] <= 102:
    if patient['infection'] == True: 
      patient['diagnosis'] = 'probably a cold'
    else:
      patient['diagnosis'] = 'unknown; take an aspirin and call me in the morning'
  print(f"{patient['name']}, your diagnosis is {patient['diagnosis']}.")