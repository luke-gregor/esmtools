
esmtools: a toolbox for Earth system model analysis
===================================================

..
    Table version of badges inspired by pySTEPS.

.. list-table::
    :stub-columns: 1
    :widths: 10 90

    * - docs
      - |docs|
    * - tests
      - |requires| |codecov|
    * - package
      - |conda| |pypi|
    * - license
      - |license|
    * - community
      - |contributors| |downloads|
    * - tutorials
      - |gallery|

.. |docs| image:: https://img.shields.io/readthedocs/esmtools/stable.svg?style=flat
    :target: https://esmtools.readthedocs.io/en/stable/?badge=stable
    :alt: Documentation Status

.. |requires| image:: https://requires.io/github/bradyrx/esmtools/requirements.svg?branch=master
     :target: https://requires.io/github/bradyrx/esmtools/requirements/?branch=master
     :alt: Requirements Status

.. |codecov| image:: https://codecov.io/gh/bradyrx/esmtools/branch/master/graph/badge.svg
      :target: https://codecov.io/gh/bradyrx/esmtools

.. |conda| image:: https://img.shields.io/conda/vn/conda-forge/esmtools.svg
    :target: https://anaconda.org/conda-forge/esmtools
    :alt: Conda Version

.. |pypi| image:: https://img.shields.io/pypi/v/esmtools.svg
   :target: https://pypi.python.org/pypi/esmtools/

.. |license| image:: https://img.shields.io/github/license/bradyrx/esmtools.svg
    :alt: license
    :target: ../../LICENSE.txt

.. |contributors| image:: https://img.shields.io/github/contributors/bradyrx/esmtools
    :alt: GitHub contributors
    :target: https://github.com/bradyrx/esmtools/graphs/contributors

.. |downloads| image:: https://img.shields.io/conda/dn/conda-forge/esmtools
    :alt: Conda downloads
    :target: https://anaconda.org/conda-forge/esmtools

.. |gallery| image:: https://img.shields.io/badge/esmtools-example_gallery-ed7b0e.svg
    :alt: climpred gallery
    :target: https://esmtools.readthedocs.io/en/stable/examples.html

Most Recent Release
===================

v1.1.1 of ``esmtools`` mainly introduces dask-friendly, vectorized, lightweight
functions for standard statistical functions. They also intelligently handle
datetimes on the independent (x) axis:

* :py:func:`~esmtools.stats.linear_slope`
* :py:func:`~esmtools.stats.linregress`
* :py:func:`~esmtools.stats.polyfit`
* :py:func:`~esmtools.stats.rm_poly`
* :py:func:`~esmtools.stats.rm_trend`


Installation
============

You can install the latest release of ``esmtools`` using ``pip`` or ``conda``:

.. code-block:: bash

    pip install esmtools

.. code-block:: bash

    conda install -c conda-forge esmtools

You can also install the bleeding edge (pre-release versions) by running

.. code-block:: bash

    pip install git+https://github.com/bradyrx/esmtools@master --upgrade

**Getting Started**

* :doc:`examples`
* :doc:`accessors`

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Getting Started

    examples
    accessors

**Help & Reference**

* :doc:`api`
* :doc:`contributing`
* :doc:`changelog`
* :doc:`release_procedure`
* :doc:`contributors`
* :doc:`additional_packages`

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Help & Reference

    api
    contributing
    changelog
    release_procedure
    contributors
    additional_packages.ipynb
