# Create a command that kills a process
exec { 'kills process':
  command  =>  'pkill killmenow',
  path     =>  '/usr/bin',
  provider =>  'shell',
}
