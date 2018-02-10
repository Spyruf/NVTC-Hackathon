import urllib.request

url = urllib.request.urlopen('https://www.mentalhealth.va.gov/docs/data-sheets/Suicide-Data-Sheets-VA-States.pdf')

for line in url:
    try:
        line = line.decode('utf-8').strip()
        print(line)
    except:
        print("err")