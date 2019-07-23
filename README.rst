py-commit-hooks
---------------

This is a collection of pre-commit hooks used in my projects.

Usage
=====

Add ``.pre-commit-config.yaml`` and point it to this repository, listing
the hooks you want to use. It should look like this:

.. code:: YAML

  repos:
  - repo: https://github.com/Landmaj/py-commit-hooks.git
    rev: v1.3.2
    hooks:
    - id: autoflake
    - id: isort
    - id: black
    - id: flake8

You should also copy ``pyproject.toml`` to your repository.


Running the hooks
+++++++++++++++++

After adding the hooks, install pre-commit either globally or in the
virtual environment - it does not matter, as it will create it's own
virtual environment to run hooks in anyway. I recommend using pipx_.
Run ``pre-commit install`` in the same directory where ``.pre-commit-config.yaml``
is and wait a few second/minutes for the initial setup.

After that, the hooks will run automatically during each commit on all
staged files. You can force execution on all files using
``pre-commit run --all-files``. Each hook can also be used separately:
``pre-commit run black`` or ``pre-commit run black --all-files``. Refer
to pre-commit_ documentation for more information.

If you have global hooks, pre-commit will complain and will not run.
To fix this, you have to remove them:
``git config --global --unset-all core.hooksPath``

.. _pipx: https://github.com/pipxproject/pipx
.. _pre-commit: https://pre-commit.com/

