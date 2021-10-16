import random
import json

json_file = open('words.json')
words = json.loads(json_file)

for i in words['words']:
    print(i)