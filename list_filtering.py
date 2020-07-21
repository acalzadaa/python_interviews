# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

def filter_list(data_list):
  index = 0
  returnValue = []
  for elem in data_list:
   
    try:
      returnValue.append(int(elem))
      index += 1

    except ValueError:
      pass
 
  return returnValue
