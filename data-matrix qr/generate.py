import requests

baseurl = "https://barcode.orcascan.com/?type=datamatrix&data="


for i in range(1, 61):
    # make 1 as 01
    url = baseurl + str(i).zfill(2)
    print(url)
    # call api to generate qr code and save it
    response = requests.get(url)
    with open(f"output/{str(i).zfill(2)}.svg", "wb") as f:
        f.write(response.content)
