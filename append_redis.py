# Filename: append_redis.py
import redis
pool = redis.ConnectionPool(host = '127.0.0.1', port = 6380)
r = redis.Redis(connection_pool = pool)
print r.append('append_key','append_OK')
