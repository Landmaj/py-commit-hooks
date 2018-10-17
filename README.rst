py-commit-hooks
---------------

This is a collection of pre-commit hooks used in my projects.
At the moment it is mostly focused on sorting Python imports.

Usage
=====

You can add pre-commit hooks included in this repository using two
methods.

1. Point pre-commit to this repository
    The easiest way is to add ``.pre-commit-config.yaml`` and point it
    to this repository, listing the hooks you want to use. It would
    look like this:

.. code:: YAML

  repos:
  - repo: https://github.com/Landmaj/py-commit-hooks.git
    rev: v1.1.0
    hooks:
    - id: black
    - id: autoflake
    - id: seed-isort-config
    - id: isort

2. Store the hooks locally
    If you do not want to link to this repository, you can copy the
    hooks and link to them locally. This is something I do at work.
    Copy ``.pre-commit-hooks.yaml`` from this repository to you
    project's main directory and add file called
    ``.pre-commit-config.yaml`` with the following content:

.. code:: YAML

  repos:
  - repo: local
    hooks:
    - id: black
    - id: autoflake
    - id: seed-isort-config
    - id: isort

Remove any hooks that you do not want (or comment them out) from
``.pre-commit-hooks.yaml``. Keep in mind that seed-isort-config and
isort should be kept together, otherwise isort will not distinguish
your modules and packages from third party libraries.

You should also copy ``.isort.cfg`` together with ``.pre-commit-hooks.py``.
The settings should not be modified (except for ``not_skip=__init__.py`` which can be safely removed) if you want to use Black.
Otherwise it may cause commits to fail all the time due to conflicts between Black and isort formatting.

Running the hooks
+++++++++++++++++

After adding the hooks, install pre-commit either globally or in the
virtual environment - it does not matter, as it will create it's own
virtual environment to run hooks in anyway. I recommend using pipsi_.

After that, the hooks will run automatically during each commit on all
staged files. You can force execution on all files using
``pre-commit run --all-files``. Each hooks can also be used separately:
``pre-commit run black`` or ``pre-commit run black --all-files``. Refer
to pre-commit_ documentation for more information.

If you have global hooks, pre-commit will complain and will not run.
To fix this, you have to remove them:
``git config --global --unset-all core.hooksPath``


.. _isort: https://isort.readthedocs.io/en/latest/
.. _pipsi: https://github.com/mitsuhiko/pipsi
.. _pre-commit: https://pre-commit.com/


