[![Build Status](https://travis-ci.org/Dinoshauer/pre-commit-unittests.svg)](https://travis-ci.org/Dinoshauer/pre-commit-unittests)
[![Coverage Status](https://coveralls.io/repos/Dinoshauer/pre-commit-unittests/badge.png)](https://coveralls.io/r/Dinoshauer/pre-commit-unittests)

Pre-commit unittest runner
==========================

This [pre-commit](https://github.com/pre-commit) hook that will run a command
for you (ideally, unittests).

* [pre-commit](https://github.com/pre-commit)
* [fabric](http://www.fabfile.org)


Add this to your ``.pre-commit-config.yaml`` file

    - repo: git://github.com/Dinoshauer/pre-commit-unittests
      sha: HEAD
      hooks:
      - id: unittest-runner
        args: ['--run-cmd "nosetests tests/"']

Args:

The exact provided string will be run with fabric's ``local``


Development: ``pip install -r requirements-dev.txt``

Testing: ``py.test --cov pre_commit_hook tests/``
