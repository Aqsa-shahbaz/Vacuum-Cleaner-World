def vacuumcleaner(data):

  actions = []  # List to store the actions taken
  status = "clean"  # Initial status of the vacuum cleaner

  for i in data:    # Iterate through each percept in the data
    actions.append({'Percept ':  i})  
    if i == ['A', 'Clean']:  # Check conditions based on percept and take corresponding action
      actions.append({'Action ':'Right'})
    elif i== ['A', 'Dirty']:
      actions.append({'Action':'Suck'})
      status = 'Clean'
    elif i == ['B', 'Clean']:
      actions.append({'Action ':'Left'})
    else:
      actions.append({'Action':'Suck'})
      status = 'Clean'

  return actions

arr=[] # List to store percept sequences
op = input ('Enter how many times you want to perform the actions: ')
op = int(op)
for i in range (op):
  data = input ('Enter percept sequence (e.g., A Clean, A Dirty, B Clean):')
  data = [i.split() for i in data.split(', ')]
  arr.append(data)

for i in  arr:
  result = vacuumcleaner(i) #call vacuum cleaner function for each percept sequence
  print (result)