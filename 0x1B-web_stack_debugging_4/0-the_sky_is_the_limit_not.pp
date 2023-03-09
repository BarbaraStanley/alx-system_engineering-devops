package { 'nginx': ensure => installed }
file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
service { 'nginx': ensure => running, enable => true, require => File['/etc/default/nginx'] }i
