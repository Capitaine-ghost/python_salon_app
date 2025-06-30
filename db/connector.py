import MySQLdb

class DbConnection () : 
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.status=None

    def connect(self):
        try:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.database,
                charset='utf8'
            )
            self.status =200
            print("Connexion à la base de données réussie.")
        except MySQLdb.Error as e:
            print(f"Erreur lors de la connexion à MySQL : {e}")
            self.status =500
            self.connection = None
        finally : 
            return self.status
        
    def close(self):
        if self.connection:
            self.connection.close()
            print("Connexion à la base de données fermée.")

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            print("Aucune connexion active à la base de données.")
            return None

    def execute_query(self, query, params=None):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, params)
                self.connection.commit()
                print("Requête exécutée avec succès.")
                self.status=201             
            except MySQLdb.Error as e:
                print(f"Erreur lors de l'exécution de la requête : {e}")
                self.status=500
                self.connection.rollback()
            finally:
                cursor.close()
                return self.status
        else:
            print("Aucune connexion active pour exécuter la requête.")

    def fetch_all(self, query, params=None):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, params)
                results = cursor.fetchall()
                self.status=200
                print("Données récupérées avec succès.")
                return [results, self.status]
            except MySQLdb.Error as e:
                print(f"Erreur lors de la récupération des données : {e}")
                self.status=500
                return [None,self.status]
            finally:
                cursor.close()
        else:
            print("Aucune connexion active pour récupérer les données.")
            return [None, 500]
    def fetch_one(self, query, params=None):
        pass
