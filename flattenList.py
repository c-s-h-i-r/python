def flatten(list):
  return [item for sublist in list for item in sublist]
  
print flatten([[1,[1,[1,2]]]])