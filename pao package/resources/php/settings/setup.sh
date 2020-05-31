# setup for Laravel with Pao==0b.2

echo '--- Pao ---'
echo "wait composer installation" 

php composer-setup.php --install-dir=bin --filename=composer 

echo "wait laravel installation" 

composer global require laravel/installer
echo Job 2 exited with status $?
