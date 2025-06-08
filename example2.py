import urllib.parse
import html
import base64
import random
import re

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
    # Escape characters as \xHH or \uHHHH
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

if __name__ == "__main__":
    user_input = input("Enter your script or HTML tag: ")
    for i in range(20):
        result = random_combine_encode(user_input)
        print(f"\n[Random Combined Encoding {i+1}]:\n{result}")
