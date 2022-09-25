from setuptools import setup

setup(
    name='bevan-transfer',
    version='0.2',
    py_modules=['bevantransfer'],
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'bevan-transfer = bevantransfer:cli',
        ]
    }
)