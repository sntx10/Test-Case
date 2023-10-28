from pymongo import MongoClient


def aggregate_salaries(dt_from, dt_upto, group_type):
    client = MongoClient("localhost", 27017)
    db = client["mydatabase"]
    collection = db["salaries"]

    group_fields = {
        "hour": {"format": "%Y-%m-%dT%H:00:00", "id": {"year": {"$year": "$date"}, "month": {"$month": "date"}, "day": {"dayOfMonth": "$date"}, "hour": {"$hour": "$date"}}},
        "day": {"format": "%Y-%m-%dT00:00:00", "id": {"year": {"$year": "$date"}, "month": {"$month": "$date"}, "day": {"$dayOfMonth": "$date"}}},
        "month": {"format": "%Y-%m-01T00:00:00", "id": {"year": {"$year": "$date"}, "month": {"$month": "$date"}}}
    }

    pipeline = [
        {
            "$match": {
                "date": {
                    "$gte": dt_from,
                    "$lte": dt_upto
                }
            }
        },
        {
            "$group": {
                "_id": group_fields[group_type]["id"],
                "sum": {"$sum": "$amount"}
            }
        },
        {
            "$project": {
                "formatted_date": {"$dateToString": {"format": group_fields[group_type]["format"], "date": "$_id"}},
                "sum": 1
            }
        },
        {
            "$sort": {"formatted_date": 1}
        }
    ]

    result = list(collection.aggregate(pipeline))
    dataset = [item["sum"] for item in result]
    labels = [item["formatted_date"] for item in result]

    return {"dataset": dataset, "labels": labels}