# File: 2-execute_a_command.pp
# Execute a command to kill the process named killmenow

exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
