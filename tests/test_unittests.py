import os
import pytest

from pre_commit_hook.unittests import main


def test_run_cmd():
    assert main(['something', '--run-cmd', 'ls']) == 0
