# File: 0-strace_is_your_friend.pp
exec { 'fix-apache-500-error':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php', 
  path        => '/usr/local/bin/:/bin/' 
  refreshonly => true,
}
