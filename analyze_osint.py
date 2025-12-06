import requests
from bs4 import BeautifulSoup, Comment
import sys

def analyze_page(url):
    try:
        print(f"[*] Analyzing {url}...")
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\n[+] Title:")
        if soup.title:
            print(f"    {soup.title.string.strip()}")
        else:
            print("    No title found")
            
        print("\n[+] Meta Tags:")
        for meta in soup.find_all('meta'):
            name = meta.get('name', meta.get('property', ''))
            content = meta.get('content', '')
            if name or content:
                print(f"    - {name}: {content}")
                
        print("\n[+] Comments (Potential Hidden Info):")
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for comment in comments:
            print(f"    - {comment.strip()}")
            
        print("\n[+] Links (href):")
        for link in soup.find_all('a', href=True):
            print(f"    - {link.text.strip()} -> {link['href']}")
            
        print("\n[+] Images (src):")
        for img in soup.find_all('img', src=True):
            print(f"    - {img.get('alt', 'No alt')} -> {img['src']}")

        print("\n[+] Scripts (src):")
        for script in soup.find_all('script', src=True):
            print(f"    - {script['src']}")

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_osint.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    analyze_page(url)
