import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package', [
      'build-essential',
      'python3-dev',
      'libsqlite3-dev',
      'libreadline6-dev',
      'libgdbm-dev',
      'zlib1g-dev',
      'libbz2-dev',
      'sqlite3',
      'tk-dev',
      'zip',
      'libssl-dev',
])
def test_apt_packages_are_installed(host, package):
    p = host.package(package)

    assert p.is_installed is True


def test_python3_is_installed(host):
    c = host.run('/opt/python3.6.4/bin/python3.6 -V')

    assert c.stdout == 'Python 3.6.4\n'


@pytest.mark.parametrize('src, dest', [
    ('/opt/python3.6.4/bin/python3.6', '/usr/local/bin/python3.6'),
    ('/opt/python3.6.4/bin/pip3.6', '/usr/local/bin/pip'),
])
def test_python_links_exists(host, src, dest):
    f = host.file(dest)

    assert f.linked_to == src
