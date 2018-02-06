import random
import time
from datetime import datetime, timedelta
import redis
import faker

r = redis.Redis(password='000000')
faker = faker.Faker('zh_CN')
DEADLINE = datetime.now() + timedelta(hours=1)


def exam(course, studetns=50):
    print("%s exam start... %s students" % (course, studetns))
    for i in range(studetns):
        name = faker.name()
        tiem_remaining = (DEADLINE - datetime.now()).total_seconds()

        score = '%s.%s' % (random.randint(60, 100), str(tiem_remaining).replace('.', ''))

        r.zadd(course, name, score)
        print('%s: %s' % (name, score))
        time.sleep(0.2)
        print('%s exam end' % course)


def top(course, rank_range=10):
    stus = r.zrevrange(course, 0, rank_range, withscores=True)
    for i, (stu, score) in enumerate(stus):
        print(i + 1, stu.decode('utf-8'), score)


if __name__ == '__main__':
    courses = ['English', 'Math']
    for course in courses:
        exam(course)
        top(course)