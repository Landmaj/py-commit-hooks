from setuptools import setup

setup(
    name="pre_commit_dummy_package",
    version="0.1",
    install_requires = [
        'autoflake==1.2',
        'seed-isort-config==1.2',
        'isort==4.3.3',
    ]
)
