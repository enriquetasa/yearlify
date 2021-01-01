#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = 'yearlify',
    version = '0.1',
    packages = find_packages(),
    scripts = [
        'manage.py'
        ],
    author='Enrique Tasa Sanchis',
    author_email='tasa@enriquetasa.com',
    install_requires=[
        'asgiref==3.3.1',
        'cffi==1.14.4',
        'cryptography==3.3.1',
        'Django==3.1.4',
        'django-appconf==1.0.4',
        'django-crispy-forms==1.10.0',
        'django-cryptography==1.0',
        'pycparser==2.20',
        'pytz==2020.5',
        'six==1.15.0',
        'sqlparse==0.4.1',
        ],
    )
