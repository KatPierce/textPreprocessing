from neo4j import GraphDatabase


class GBDConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_tags(self, word):
        with self.driver.session() as session:
            tags = session.read_transaction(self._get_tags, word)
            for tag in tags:
                print(tag)

    @staticmethod
    def _get_tags(tx, word):
        people = []
        result = tx.run(
            "MATCH (a:Person {surname:$word})-[:WRITES]->(m)<-[:WRITES]-(cowriters) RETURN cowriters.surname AS name",
            word=word)
        for record in result:
            people.append(record["name"])
        return people
