from pie import *


@task
def setup():
    createVenvs()
    updatePackages()


@task
def createVenvs():
    venv(r'venvs\test').create()


@task
def updatePackages():
    with venv(r'venvs\test'):
        pip(r'install -U pip')
        pip(r'install -U -r requirements.test.txt')


@task
def test():
    with venv(r'venvs\test'):
        cmd(r'python -m pytest -s tests')


@task
def build():
    cmd(r'set HTTPS_PROXY=localhost:38080 && python setup.py clean --all bdist_wheel --universal upload')
