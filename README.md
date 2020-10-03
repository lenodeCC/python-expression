# Todo

## About

Serialize and deserialize nested compound expression strings such as `(a = 1 or (b = 2 and c = 3))` into parsable expression trees such as `[key:a operator:= value:1, conjunction:or, [key:b operator:= value:2, conjunction:and, key:c operator:= value:3]]`.

You may want to provide an easy to configure filter on an endpoint such as `GET /services?filter=(price lt 200 and duration is 2hrs)`

You may want to build an ORM filter.

These sets of classes make few assumptions as to how conditions will be evaluated. It lets the author decide.

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

Evaluate an expression as a boolean.

```python

class DummyDateBetweenHandler():

    def __init__(self, data):
        self._data = data

    def handle(self, condition):

        key = self._data.get(condition.key)
        values = condition.value.split(',')

        if condition.operator == 'date_between':
            date1 = datetime.strptime(values[0], '%Y-%M-%d')
            date2 = datetime.strptime(values[1], '%Y-%M-%d')

            if date1 <= key <= date2:
                return True

        return False

evaluate = Evaluate(DummyDateBetweenHandler({
    "date": datetime.strptime("2020-09-27", '%Y-%M-%d')
}))

result = evaluate.from_expression('date date_between 2020-09-26,2020-09-28')
self.assertTrue(result)

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