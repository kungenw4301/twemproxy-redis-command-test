# Filename: bitop_redis.py
import redis
pool = redis.ConnectionPool(host = '127.0.0.1', port = 6384)
r = redis.Redis(connection_pool = pool)
print r.set('mykey','\xff\xf0\x00')
print r.bitpos('mykey', 0)

print r.set('mykey','\x00\xff\xf0')
print r.bitpos('mykey', 1, 0)
print r.bitpos('mykey',1,1)
print r.set('mykey', '\x00\x00\x00')
print r.bitpos('mykey', 1)
