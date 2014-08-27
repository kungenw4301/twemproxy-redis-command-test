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

def getbit_test(client):
    print 'command: getbit';
    print 'setbit mykey 7 1:\n %s' % client.setbit('mykey', 7, 1)
    print 'getbit mykey 0:\n %s' % client.getbit('mykey', 0)
    print 'getbit mykey 7:\n %s' % client.getbit('mykey', 7)
    print 'getbit mykey 100:\n %s' % client.getbit('mykey', 100)


if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    getbit_test(d[i])
	    print '\n'
	
    flush_all()

