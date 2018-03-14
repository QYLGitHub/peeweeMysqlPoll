from setuptools import setup, find_packages
setup(
    name='peewee_mysqlpool',
    version='0.1',
    author='perror',
    packages=find_packages(),
    publish=[
        'sudo python3 setup.py bdist_egg',
        'sudo python3 setup.py sdist',
        'sudo python3 setup.py bdist_egg upload'
        'sudo python3 setup.py sdist upload'
    ]
)