import pymysql

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="École",
        cursorclass=pymysql.cursors.DictCursor 
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

associations = [(étudiant, enseignant) 
                for étudiant in étudiants 
                for enseignant in enseignants 
                if étudiant['numero_classe'] == enseignant['numero_classe']]

print("\nAssociations élèves - enseignants :")
for étudiant, enseignant in associations:
    print(f"Élève: {étudiant['prenom']} {étudiant['nom']} - Enseignant: {enseignant['prenom']} {enseignant['nom']}")

connection.close()