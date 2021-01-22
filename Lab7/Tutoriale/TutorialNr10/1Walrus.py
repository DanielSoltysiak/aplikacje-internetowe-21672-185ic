from walrus import *
db = Database(host='localhost', port=6379, db=0)

db['test']=11

redis_list = db.List('test_list')

redis_list.append('22')
redis_list.extend([22,44])

redis_set = db.Set('test_set')

redis_set.add(22)
redis_set.remove(22)

redis_sorted_set = db.ZSet('test_sorted_set')
redis_sorted_set.add({'w': 11,"e": 33})