from urllib.parse import quote_plus

from httpclients.base_httpclient import BaseHttpClient
from httpclients.responsemodels.cves_response import CvesResponse


class NvdHttpClient(BaseHttpClient):
    """Derived HttpClient to handle interacting with NIST NVD (National Vulnerability Database)"""
    def __init__(self, base_url: str):
        print("DEBUG: initialising NvdHttpClient")
        super().__init__(base_url)
        self.cves_url = "rest/json/cves/2.0"

    def find_cves_by_keywords(self, keywords: str) -> CvesResponse:
        print("DEBUG: called find_cves_by_keywords")
        keywords = keywords
        cves_response = self.get(self.cves_url, params={"keywordSearch": keywords})
        print(f"TRACE: got response from NVD API\n{cves_response}")
        return CvesResponse.parse_json(cves_response)