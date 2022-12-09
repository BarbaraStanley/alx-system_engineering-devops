# a manifest that creates a file 'school' in /tmp with 0744 permission and contains 'I love Puppet'

file{ 'school' :
  ensure  => present,
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
