import dateutil.parser
from pymongo import MongoClient
from decouple import config

MONGO_USERNAME = config('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASSWORD = config('MONGO_INITDB_ROOT_PASSWORD')
MONGO_DATABASE = config('MONGO_INITDB_DATABASE')

MONGODB_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongodb:27017/{MONGO_DATABASE}"

client = MongoClient(MONGODB_URI)
db = client[MONGO_DATABASE]


def aggregate_salaries(dt_from, dt_upto, group_type):
    dt_from = dateutil.parser.parse(dt_from)
    dt_upto = dateutil.parser.parse(dt_upto)

    if group_type == "hour":
        group_format = "%Y-%m-%dT%H:00:00"
    elif group_type == "day":
        group_format = "%Y-%m-%dT00:00:00"
    elif group_type == "month":
        group_format = "%Y-%m-01T00:00:00"
    else:
        raise ValueError("Invalid group_type")

    pipeline = [
        {
            "$match": {
                "dt": {"$gte": dt_from, "$lte": dt_upto}
            }
        },
        {
            "$group": {
                "_id": {
                    "$dateToString": {"format": group_format, "date": "$dt"}
                },
                "total": {"$sum": "$value"}
            }
        },
        {"$sort": {"_id": 1}}
    ]

    results = db["sample_collection"].aggregate(pipeline)

    dataset = []
    labels = []
    for result in results:
        dataset.append(result["total"])
        labels.append(result["_id"])

    return {"dataset": dataset, "labels": labels}

