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

## upgrade
```
$ python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in d:\work\python\ds\loscursos\grpc-in-python\env\lib\site-packages (24.2)
Collecting pip
  Using cached pip-24.3.1-py3-none-any.whl.metadata (3.7 kB)
Using cached pip-24.3.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.2
    Uninstalling pip-24.2:
      Successfully uninstalled pip-24.2
Successfully installed pip-24.3.1
```

## Links
- https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/
