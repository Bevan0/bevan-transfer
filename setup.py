from setuptools import setup

setup(
    name='bevan-transfer',
    version='0.1',
    py_modules=['bevantransfer'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'bevan-transfer = bevantransfer:main',
        ]
    }
)