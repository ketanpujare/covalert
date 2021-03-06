from datetime import datetime
from requests import get
import json


class CowinAPI(object):
    def __init__(self) -> None:
        super().__init__()
        self.base_url = 'https://cdn-api.co-vin.in/api/v2/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
        }
        self.fail_meassage = """Cowin's weblink in not working"""

    @staticmethod
    def get_today_date() -> str:
        today = datetime.today()
        return today.strftime("%d-%m-%Y")

    def api_status(self) -> bool:
        url = '{}admin/location/states'.format(self.base_url)
        r1 = get(url, headers=self.headers)
        if r1.status_code == 200:
            return True, r1.status_code
        return False, r1.status_code

    def get_states(self) -> json:
        url = '{}admin/location/states'.format(self.base_url)
        r1 = get(url, headers=self.headers)
        if r1.status_code != 200:
            return self.fail_meassage, r1.status_code
        return r1.json().get('states'), r1.status_code

    def get_districts(self, state_id) -> json:
        url = '{}admin/location/districts/{}'.format(self.base_url, state_id)
        r1 = get(url, headers=self.headers)
        if r1.status_code != 200:
            return self.fail_meassage, r1.status_code
        return r1.json().get('districts'), r1.status_code

    def get_avail_disricts(self, district_id) -> json:
        url = '{}appointment/sessions/public/calendarByDistrict?district_id={}&date={}'.format(
            self.base_url, district_id, self.get_today_date())
        r1 = get(url, headers=self.headers)
        if r1.status_code != 200:
            return self.fail_meassage, r1.status_code
        return r1.json().get('centers'), r1.status_code


if __name__ == '__main__':
    pass
