# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

def filter_list(data_list):
  return_value = []
  for elem in data_list:
    try:
      return_value.append(int(elem))
    except ValueError:
      pass
  return return_value
