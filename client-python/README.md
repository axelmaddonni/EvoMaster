# EvoMaster Client for Python

Environment:
```
pyenv virtualenv venv-evomaster
pyenv activate venv-evomaster
pip install -r requirements-dev.txt
```

Running the instrumented version of EvoMaster Proxy controller:

```python
python -m evomaster_client.cli run -p 'evomaster_client.controller' -m 'evomaster_client.controller.em_app'
```

Running tests:

```python
pytest [-s] tests
```