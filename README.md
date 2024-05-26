# Travel Recommendation

## Installation

### Install makefile

#### On window  

Install chocolatey: https://docs.chocolatey.org/en-us/choco/setup#more-install-options  

Install makefile using chocolatey

```
choco install make
```

#### On macos
Install homebrew: https://docs.brew.sh/Installation

Install makefile using homebrew

```
brew install make
```

### Install docker

https://docs.docker.com/get-docker/


## Setup

### Using local env


Install python3 with version >= 3.9.0

#### Create virtualenv
```
python3 -m venv venv
```

#### Activate virtualenv

On Window
```
venv\Scripts\activate
```

On MacOS/Linux
```
source venv/bin/activate
```

#### Install dependencies
```
make install
```

#### Run server

```
make run
```

  Run server with reload mode
```
make run-reload
```

### Using docker

#### Build docker image
```
make build
```

#### Run server
```
make up
```

Sample API curl
```
curl --location 'localhost:3000/recommendations?country=CO&season=winter'

```

### Run tests

```
make test
```

#### Run tests with coverage

```
make test-cov
```