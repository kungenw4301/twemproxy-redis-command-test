# Filename: bitcount_redis.py
import redis
pool = redis.ConnectionPool(host = '127.0.0.1', port = 6379)
r = redis.Redis(connection_pool = pool)
print r.bitcount('bits')
print r.bitcount('append_key')
