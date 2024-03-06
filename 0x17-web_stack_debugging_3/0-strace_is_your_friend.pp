# 0-strace_is_your_friend.pp
exec { '500-error':
  command  => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
  path => '/usr/local/bin/:/bin/',
}