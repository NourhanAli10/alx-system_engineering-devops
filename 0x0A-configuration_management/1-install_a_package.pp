# 1-install_a_package.pp

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

exec { 'Refresh the shell':
  command     => 'exec $SHELL',
  path        => ['/bin', '/usr/bin', '/usr/local/bin'],
  refreshonly => true,
}
