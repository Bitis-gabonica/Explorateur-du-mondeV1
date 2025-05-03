import requests

def fetch_country_data_by_code(code):
    url = f"https://restcountries.com/v3.1/alpha/{code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]

        # Extraction des champs utiles
        name = data['name']['common']
        capital = data.get('capital', [''])[0]
        region = data.get('region', '')
        flag_url = data.get('flags', {}).get('png', '')

        languages = ', '.join(data.get('languages', {}).values())

        currencies = data.get('currencies', {})
        currency = next(iter(currencies.values()), {}).get('name', '')

        timezone = data.get('timezones', [''])[0]

        return {
            'name': name,
            'code': code.upper(),
            'capital': capital,
            'region': region,
            'flag_url': flag_url,
            'languages': languages,
            'currency': currency,
            'timezone': timezone,
        }
    except Exception as e:
        print(f"Erreur lors de la récupération du pays {code}: {e}")
        return None
