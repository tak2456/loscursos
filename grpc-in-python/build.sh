#!/usr/bin/bash

# protoc --python_out=. protodefs/rides.proto
python -m grpc_tools.protoc \
    -I protodefs/ \
    --python_out=mygrpc \
    --grpc_python_out=mygrpc \
    protodefs/rides.proto
        