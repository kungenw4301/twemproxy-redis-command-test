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

def getrange_test(client):
    print 'command: getrange';
    print 'set mykey "this is a string":\n %s' % client.set('mykey', 'this is a string')
    print 'getrange mykey 0 3:\n %s' % client.getrange('mykey', 0, 3)
    print 'getrange mykey -3 -1:\n %s' % client.getrange('mykey', -3, -1)
    print 'getrange mykey 0 -1:\n %s' % client.getrange('mykey', 0, -1)
    print 'getrange mykey 10 100:\n %s' % client.getrange('mykey', 10, 100)


if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    getrange_test(d[i])
	    print '\n'
	
    flush_all()

