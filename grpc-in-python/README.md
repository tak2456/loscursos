## Protocol Buffer
https://github.com/protocolbuffers/protobuf

## RPT/gRPC
RPC : Remote Procedure Call
gRPC: from Google, HTTP/2


HTTP/2
 - Binary frames
 - Header compression
 - Multiplexing
 - Request prioritization
 - Server push
 - Secure
 - http://www.http2demo.io/

## Links
https://github.com/fullstorydev/grpcurl
https://www.postman.com/
https://buf.build/
https://openssl.org/
https://github.com/grpc-ecosystem/grpc-gateway/


## protcol buffer (.proto)
```
protoc --version
protoc --python_out=. rides.proto

pip install protobuf
```

```
$ which python
.../grpc-in-python/env/Scripts/python
(env) 
$ which python3
/c/Users/.../AppData/Local/Microsoft/WindowsApps/python3
(env) 
```

## VS Code
Debug:Start Without Debugging : CTRL + F5
.vscode/settings.json
```
{
    "python.analysis.extraPaths": [
        "./protodefs"
    ],
    "python.languageServer": "Pylance"
}
```

### Behavior Explanation
Field is Set: If you set the type field to pb.REGULAR (which is 0), it might not show up because the default value for that field is also 0.
Default Field Handling: In protobuf, only fields that differ from their default values are shown in the output. If the field's value is 0, it may be omitted entirely from the string representation.

```python 
$python scripts/server.py
2024-10-28T22:20:00 - INFO - <module> - server ready on [::]:8888
```

### grpcurl
```sh
$ /d/Tools/grpcurl_1.9.1_windows_x86_64/grpcurl.exe --version
grpcurl.exe v1.9.1

$ /d/Tools/grpcurl_1.9.1_windows_x86_64/grpcurl.exe -plaintext localhost:8888 list Rides
Rides.Start

$grpcurl.exe -plaintext localhost:8888 describe .StartRequest
StartRequest is a message:
message StartRequest {
  int64 car_id = 1;
  string driver_id = 2;
  repeated string passenger_ids = 3;
  .RideType type = 4;
  .Location location = 5;
  .google.protobuf.Timestamp time = 6;
}

$grpcurl.exe -plaintext -d @ localhost:8888  Rides.Start < ../inputs/request.json
{
  "id": "d1d79b0282494cde873f4d23ceaf69cf"
}

# with https
$grpcurl.exe -insecure -d @ localhost:8888  Rides.Start < inputs/request.json
```


### how to share
- mono repo
- git submodule 
- python package
