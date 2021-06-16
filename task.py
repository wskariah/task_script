import os
import json

with open('data/data.json') as f:
  data = json.load(f)

for i in data['data']:
    print(i)

# sorting using custom key
task_list = [
    {'1. setup': 'Lets setup the docker', '2. create': 'create docker file', '3. define': 'Now define the services in compose file', '4. build_run': 'now run docker-compose up'},
]

# custom functions to get the docker setup info
def get_setup(task_list):
    return task_list.get('setup')


def get_create(task_list):
    return task_list.get('create')


def get_define(task_list):
    return task_list.get('define')

def get_build_run(task_list):
    return task_list.get('build_run')

# sort Descending order
task_list.sort(key=get_define, reverse=True)
print(task_list, end='\n\n')