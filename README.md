
<a name="readme-top"></a>

<p  align="center"><img width="600px" src="https://github.com/BinaryBeast007/browser-password-decryptor/blob/main/assets/BrowserPasswordDecryptor.gif"></p>


<h2 align="center">Browser Password Decryptor</h2>
<p align="center">
    Extract and decrypt saved passwords from popular web browsers
    <br />
    <strong>Explore the docs »</strong>
    <br />
    <a href="https://github.com/BinaryBeast007/browser-password-decryptor/issues">Report Bug</a>
    ·
    <a href="https://github.com/BinaryBeast007/browser-password-decryptor/issues">Request Feature</a></p>

<!-- TABLE OF CONTENTS -->
<details open>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#executable">Executable</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Browser Password Decryptor is designed to extract and decrypt saved passwords from popular web browsers and send them as an email attachment. It provides a convenient way to retrieve passwords saved in browsers like Chrome, Brave, Edge, Firefox and Opera, and securely send them to a designated email address. Please note that this tool should only be used for educational and ethical purposes, and any unauthorized use may violate privacy laws and regulations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Getting started with [Python](https://www.python.org/about/gettingstarted/)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Dependencies

Before running Browser Password Decryptor, make sure you have Python 3.x installed on your system. Additionally, you need to install the required Python modules listed in the `requirements.txt` file. You can install them using the following command:

```bash
pip install -r requirements.txt
```

or

```bash
pip install pycryptodomex pywin32
```

If you prefer to install the modules manually, here's the list of required Python modules:
```bash
pycryptodomex 
pywin32 
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

- Clone the repo
   ```bash
   git clone https://github.com/BinaryBeast007/browser-password-decryptor
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Usage

To use Browser Password Decryptor, you will need to set up a Mailtrap account with temporary mail. Follow the steps below to configure Browser Password Decryptor with your Mailtrap credentials:

1.  **Create a Mailtrap Account**
    
    -   Go to [https://mailtrap.io/](https://mailtrap.io/) and sign up for an account with temporary mail.
2.  **Access SMTP Settings**
    
    -   After signing in, navigate to "Email Testing" and select "Inboxes" from the dropdown menu.
3.  **Obtain Mailtrap Credentials**
    
    -   In the Inboxes page, select "SMTP Settings" for the desired inbox.
    -   Locate the "Show Credentials" button and click on it. This will reveal the SMTP username and password specific to your Mailtrap inbox.
4.  **Configure `main.py`**
    
    -   Navigate to the `src` folder
    -   Inside the `main` method, look for the lines where `EMAIL` and `PASSWORD` are defined.
    -   Copy the previously obtained Mailtrap SMTP username and password.
    -   Replace `EMAIL` with the Mailtrap SMTP username and `PASSWORD` with the Mailtrap SMTP password.
    
5.  **Save and Run**
    
    -   Save your changes to the Python script after configuring the email credentials.
    -   Now, Browser Password Decryptor is set up to send email notifications using the provided Mailtrap account.

To use Browser Password Decryptor, simply run the script:

```bash
python src/main.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

-   **Password extraction from various web browsers:** The script supports extracting passwords from browsers such as Chrome, Brave, Edge, Firefox, and Opera.
-   **Password decryption:** The extracted password data is decrypted using AES encryption, allowing you to view the actual passwords associated with the accounts.
-   **Email notification:** The decrypted passwords are sent as an attachment in an email to a specified recipient address, providing a way to securely access the extracted information.
- **Cleanup:** Deletes the csv file and cache folder

### Supported Browser [Windows]

| Browser         | Password  |
|:----------------|:---------:|
| Google Chrome   |     ✅    |
| Brave           |     ✅    |
| Microsoft Edge  |     ✅    |
| Firefox         |     ✅    |
| Opera           |     ✅    |


## Executable

You can convert this Python script into a standalone executable (`.exe`) file using tools like `pyinstaller` or `cx_Freeze`. This allows you to run the script on systems without needing a Python interpreter.

### Using PyInstaller

1.  Install `pyinstaller` using `pip` if you haven't already: 
	```bash
	pip install pyinstaller
	```
2. Navigate to the  `src`  folder
	```bash
		cd src
	```
3. Create the executable:
	```bash
	pyinstaller --onefile main.py
	```
4. The executable will be created in the `dist` directory within your script's directory.

### Using cx_Freeze

1.  Install `cx_Freeze` using `pip` if you haven't already:
	```bash
	pip install cx-Freeze
	```
2. Create a `setup.py` file in the same directory as your script with the following content:
	```python
	import sys
	from cx_Freeze import setup, Executable

	# Change 'main.py' to your script's filename
	executables = [Executable('main.py')]

	setup(name='PasswordExtractor',
	      version='1.0',
	      description='Description of your project',
	      executables=executables)
	```

3. Open a terminal and navigate to the directory containing your script and the `setup.py` file.
	```bash
	cd src
	```
4. Create the executable:
	```bash
	python setup.py build
	```
5. The executable will be created in the `build` directory within your script's directory.

### Running the Executable

Once the executable is created, you can run it directly on compatible systems without needing Python installed. Keep in mind that the resulting executable may be flagged by some antivirus software due to its behavior of extracting and sending password data.

**Note:** Creating an executable doesn't change the fact that the script involves sensitive operations and should be used ethically and responsibly.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the repository on GitHub.
    
2.  Create a new branch with a descriptive name:
    
    ```bash
    git checkout -b feature/your-feature-name
    ``` 
    
3.  Make your changes and commit them:
    
    ```bash
    git commit -m "Add your commit message here"
    ``` 
    
4.  Push your changes to your forked repository:
    
    ```bash
    git push origin feature/your-feature-name
    ``` 
    
5.  Open a pull request on the original repository, explaining your changes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Disclaimer

This project and its associated source code, tools, and files are provided for educational and research purposes only. The author(s) of this project take NO responsibility and/or liability for any consequences that may arise from how you choose to use any of the provided tools, source code, or files. The script is intended for educational use only. It is important to respect privacy and obtain proper authorization before extracting passwords from any device.

**USE AT YOUR OWN RISK.**

Please ensure that you have the necessary permissions and consent before using this tool on any system or network. Unauthorized use or any malicious activities are strictly prohibited.

By using Browser Password Decryptor, you agree to comply with all applicable laws and regulations. The authors are not responsible for any misuse, damage, or any other potential harm caused by the use of this project.

Always use this tool responsibly and respect the privacy and security of others. If you are uncertain about the legality or ethical implications of using this tool, seek advice from legal and ethical experts before proceeding.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/BinaryBeast007/browser-password-decryptor/blob/main/LICENSE) file for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

