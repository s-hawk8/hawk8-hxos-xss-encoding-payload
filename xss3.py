import urllib.parse
import html
import base64
import random
import requests

def url_encode(s):
    return urllib.parse.quote(s)

def double_url_encode(s):
    return urllib.parse.quote(urllib.parse.quote(s))

def html_entity_encode(s):
    return ''.join(f'&#{ord(c)};' for c in s)

def html_entity_hex_encode(s):
    return ''.join(f'&#x{ord(c):x};' for c in s)

def unicode_escape(s):
    return s.encode('unicode_escape').decode()

def base64_encode(s):
    return base64.b64encode(s.encode()).decode()

def hex_encode(s):
    return ''.join(f'%{ord(c):02x}' for c in s)

def js_escape(s):
    def escape_char(c):
        o = ord(c)
        if o < 256:
            return f'\\x{o:02x}'
        else:
            return f'\\u{o:04x}'
    return ''.join(escape_char(c) for c in s)

encoders = [
    url_encode,
    double_url_encode,
    html_entity_encode,
    html_entity_hex_encode,
    unicode_escape,
    base64_encode,
    hex_encode,
    js_escape,
]

def random_combine_encode(s, max_depth=5):
    encoded = s
    depth = random.randint(1, max_depth)
    for _ in range(depth):
        encoder = random.choice(encoders)
        encoded = encoder(encoded)
    return encoded

def save_to_file(results, filename="encoded_results.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for i, res in enumerate(results, 1):
            f.write(f"[Random Combined Encoding {i}]:\n{res}\n\n")
    print(f"Results saved to {filename}")

def test_on_url(results, url, method="GET"):
    print(f"Testing {len(results)} payloads on {url} using {method} ...")
    for i, payload in enumerate(results, 1):
        try:
            if method == "GET":
                r = requests.get(url, params={"payload": payload}, timeout=5)
            else:  # POST
                r = requests.post(url, data={"payload": payload}, timeout=5)
            print(f"Test {i}: Status {r.status_code}")
        except Exception as e:
            print(f"Test {i}: Error {e}")

if __name__ == "__main__":
    user_input = input("Enter your script or HTML tag: ")
    results = [random_combine_encode(user_input) for _ in range(20)]
    for i, res in enumerate(results, 1):
        print(f"\n[Random Combined Encoding {i}]:\n{res}")

    choice = input("\nDo you want to save results to a file? (y/n): ").strip().lower()
    if choice == 'y':
        filename = input("Enter filename (default: encoded_results.txt): ").strip()
        if not filename:
            filename = "encoded_results.txt"
        save_to_file(results, filename)

    choice = input("\nDo you want to test these payloads on a URL? (y/n): ").strip().lower()
    if choice == 'y':
        url = input("Enter the URL to test (e.g. https://example.com/test): ").strip()
        method = input("Choose HTTP method (GET/POST): ").strip().upper()
        if method not in ["GET", "POST"]:
            print("Invalid method, defaulting to GET")
            method = "GET"
        test_on_url(results, url, method)