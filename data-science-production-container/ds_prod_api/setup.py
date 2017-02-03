from setuptools import setup

setup(name='ds_prod_api',

    packages=['ds_prod_api'],
      version='0.1',

    entry_points={
        'console_scripts': [
        'ds_prod_api = ds_prod_api.command_line:main']
    })