from setuptools import setup

setup(
    name="pre_commit_dummy_package",
    version="0.1",
    install_requires = [
        'autoflake',
        'seed-isort-config',
        'isort',
        'black',
    ]
)
