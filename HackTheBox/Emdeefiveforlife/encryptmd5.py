# Import des modules nécessaires
from selenium import webdriver
from selenium.webdriver.common.by import By
import hashlib
import time

# Initialisation du pilote Selenium pour le navigateur Chrome
driver = webdriver.Chrome()

# Accéder à l'URL où se trouve le chiffrement à effectuer
driver.get("http://94.237.57.59:31843/")

# Récupération du texte à chiffrer qui se trouve dans la balise h3
tocypher = driver.find_element(By.XPATH, "/html/body/h3").text
print("On récupère : " + tocypher)

# Chiffrement du texte récupéré en utilisant l'algorithme MD5
md5 = hashlib.md5(tocypher.encode('utf-8')).hexdigest()
print("Cela donne en md5 : " + md5)

# Recherche de l'élément HTML de type 'input' avec le nom 'hash' pour y saisir le résultat du chiffrement
clickable = driver.find_element(By.NAME, "hash")
clickable.send_keys(md5)

# Recherche du bouton de soumission du formulaire et clic dessus
clickable = driver.find_element(By.XPATH, "/html/body/center/form/input[2]")
clickable.click()

# Attente d'une seconde pour que la page se charge
time.sleep(1)

# Affichage du résultat (le flag) qui se trouve dans la balise p
print("Le flag est : " + driver.find_element(By.XPATH, "/html/body/p").text)

# Fermeture du navigateur
driver.quit()
