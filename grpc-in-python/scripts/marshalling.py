import sys
import os

from datetime import datetime

print("Protobuf import successful!")

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../protodefs'))
#project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../mygrpc'))
sys.path.insert(0, project_root)

import rides_pb2 as pb


print(pb.POOL)
print(pb.RideType.Name(pb.REGULAR))
print(pb.RideType.Value('POOL'))

loc = pb.Location(
    lat=12.345, 
    lng=67.890
)
print(loc)

request = pb.StartRequest(
    car_id=95,
    driver_id='McQueen',
    passenger_ids=['p1', 'p2', 'p3', 'p4'],
    type=pb.POOL,
    location=loc
)

time = datetime(2024, 10, 27, 23, 37, 42)
request.time.FromDatetime(time)
print(request)

#region ToDAteTime
time2 = request.time.ToDatetime()
print(type(time2), time2)
#endregion

# region now
print('Timestamp')
from google.protobuf.timestamp_pb2 import Timestamp
now = Timestamp()
now.GetCurrentTime()

print(f'current time: {now}')
print(f'current now.ToDatetime(): {now.ToDatetime()}')
# endregion

# region Marshal
data = request.SerializeToString()
print('type:', type(data))
print('size:', len(data))
print()
# endregion

# region Unmarshal
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)
# endregion
print(f"Date Recieved = {request2.time.ToDatetime()}")

# Print the type field after deserialization
print("Type (as enum value):", request2.type)  # This will print the integer value
print("Type (as string):", pb.RideType.Name(request2.type))  # This will print the string representation

# region json
from google.protobuf.json_format import MessageToJson
data = MessageToJson(request)
print('json:', data)
# endregion

# region size
print('encode size:')
print('- json     : ', len(data))
print('- protobuf : ', len(request.SerializeToString()))