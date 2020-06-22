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
                print(tag, tags[tag])



    @staticmethod
    def _get_tags(tx, word):
        tags = []
        area = []
        ind = []
        result = tx.run(
            "MATCH (a:KeyWord {title:$word})-[:MATCHES]->(tags),"
            "(tags)-[:SPECIFIES]->(areas:ExpertiseAreas), "
            "(tags)-[:SPECIFIES]->(solutions:IndustrySolutions) "
            "RETURN tags.title as tags, areas.title as area, solutions.title as ind",
            word=word)

        for record in result:
            if record["tags"] not in tags:
                tags.append(record["tags"])
            if (record["area"]) not in area:
                area.append(record["area"])
            if (record["ind"]) not in ind:
                ind.append(record["ind"])
        data = {'Теги:': tags, 'Области экспертизы:': area, 'Отраслевые решения:': ind}
        # return tags, area, ind
        return data
