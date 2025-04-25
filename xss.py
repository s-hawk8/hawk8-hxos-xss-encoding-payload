import urllib.parse
import html
import base64
import random

def url_encode(s):
    return urllib.parse.quote(s)

def html_entity_encode(s):
    return ''.join(f'&#{ord(c)};' for c in s)

def unicode_escape(s):
    return s.encode('unicode_escape').decode()

def base64_encode(s):
    return base64.b64encode(s.encode()).decode()
    

# لیست توابع انکدینگ
encoders = [url_encode, html_entity_encode, unicode_escape, base64_encode]

def random_combine_encode(s, max_depth=3):
    encoded = s
    depth = random.randint(1, max_depth)  # تعداد لایه‌های انکدینگ تصادفی
    for _ in range(depth):
        encoder = random.choice(encoders)
        encoded = encoder(encoded)
    return encoded

if __name__ == "__main__":
    user_input = input("Enter your script or HTML tag: ")
    for i in range(20):  # ۵ خروجی ترکیبی تصادفی تولید می‌کند
        result = random_combine_encode(user_input)
        print(f"\n[Random Combined Encoding {i+1}]:\n{result}")