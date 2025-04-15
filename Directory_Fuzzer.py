import requests 

def fuzz_directory(base_url, wordlist):
    print(f"Fuzzing {base_url} for directories...\n")
    found = []

    for word in wordlist:
        url = f"{base_url}/{word.scrip()}"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[+] Found: {url}")
            found.append(url)
        elif response.status_code == 403:
            print(f"[-] Forbidden: (403): {url}")

        return found
    
if __name__ == "__main__":
    base_url = input("Enter the website URL (e.g. http://example.com): ")
    wordlist = ["admin", "login", "uploads", "images", "css", "js", "dashboard", "config"]

    fuzz_directory(base_url, wordlist)