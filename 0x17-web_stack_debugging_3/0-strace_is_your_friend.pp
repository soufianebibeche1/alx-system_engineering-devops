# Puppet manifest to fix Apache 500 error
# the issue,fix it and then automate it using Puppet

exec { 'internal-server':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/usr/bin/:/bin/'
}
