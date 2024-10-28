# Los Cursos

- Learn FastApi.com
- Learn YFinance
- 8 things you should know in python
- gRPC in python

---

```python
#!/usr/bin/env python3

from subprocess import run
from sys import executable


def call(cmd):
    print(' '.join(cmd))
    run(cmd, check=True)


venv = '.venv'
call([executable, '-m', 'venv', venv])
py = f'{venv}/bin/python'
call([py, '-m', 'pip', 'install', '--upgrade', 'pip'])
call([py, '-m', 'pip', 'install', '-r', 'requirements.txt'])

```
or

## virtual env
```
$ mkdir projectA
$ cd projectA
$ python3 -m venv env
$ . env/Scripts/activate

$ pip list
Package Version
------- -------
pip     24.3.1
(env)

pip install pytest
pip install ipykernel

or 

pip freeze > requirements.txt 
pip install -r requirements.txt

python.exe -m pip install --upgrade pip
...

```

## VSCode
Python: Select Interpretor

#%%

