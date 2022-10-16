# to write convertL

def convertL(country_list):
    country_dict = {}

    for country_tuple in country_list:
        country = {country_tuple[0]:country_tuple[1]}
        country_dict.update(country)
    
    def getkey(x):
        code = x[1].replace('+','')
        return int(code)

    sorted_country_dict = {k: v for k, v in sorted(country_dict.items(), key=getkey)}
    
    return sorted_country_dict

# given
n = int(input())
L = []
for i in range(n):
    L.append(input().split())

print(convertL(L))