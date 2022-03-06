import random

print([1, 6, 0, 8, -8, 0])
codes = [200, 301, 400, 401, 403, 404, 408, 500, 502, 504]
rand = random.randrange(0, len(codes))
messages = ["OK", "Moved Permanently", "Bad Request", "Unauthorized", "Forbidden", "Not Found", "Request Timeout",
            "Internal Server Error", "Bad Gateway", "Gateway Timeout"]
print(str(codes[rand]) + " " + messages[rand])
