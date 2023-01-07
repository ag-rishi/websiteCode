import requests

my_file = open("C:\\Users\\rishi\\Documents\\PYTHON\\CLEANLINKSFRESHEST.txt", "r")
weblist = my_file.readlines()
weblist = list(map(lambda s: s.strip(), weblist))

i = 0
while i < len(weblist):
    try: 
        r = requests.head(weblist[i])
        if r.status_code == 200:  
            print(weblist[i])
    except requests.ConnectionError:
        pass
    i = i + 1