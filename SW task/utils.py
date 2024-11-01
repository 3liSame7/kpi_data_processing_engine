import json
import datetime

def construct_message(asset_id, attribute_id, value):
    response = {
        "asset_id": asset_id,
        "attribute_id": attribute_id,
        "timestamp": datetime.datetime.now().isoformat() + "Z",
        "value": value
    }
    return json.dumps(response)
