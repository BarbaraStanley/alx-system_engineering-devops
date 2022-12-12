# A module to set up your client SSH configuration file so that you can connect to a server without typing a password

exec{ 'edit ssh config':
  command  => "echo 'PasswordAuthentication no' >> /etc/ssh/ssh_config",
  provider => shell,
}
exec{ 'edit config ssh':
  command  => "echo 'IdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
  provider => shell,
}
