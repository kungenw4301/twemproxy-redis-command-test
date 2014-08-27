import redis
import redis_reset

def flush_all():
    for port in [6380, 6381, 6382, 6383, 6384]:
        redis_reset.flush_each_instance(port)
    print;

proxy_pool = redis.ConnectionPool(host='localhost', port=6379)
redis_pool = redis.ConnectionPool(host='localhost', port=6384)

redis_client = redis.Redis(connection_pool = redis_pool)
proxy_client = redis.Redis(connection_pool = proxy_pool)

def expire_test(client):
    print 'command: expire';
    print 'set mykey hello:\n %s' % client.set('mykey','hello')
    print 'expire mykey 10:\n %s' % client.expire('mykey', 10)
    print 'TTL mykey:\n %s' % client.ttl('mykey') 


if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    expire_test(d[i])
	    print '\n'
	
    flush_all()

