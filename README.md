# Todo

## About

Serialize and deserialize nested compound expression strings such as (a = 1 or (b = 2 and c = 3)) into parsable expression graphs.

## Install

pre-requisites
- sudo apt-get install python3
- sudo apt-get install python3-pip
- sudo pip3 install virtualenv 

1. Clone repository and enter its directory
```
git clone {repo}
cd {repo-name}
```

2. Create and activate environment
```
virtualenv -p python3 env
. env/bin/activate
```

3. Install requirements
```
pip3 install -r requirements.txt
```

## Configure

## Use
- [ ] todo

## Contribute

### Running tests
```
coverage run -m unittest2 discover -p="*Test.py"
coverage html
```

or use

```
bash bin/run-tests
```

```
bash bin/run-tests *Test.py
```