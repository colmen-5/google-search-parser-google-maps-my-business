thonimport requests
from bs4 import BeautifulSoup

class GoogleParser:
    def __init__(self, query, country_code='US'):
        self.query = query
        self.country_code = country_code
        self.url = f"https://www.google.com/search?q={query}&hl={country_code}"

    def extract_business_info(self):
        # Request the Google search results page
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting business information from the right-side box (assuming the HTML structure)
        business_info = {
            'company_name': self.query.split()[0],
            'website': self._extract_website(soup),
            'phone_number': self._extract_phone_number(soup),
            'address': self._extract_address(soup),
            'reviews': self._extract_reviews(soup),
            'social_accounts': self._extract_social_accounts(soup),
        }

        return business_info

    def _extract_website(self, soup):
        # Example extraction, needs actual HTML structure to work
        website = soup.find('a', {'href': True, 'class': 'BVG0Nb'})
        return website['href'] if website else None

    def _extract_phone_number(self, soup):
        # Example extraction, needs actual HTML structure to work
        phone = soup.find('span', {'class': 'LrzXr'})
        return phone.get_text() if phone else None

    def _extract_address(self, soup):
        # Example extraction, needs actual HTML structure to work
        address = soup.find('span', {'class': 'LrzXr'})
        return address.get_text() if address else None

    def _extract_reviews(self, soup):
        # Example extraction, needs actual HTML structure to work
        reviews = soup.find('span', {'class': 'Aq14fc'})
        return int(reviews.get_text()) if reviews else 0

    def _extract_social_accounts(self, soup):
        # Example extraction, needs actual HTML structure to work
        social_accounts = {}
        facebook = soup.find('a', {'href': True, 'aria-label': 'Facebook'})
        if facebook:
            social_accounts['facebook'] = facebook['href']
        twitter = soup.find('a', {'href': True, 'aria-label': 'Twitter'})
        if twitter:
            social_accounts['twitter'] = twitter['href']
        return social_accounts