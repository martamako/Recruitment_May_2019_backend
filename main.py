import requests
import json
import pandas as pd
import urllib


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main():
    response = requests.get("https://api.dane.gov.pl/1.4/resources/44100,liczba-osob-ktore-przystapiyzday-egzamin-maturalny?lang=pl")
    json_response = response.json()
    csv_url = json_response["data"]["attributes"]["link"]
    data = pd.read_csv(csv_url, sep=";")
    print(data.to_string())
    jprint(response.json())


if __name__ == '__main__':
    main()
