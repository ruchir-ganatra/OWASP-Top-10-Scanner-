import requests
from bs4 import BeautifulSoup

# Common headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to check for basic SQL Injection vulnerability
def check_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url, params={"input": payload}, headers=HEADERS)
    if "error" in response.text or "syntax" in response.text:
        return True
    return False

# Function to check for XSS vulnerability
def check_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={"input": payload}, headers=HEADERS)
    if payload in response.text:
        return True
    return False

# Main function to scan the site
def scan_site(url):
    print(f"Scanning {url} for OWASP Top 10 vulnerabilities...")
    vulnerabilities = []

    # Check for SQL Injection
    if check_sql_injection(url):
        vulnerabilities.append("SQL Injection")

    # Check for XSS
    if check_xss(url):
        vulnerabilities.append("Cross-Site Scripting (XSS)")

    if vulnerabilities:
        print(f"Vulnerabilities found: {', '.join(vulnerabilities)}")
    else:
        print("No vulnerabilities found!")

# Entry point
if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    scan_site(target_url)
