# Password Hacking Tool

## Introduction
This Python-based tool is designed to perform a combination of dictionary and timing attacks to hack passwords. It uses a brute-force approach, iterating over combinations of usernames and passwords until it successfully logs in.

## Features
- **Dictionary Attacks**: Utilizes predefined lists of usernames and passwords.
- **Timing Attacks**: Employs time analysis to guess passwords more efficiently.
- **Customizable Target**: Can be configured to attack any hostname and port.

## Installation
To use this tool, you need Python installed on your system. No additional libraries are required.

## Usage
Run the script from the command line by providing the target hostname and port. For example:

```bash
python hacking_hack.py 127.0.0.1 9090
```

## Files
- *passwords.txt*: Contains a list of potential passwords.
- *logins.txt*: Contains a list of potential usernames.

## Warning
This tool is provided for educational purposes only. Unauthorized hacking is illegal and unethical. Use this tool only in legal and ethical contexts, such as penetration testing with permission.

