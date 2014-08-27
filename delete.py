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

def delete_test(client):
    print 'command: del';
    print client.set('key1','hello')
    print client.set('key2','world')

    print client.delete('key1', 'key2', 'key3')

if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    delete_test(d[i])
	    print '\n'
	
    flush_all()

