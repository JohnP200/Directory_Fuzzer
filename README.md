# Directory Fuzzer (Python)

This Python script brute-forces common directories on a website using a simple wordlist.

## Features

- Scans for hidden or common paths like `/admin`, `/login` `/uploads`, etc.
- Reports open (HTTP 200) and forbidden (HTTP 403) directories

## Usage 

```bash
python directory_fuzzer.py

## Example
Enter the target URL (e.g., https://example.com): http://example.com
Enter the path to the wordlist (e.g., wordlist.txt): wordlist.txt
[200] http://example.com/admin
[200] http://example.com/login

## Disclaimer
This tool is for educational and authorized penetration testing only. Do not use it on domains you do not own or have permission to test.

## License
MIT License