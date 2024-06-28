# This Puppet manifest kills a process named 'killmenow' using the pkill command.
exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  onlyif  => 'pgrep killmenow',
}
