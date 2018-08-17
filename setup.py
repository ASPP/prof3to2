from setuptools import setup


setup(
    name='prof3to2',
    version='1.0.0',
    packages=['prof3to2'],
    entry_points={
        'console_scripts': [
            'prof3to2 = prof3to2.main:main'
        ]
    },
)
