# Todo

## About

Serialize and deserialize nested compound expression strings such as (a = 1 or (b = 2 and c = 3)) into parsable expression trees such as [key:a operator:= value:1, conjunction:or, [key:b operator:= value:2, conjunction:and, key:c operator:= value:3]]..

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

Deserialize a string into a tree of conditions.

```python
expression = Expression('(a = 1 and b = 2)')
conditions = expression.to_conditions()

print(conditions.conditions[0].key))        # a
print(conditions.conditions[0].operator))   # =
print(conditions.conditions[0].value))      # 1

print(conditions.conditions[1].value))      # and

print(conditions.conditions[2].key)))       # b
print(conditions.conditions[2].operator))   # =
print(conditions.conditions[2].value))      # 2
```

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