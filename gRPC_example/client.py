import grpc

from definitions.builds.service_pb2 import Null, RequestForAJoke
from definitions.builds.service_pb2_grpc import TestServiceStub


def main():
    with grpc.insecure_channel(
        "localhost:5005", options=(("grpc.enable_http_proxy", 0))
    ) as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        for _ in range(5):
            anekdote = client.GetAnekdote(
                RequestForAJoke(
                    theme="stirlitc",
                )
            )

            print(anekdote.anekdote)

        for _ in range(5):
            anekdote = client.GetAnekdote(
                RequestForAJoke(
                    theme="watson",
                )
            )

            print(anekdote.anekdote)


if __name__ == "__main__":
    main()
