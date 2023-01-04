
# Python Docker Application

## Getting started

1. Clone the repository:

```
git clone git@github.com:babanila/python-docker-sample.git
```

2. Install the dependencies:

```
 pip3 install -r requirements.txt
```

3. Running app locally without docker:

```
 python3 app.py
```

## Build the docker image

    - docker build -t babanila/python-docker-sample .

    - docker run -p 5000:5000 babanila/python-docker-sample:v1.0.0

## Build and run docker image with specific version

    - docker build -t babanila/python-docker-sample:v1.0.0 .

    - docker run -p 5000:5000 babanila/python-docker-sample:v1.0.0

## Run container in detached mode

    - docker run -d -p 5000:5000 babanila/python-docker-sample

## URL to visit

1. <http://127.0.0.1:5000/>

2. <http://127.0.0.1:5000/2>

3. <http://127.0.0.1:5000/hello>
