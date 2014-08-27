import redis
import redis_reset

redis_reset.flush_each_instance(6384)

pool = redis.ConnectionPool(host='localhost', port=6384)
r = redis.Redis(connection_pool = pool)

print r.set('mykey','10')
print r.decr('mykey', amount=3)

print r.set('mykey', '234293482390480948029348230948')
#print r.decr('mykey', 3)


redis_reset.flush_each_instance(6384)
