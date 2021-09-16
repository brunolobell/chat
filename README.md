# CHAT

Simple chat application using python to Socket and React to GUI.

## Instalation

It is necessary to have installed [NPM](https://nodejs.org/en/download/), [Python3](https://www.python.org/downloads) and [pip](https://pip.pypa.io/en/stable).

### Enviroment Variables

``` bash
# SOCKET
HOST=127.0.0.1
PORT=5000
CONNECTIONS=100

# GUI
```

### Clone and install

``` bash
# Clone the repository
$ git clone https://github.com/brunolobell/chat.git

# Open directory
$ cd chat

# Install dependencies
# To Socket
$ pip install -r requirements.txt
# To GUI
$ npm install

```

## Usage

### Socket

``` bash
# Open directory config
$ cd config

# Run the socket
$ python server.py
```

### GUI

``` bash
# Run GUI
$ npm start

# In a browser
http://localhost:3000
```

## Developers

This application was developed by Bruno Machado Löbell and Johann Pinheiro Pires to subject distributed systems taught by Dr. Bruno Lopes Dalmazo.