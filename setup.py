from setuptools import setup

setup(
    name='acb_venv_manager',
    version='0.1.0',
    description='A Python script to automate the creation and management of Python virtual environments.',
    license='MIT',
    author='Ahmed Cemil',
    author_email='ahmedcemil@example.com',
    url='https://github.com/AhmedCemil/venv_manager',
    packages=['acb_venv_manager'],
    entry_points={
        'console_scripts': [
            'acb_venv_manager = acb_venv_manager.venv_manager:__main__',
        ],
    },
)
