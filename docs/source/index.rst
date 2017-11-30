========
NOTICE!!
========

**tl;dr:** This project was renamed to `Stapled`, which can be found `here`_.

As of now this project has been renamed to ``Stapled`` because there are
various other projects with the name ``ocspd`` which is confusing. Plus we want
to implement functional tests in the near future, which are probably going to
be based on a package also called ``ocsdp``. This project will be kept here
until June 30th 2018, in case you have this repo set as a dependency of some
project.

From now on you will get a warning when you install the package, that tells you
to use `Stapled` instead. From the 1st of January 2018 you will get an error
instead. From June 30th 2018 onward the installation will stop working entirely.

You can find `Stapled` `here`_.

.. _here: https://github.com/greenhost/stapled

============
Introduction
============

Why do I need ``ocspd``?
========================

``ocspd`` is meant to be a helper daemon for HAProxy which doesn't do OCSP stapling out of the box. However HAProxy *can* serve staple files if they are place in the certificate directory, which is what we use to our benefit.

.. toctree::
    :caption: Table of Contents
    :maxdepth: 3

    using
    modules
    core
    scheduling
    errorhandling


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

