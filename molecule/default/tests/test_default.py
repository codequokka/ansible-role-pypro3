import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_python_interpreter_exists(host):
    f = host.file('/usr/bin/python')

    assert f.linked_to == '/usr/bin/python3.5'


def test_apt_packages_are_installed(host):
    p = host.package('language-pack-ja')

    assert p.is_installed is True


def test_system_default_locale_is_ja(host):
    f = host.file('/etc/default/locale')

    assert f.contains('LANG=ja_JP.UTF-8') is True


def test_user_locale_is_ja(host):
    f = host.file('/home/vagrant/.bashrc')

    assert f.contains('LANGUAGE=ja_JP:ja') is True
