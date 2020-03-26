# Client config file
file_line { 
 'turn off password auth':
 ensure => 'present',
 path   => '/etc/ssh/ssh_config',
 line   => 'PasswordAuthentication no'
 ;
 'declare identity file':
 ensure => 'present',
 path   => '/etc/ssh/ssh_config'
 line   => 'IdentityFile ~/.ssh/holberton'
}
