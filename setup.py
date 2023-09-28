from setuptools import setup

setup(
    name='venv_manager',
    version='0.1',
    description='A Python script to automate the creation and management of Python virtual environments.',
    license='MIT',
    author='Ahmed Cemil Bilgin',
    author_email='ahmed.c.bilgin@gmail.com',
    url='https://github.com/AhmedCemil/venv_manager',
    packages=['venv_manager'],
    entry_points={
        'console_scripts': [
            'venv_manager = venv_manager.venv_manager:__main__',
        ],
    },
)
