import redis
r= redis.Redis(host='10.0.102.205')
channels = ['1708', '1709']

if __name__ == '__main__':
    pubsub = r.pubsub()
    map(pubsub.subscribe, channels)
    pubsub.subscribe('1708')
    while True:
        for item in pubsub.listen():
            message = item['data']
            if type(message) == bytes:
                message = message.decode('utf-8')
            print(message)