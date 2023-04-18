# import requests


# def make_request():
#     # ⛔️ AttributeError: partially initialized module 'requests'
#     # has no attribute 'get' (most likely due to a circular import)
#     res = requests.get('https://reqres.in/api/users')

#     parsed = res.json()

#     print(parsed)


# make_request()


import requests

# 👇️ ['__builtins__', '__cached__', '__doc__', '__file__',
#  '__loader__', '__name__', '__package__', '__spec__', 'requests']
print(dir(requests))