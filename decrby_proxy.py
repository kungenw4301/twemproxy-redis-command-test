import redis
import redis_reset

for port in [6380, 6381, 6382, 6383]:
    redis_reset.flush_each_instance(port)

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool = pool)

print r.set('mykey','10')
print r.decr('mykey', amount=3)

print r.set('mykey', '234293482390480948029348230948')
#print r.decr('mykey', 3)

for port in [6380, 6381, 6382, 6383]:
    redis_reset.flush_each_instance(port)
