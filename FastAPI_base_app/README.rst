==========================
Home work 2
==========================

Business scenarios:
-------------------------------------------------------------------------------
- Register user
- Unregister user

Tests
-------------------------------------------------------------------------------
Tests are located in :code:`app/tests`. There are 2 types of tests: unit tests and integration tests.

To run tests run following command in root folder in your shell (Unix): :code:`./run_tests.sh`

==========================
FastAPI base project
==========================

Poetry initial setup
-------------------------------------------------------------------------------
- Configure Poetry **(should be done once globally)**:

.. code::

    poetry config virtualenvs.in-project false
    poetry config virtualenvs.path <conda-install-path>/envs

Packages installation
-------------------------------------------------------------------------------
- Create and activate *conda* virtual environment for development:

.. code::

    conda create -n BaseApp python=3.10
    conda activate BaseApp

- Install dependencies with Poetry:

.. code::

    poetry install
