A Simple Python Example of Using Pact Testing
=============================================

The project provides a simple example of Pact_ testing with Python from both a consumer and provider perspective using the python-pact_ package

Installation
------------

First ensure you are inside your virtual environment. Then install the dependencies with ``pip``:

.. code-block:: bash

    pip install -r requirements.txt


Running the Pact Tests
----------------------

The example uses pyinvoke_ as a task runner (the tasks themselves can be seen in ``tasks.py``). You will first need to run the consumer tests. These create the pact files we will later be verifying with pact_.

.. code-block:: bash

    invoke test_consumer

In addition to a bunch of temporary folders/files this will generate a pact ``JSON`` file called ``consumer-provider.json`` on successfully running the tests. This is the pact file we will be validating against a real instance of the service.

Once that is completed, we can validate the pact file with:

.. code-block:: bash

    invoke test_provider


To make things a little easy to run, the test_provider invoke task automatically starts an testing instance of the provider in a separate thread and closes it again after the validate has been completed. In a real world situation that would likely be handled by the CI server or at least another process.


.. _pact: https://docs.pact.io/
.. _python-pact: https://github.com/pact-foundation/pact-python
.. _pyinvoke: http://docs.pyinvoke.org/en/latest/
