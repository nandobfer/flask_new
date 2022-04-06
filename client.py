from urllib.request import urlopen

handler_url = 'http://localhost:7171/testing_comms/'

class Client():
    def __init__(self, name):
        self.name = name

    def run(self):
        global handler_url

        url = handler_url + '?name=' + self.name
        file = urlopen(url)
        received = file.read()
        print(received)
        file.close()

client = Client(input('Digite seu nome: '))
client.run()