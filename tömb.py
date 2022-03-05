import random

print([1, 6, 0, 8, -8, 0])
codes = [200, 301, 400, 401, 403, 404, 408, 500, 502, 504]

response =codes[random.randrange(0, len(codes))]
print(response)
if response == 200:
    print("OK")
elif response == 301:
    print("Moved Permanently")
elif response == 400:
    print("Bad Request")
