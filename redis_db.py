import redis

from config import Development as status

redis_host = status.REDIS_HOST
redis_port = status.REDIS_PORT
redis_password = status.REDIS_PASSWORD

def hello_redis():

    """Example Hello Redis Program"""

    try:

        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.

        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)


        r.set("msg:hello", "Hello Redis!!!")

        msg = r.get("msg:hello")

        print(msg)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    hello_redis()



    


