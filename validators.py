import requests

# Function to download the TLD list and create a set of valid TLDs
def get_valid_tlds():
    response = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
    tlds = response.text.strip().split("\n")[1:]
    return tlds

print(get_valid_tlds())
print(len(get_valid_tlds()))
