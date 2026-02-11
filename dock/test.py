import requests

import logging

logging.setLoggerClass(logging.Logger)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def test_script():
    url = "https://api.github.com/repos/anchore/grype/releases/latest"
    headers = {
        "accept": "application/json"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        data = res.json()
        logging.info(f"Latest release: {data['tag_name']}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    test_script()