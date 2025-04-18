from exercitii_import import math_operations

print(math_operations.add(3123, 132))
print(math_operations.subtract(3123, 132))
import string_operations
print(string_operations.concatenate("Mario ","Mihai"))
import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.json())
