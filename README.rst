developer-tools
===========

Useful tools for Python developers.

This is mostly an example to show how `autopip <https://pypi.org/project/autopip/>`_ can be used to install a group of
apps with various version specifications, but the author does install it as it conveniently provides all the tools
useful for doing Python software development.

To install::

    autopip install developer-tools

How does it work? You can tell `autopip` to install other apps by setting an `autopip` entry point group in
``setup.py`` with the list of apps and versions. Versions can be pinned to major or a specific version, or use `latest`
to install the latest version. Take a look at the `autopip` entry point group in
`developer-tools' setup.py <https://github.com/maxzheng/developer-tools/blob/master/setup.py>`_

For security and user experience, it is recommended to pin to a specific version -- at least minor -- for apps that you
don't own. For apps that you own where you have good versioning in the app, then `latest` works better.
