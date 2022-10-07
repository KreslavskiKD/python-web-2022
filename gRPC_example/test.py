# -*- coding: utf-8 -*-

import json

import urllib3

http = urllib3.PoolManager()


def main():
    for _ in range(10):
        r = http.request(
            "POST",
            "http://127.0.0.1:5005/TestService/GetAnekdote",
            headers={"Content-Type": "application/json"},
            body=json.dumps({"theme": "stirlitc"}),
        )
        print(r.data.decode("utf-8"))


if __name__ == "__main__":
    main()
