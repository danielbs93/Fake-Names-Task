import concurrent.futures
import json
import requests
import time
from config import configURLaccess


class NamesGenerator:

    def __init__(self):
        self.names = []
        self.scrapping_time = None

    def load_url(self, url: str) -> json:
        """
        Scrapping the names from the given url by accessing its text property since there is no API!
        :param url: URL of the names url
        :return: first name and last name
        """
        response = requests.get(url, timeout=configURLaccess.TIMEOUT, headers=configURLaccess.HEADERS)
        extracting_name = response.text.split('<h3>')[1]
        extracting_name = extracting_name.split('</h3>')[0]
        first_name, middle_name, last_name = extracting_name.split(' ')
        return (f'{first_name} {middle_name}', last_name)

    def populate_names_from_url(self) -> bool:
        with concurrent.futures.ThreadPoolExecutor(max_workers=configURLaccess.MAX_WORKERS) as executor:
            future_to_url = (executor.submit(self.load_url, configURLaccess.URL) for i in range(configURLaccess.CONNECTIONS))
            time1 = time.time()
            for future in concurrent.futures.as_completed(future_to_url):
                try:
                    data = future.result()
                except Exception as exc:
                    data = str(type(exc))
                    return False
                finally:
                    self.names.append(data)

            self.scrapping_time = time.time() - time1
            return True
