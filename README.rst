Archived
========

Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-tg-gui-pyportal/badge/?version=latest
    :target: https://circuitpython-tg-gui-pyportal.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/TG-Techie/CircuitPython_TG-Gui-PyPortal/workflows/Build%20CI/badge.svg
    :target: https://github.com/TG-Techie/CircuitPython_TG-Gui-PyPortal/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A driver to make using the TG-Gui on adafruit's PyPortal easier.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `TG-Gui-Std-CircuitPython <https://github.com/TG-Techie/TG-Gui-Std-CircuitPython>`_


Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.
   If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-tg-gui-pyportal/>`_. To install for current user:

.. code-block:: shell

    pip3 install tg-gui-pyportal

To install system-wide (this may be required in some embedded cases):

.. code-block:: shell

    sudo pip3 install tg-gui-pyportal

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install tg-gui-pyportal

Usage Example
=============

.. code-block:: python

    from tg_gui_std import *
    import tg_gui_pyportal as pyportal

    @pyportal.appwrapper
    class MyApp(Layout):

        greeter = Button(text="Hi!", self.on_press)

        def _any_(self):
            self.greeter(center, (self.width//2, self.height//2))

        def on_press(self):
            print("Hello!!")

        # temporary method
        def _loop_(self):
            pass

    pyportal.run_event_loop()

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/TG-Techie/CircuitPython_TG-Gui-PyPortal/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
