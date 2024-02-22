import json


array= []
with open('miserables.json') as json_file:
    data = json.load(json_file)
    
nodes = data['nodes']
links = data['links']
# for key,value in data:
#     array 
    
    
print(links)