
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

    - docker run -p 5000:5000 babanila/python-docker-sample

## Build and run docker image with specific version

    - docker build -t babanila/python-docker-sample:v1.0.0 .

    - docker run -p 5000:5000 babanila/python-docker-sample:v1.0.0

## Run container in detached mode

    - docker run -d -p 5000:5000 babanila/python-docker-sample

## URL to visit

1. <http://127.0.0.1:5000/>

2. <http://127.0.0.1:5000/2>

3. <http://127.0.0.1:5000/hello>

4. <http://127.0.0.1:5000/app>

# Running with Redis implemenation

## Linking Two Containers (our App and Redis Storage)

1. Create and run redis container
   - docker run -d --name redis redis:7.0.7-alpine

2. Run app container and link redis container
   - docker run -d -p 5000:5000 --link redis babanila/python-docker-sample:v3.0.0

3. Check the IP on app container
   - docker exec -it 8a9726448161 bash
   - more /etc/hosts
