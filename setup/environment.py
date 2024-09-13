class Setup():
    def __init__(self):
        self.port=27017
        self.host="localhost"
        self.url=f"mongodb://{self.host}:{self.port}/"
        self.collection_name="project"
        self.db_name="admindb"