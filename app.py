import os

message = os.getenv("MESSAGE", "Hello from Docker!")

print(message)
