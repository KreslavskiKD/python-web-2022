# HW 3
________________________________________________________________________________________

A dummy example of a Python API using gRPC to get anekdotes (haha)


Compile the .proto files...
```
python -m grpc_tools.protoc -I definitions/ --python_out=definitions/builds/ --grpc_python_out=definitions/builds/ definitions/service.proto
```

Start the server.
```
python server.py 
```

