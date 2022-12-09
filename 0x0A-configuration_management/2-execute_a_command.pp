# a manifest that kills a process named killmenow

exec { 'kill process':
  command => 'usr/bin/bash/pkill -f killmenow'
}
