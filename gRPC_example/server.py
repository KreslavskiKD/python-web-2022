# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from fakedb import db
from random import seed
from random import randint

import grpc

from definitions.builds.service_pb2 import Anekdote
from definitions.builds.service_pb2_grpc import (
    TestServiceServicer,
    add_TestServiceServicer_to_server,
)

seed(533)


class Service(TestServiceServicer):
    def Health(self, request, context):
        return request

    def GetAnekdote(self, request, context):
        anekdote = db[request.theme][randint(0, db[len(request.theme)])]
        return Anekdote(anekdote)


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("localhost:5005")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
