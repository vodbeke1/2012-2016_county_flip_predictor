import redis
import pandas as pd
import json
import numbers

from config import Development as status

redis_host = status.REDIS_HOST
redis_port = status.REDIS_PORT
redis_password = status.REDIS_PASSWORD

def initialize_redis():

    """Example Hello Redis Program"""

    data = pd.read_csv("modelling/total_data.csv")

    for i in data.index:
        r = redis.StrictRedis(host=redis_host, port=redis_port)

        json_val = data.iloc[i].to_dict()
        for k in json_val.keys():
            if isinstance(json_val[k], numbers.Number):
                json_val[k] = json_val[k].item()
    
        json_val = json.dumps(json_val)
        r.set(str(i), json_val)

        if i % 100 == 0:
            new_json = r.get(i)
            print(type(new_json.decode("utf-8")))

    #try:
#
    #    # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
    #    # using the default encoding utf-8.  This is client specific.
#
    #    r = redis.StrictRedis(host=redis_host, port=redis_port)
#
#
#
    #    r.set("msg:hello", "Hello Redis!!!")
#
    #    msg = r.get("msg:hello")
#
    #    print(msg)
#
    #except Exception as e:
        

if __name__ == '__main__':
    initialize_redis()






    


