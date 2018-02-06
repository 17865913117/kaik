import sys
import redis

r = redis.Redis(host='10.0.102.205')

if __name__ == '__main__':
    channel = sys.argv[1]
    name = sys.argv[2]
    while True:
        message = input('Enter a message:')
        if message.lower() == 'exit':
            break
        message = '{name}:{message}'.format(**locals())
        r.publish(channel, message)
