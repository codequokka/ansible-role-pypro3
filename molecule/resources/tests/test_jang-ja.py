import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package', [
      'language-pack-ja',
])
def test_apt_packages_are_installed(host, package):
    p = host.package(package)

    assert p.is_installed is True


def test_system_default_locale_is_ja(host):
    f = host.file('/etc/default/locale')

    assert f.contains('LANG=ja_JP.UTF-8') is True


def test_user_locale_is_ja(host):
    f = host.file('/home/vagrant/.bashrc')

    assert f.contains('LANGUAGE=ja_JP:ja') is True
