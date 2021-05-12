# redisEnum	

This simple script uses redis-cli to enumerate a directory for existing subdirectories.

Generally, I find this useful for enumerating user directories located in **/home** and web directories in folders like **/var/www/html**

Usage: 

```python3 redisEnum.py host_address parent_directory wordlist")```

Eg:

```python3 redisEnum.py 192.168.144.42 /home /usr/share/wordlists/common_names.txt")```
