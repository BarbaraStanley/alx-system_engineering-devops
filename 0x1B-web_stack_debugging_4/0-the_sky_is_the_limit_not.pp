#aesthetics comment
file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"'
}
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
