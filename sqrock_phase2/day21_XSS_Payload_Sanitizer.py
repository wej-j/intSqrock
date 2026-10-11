import html
import re

def sanitize_user_input(raw_payload):
    # Perform strict encoding step followed by active pattern strip-down
    encoded_string = html.escape(raw_payload)
    stripped_output = re.sub(r"(?i)script|onerror|onload", "[PROHIBITED_TOKEN]", encoded_string)
    return stripped_output

malicious_input = "<script>alert('XSS')</script>"
sanitized = sanitize_user_input(malicious_input)
print(f"Raw Input: {malicious_input}\nNeutralized Result: {sanitized}")

test_payloads = [
    "<script>alert('XSS')</script>", "<SCRIPT>alert('test')</SCRIPT>",
    "<img src=x onerror=alert('XSS')>", "<body onload=alert('XSS')>",
    "<script>console.log('test')</script>", "<div onload='test()'>Hello</div>",
    "<img onerror='test()'>", "<script src='test.js'></script>",
    "<p>script test</p>", "<input onload='example'>" ]

for payload in test_payloads:
    print("\nRaw Input:", payload)
    print("Neutralized:", sanitize_user_input(payload))