
import redis
import json

r = redis.Redis(host='redis', port=6379, db=0)
r.set('test_key', 'test_value')
print('Stored value:', r.get('test_key').decode('utf-8'))
r.delete('test_key')

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

r.set('test_json', json.dumps(data))
print('Stored value:', json.loads(r.get('test_json').decode('utf-8')))


print('toto')