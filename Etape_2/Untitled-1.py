import pymysql

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="École"
    )

def fetch_data(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM etudiants;")
        étudiants = cursor.fetchall()
        cursor.execute("SELECT * FROM enseignants;")
        enseignants = cursor.fetchall()
        return étudiants, enseignants

connection = connect_db()
étudiants, enseignants = fetch_data(connection)

print("Étudiants:")
for étudiant in étudiants:
    print(étudiant)

print("\nEnseignants:")
for enseignant in enseignants:
    print(enseignant)

connection.close()