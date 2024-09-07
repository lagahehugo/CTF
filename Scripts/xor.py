import argparse  # Importation du module argparse pour la gestion des arguments de la ligne de commande
import os  # Importation du module os pour les opérations sur le système de fichiers

def xor(pathfichierAvant, pathfichierApres, key):
    """
    Effectue une opération XOR sur le contenu binaire d'un fichier avec une clé donnée et 
    écrit le résultat dans un autre fichier.

    :param pathfichierAvant: Chemin du fichier source.
    :param pathfichierApres: Chemin du fichier destination.
    :param key: Clé utilisée pour l'opération XOR.
    """
    # Lecture du contenu binaire du fichier source
    with open(pathfichierAvant, 'rb') as fichier:
        donneeBin = fichier.read()

    # Encodage de la clé en bytes
    keyBytes = key.encode()
    keyLongueur = len(key)

    # Initialisation d'un tableau de bytes pour stocker le résultat
    result = bytearray()
    
    # Application de l'opération XOR entre chaque byte des données et la clé
    for i in range(len(donneeBin)):
        result.append(donneeBin[i] ^ keyBytes[i % keyLongueur])

    # Écriture du résultat dans le fichier destination
    with open(pathfichierApres, 'wb') as fichierApres:
        fichierApres.write(result)

def parse_arguments():
    """
    Analyse les arguments de la ligne de commande.

    :return: Les arguments analysés.
    """
    parser = argparse.ArgumentParser(description="Parser d'arguments")
    
    # Ajout de l'argument pour le premier fichier
    parser.add_argument(
        '-f1', '--file1',
        type=str,
        required=True,
        help="Le chemin du premier fichier en entrée."
    )
    
    # Ajout de l'argument pour le deuxième fichier
    parser.add_argument(
        '-f2', '--file2',
        type=str,
        required=True,
        help="Le chemin du deuxième fichier en entrée."
    )
    
    # Ajout de l'argument pour la clé
    parser.add_argument(
        '-k', '--key',
        type=str,
        required=True,
        help="La clé en entrée."
    )
    
    return parser.parse_args()

def main():
    """
    Fonction principale qui gère le flux de l'application.
    """
    # Analyse des arguments de la ligne de commande
    args = parse_arguments()
    
    # Vérification que le fichier source existe
    if not os.path.exists(args.file1):
        print(f"Erreur : le fichier {args.file1} n'existe pas.")
        return
    
    # Appel de la fonction XOR avec les arguments fournis
    xor(args.file1, args.file2, args.key)

# Point d'entrée du script
if __name__ == "__main__":
    main()
