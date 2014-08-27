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

def get_test(client):
    print 'command: get';
    print 'get nonexisting :\n %s' % client.get('nonexisting')
    print 'set mykey hello :\n %s' % client.set('mykey', 'hello')
    print 'get mykey:\n %s' % client.get('mykey')


if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    get_test(d[i])
	    print '\n'
	
    flush_all()

