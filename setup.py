from setuptools import setup

setup(
    name='pythonProject',
    version='0.0.1',
    packages=['app'],
    url='',
    license='Open',
    author='Soldafon',
    author_email='pashok2082.Ryuz@gmail.com',
    description='FirstAPI',
    install_requires=[
        'anyio==3.5.0',
        'asgiref==3.5.0',
        'click==8.0.3',
        'colorama==0.4.4',
        'fastapi==0.73.0',
        'h11==0.13.0',
        'idna==3.3',
        'pydantic==1.9.0',
        'sniffio==1.2.0',
        'starlette==0.17.1',
        'typing-extensions==4.0.1',
        'uvicorn==0.17.1'
    ],
    scripts=['app/main.py','scripts/create_db.py']
)
