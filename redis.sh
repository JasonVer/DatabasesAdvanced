sudo apt update
sudo apt install redis-server
sudo systemctl status redis
redis-cli
ping
set test "It's working!"
get test
exit
sudo systemctl restart redis
redis-cli
get test
exit