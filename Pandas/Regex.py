Regular Expression (Regex) – What & Why?

English:
Regex = A pattern matching tool used to search, extract, or manipulate strings.
বাংলায়:
Regex basically হলো এমন একটা pattern, যেটা দিয়ে আমরা কোনো string এর মধ্যে নির্দিষ্ট data খুঁজে বের করতে, replace করতে বা filter করতে পারি।

🔹 Basic Syntax

. → Any character (except newline)

* → 0 or more repetitions

+ → 1 or more repetitions

? → 0 or 1 repetition

\d → Any digit (0–9)

\D → Non-digit

\w → Word character (letters, digits, underscore)

\W → Non-word character

\s → Space

^ → Start of string

$ → End of string

[] → Match any one character inside bracket

() → Group

🔹 Simple Python Regex Example
import re

# Example text
text = "My phone number is 01712345678 and email is test123@gmail.com"

# Find digits (phone number like)
phones = re.findall(r'\d+', text)  
print("Digits found:", phones)  # ['01712345678', '123']

# Find email
email = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}', text)
print("Email found:", email)  # ['test123@gmail.com']


👉 এখানে \d+ মানে হলো এক বা একাধিক digit খুঁজবে।
👉 Email এর regex pattern দিয়ে email ধরছি।

🔹 Regex with Pandas

Pandas এ Regex **সবচেয়ে বেশি ব্যবহৃত হয় → str.contains(), str.extract(), str.replace() এ।

Example 1: Filtering rows with regex
import pandas as pd

data = {
    "Name": ["Anisa Rahman", "Abdullah Al Kawser", "Rafi", "Sumi Akter"],
    "Email": ["anisa123@gmail.com", "kawser2025@yahoo.com", "rafi99@gmail.com", "sumi@outlook.com"]
}

df = pd.DataFrame(data)

# Filter only Gmail users
gmail_users = df[df["Email"].str.contains(r'@gmail\.com', regex=True)]

print(gmail_users)


✅ Output: শুধু Gmail এর user দেখাবে।

Example 2: Extracting username from email
# Extract username part before @
df["Username"] = df["Email"].str.extract(r'(^[a-zA-Z0-9._%+-]+)')
print(df)


👉 extract() regex দিয়ে column থেকে specific অংশ আলাদা করতে ব্যবহার হয়।

Example 3: Replacing text with regex
# Replace domain with "hidden.com"
df["SafeEmail"] = df["Email"].str.replace(r'@.*', '@hidden.com', regex=True)
print(df)


👉 সব email এর domain @hidden.com দিয়ে replace হবে।

🔹 Practical Use Cases

Phone Number validation

Email extraction

Remove unwanted characters ([^a-zA-Z0-9 ])

Search/filter rows with conditions

Clean text data (logs, reviews, social media posts)