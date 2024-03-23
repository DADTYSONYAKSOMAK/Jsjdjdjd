import os


class Tayson(object):
    TAYSON = os.environ.get("TAYSON", "")

    API_ID = int(os.environ.get("API_ID", 23464711))

    API_HASH = os.environ.get("API_HASH", "d18596102470dff56b5f6c0c9844519e")
    
    OWNER = int(os.environ.get("OWNER", 5847230349))
