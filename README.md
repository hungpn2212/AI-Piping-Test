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


### Install python3 with version >= 3.9.0

## Setup
### Clone the project to your local machine
```bash
git clone https://github.com/hungpn2212/AI-Piping-Test ai-piping
```
### Navigate to the project
```bash
cd ai-piping
```

### Add env
Create **.env** file in the project's root directory and copy env variables from **.env_sample** file

```bash
 cp .env_sample .env
```
Add OPENAI_API_KEY env (Required) and model name (optional) inside .env file
```
  OPENAI_API_KEY=<Insert OpenAI API Key here>
```  

### Using local env

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