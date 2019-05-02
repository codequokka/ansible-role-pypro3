import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python_interpreter_exists(host):
    f = host.file('/usr/bin/python')

    assert f.linked_to == '/usr/bin/python3.5'
