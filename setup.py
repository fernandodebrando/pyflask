from setuptools import setup

setup(
    name='pyflask',
    packages=['pyflask'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy'
    ],
)