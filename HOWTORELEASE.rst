Release Procedure
-----------------

We follow semantic versioning, e.g., v1.0.0. A major version causes incompatible API changes,
a minor version adds functionality, and a patch covers bug fixes.

#. Create a new branch ``release-vX.x.x`` with the version for the release.

 * Update ``CHANGELOG.rst``
 * Make sure all new changes, features are reflected in the documentation.

#. Open a new pull request for this branch targeting `master`

#. After all tests pass and the PR has been approved, merge the PR into ``master``

#. Tag a release and push to github::

    $ git tag -a v1.0.0 -m "Version 1.0.0"
    $ git push origin master --tags

#. Build and publish release on PyPI::

    $ git clean -xfd  # remove any files not checked into git
    $ python setup.py sdist bdist_wheel --universal  # build package
    $ twine upload dist/*  # register and push to pypi

#. Update the stable branch (used by ReadTheDocs)::

    $ git checkout stable
    $ git rebase master
    $ git push -f origin stable
    $ git checkout master

#. Update esmtools conda-forge feedstock

 * Fork `esmtools-feedstock repository <https://github.com/conda-forge/esmtools-feedstock>`_
 * Clone this fork and edit recipe::

        $ git clone git@github.com:username/esmtools-feedstock.git
        $ cd esmtools-feedstock
        $ cd recipe
        $ # edit meta.yaml

 - Update version
 - Get sha256 from pypi.org for `esmtools <https://pypi.org/project/esmtools/#files>`_
 - Fill in the rest of information as described `here <https://github.com/conda-forge/esmtools-feedstock#updating-esmtools-feedstock>`_

 * Commit and submit a PR
