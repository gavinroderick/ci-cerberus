from httpclients.nvd_httpclient import NvdHttpClient


if __name__ == '__main__':
    nvd_client = NvdHttpClient("https://services.nvd.nist.gov/")
    cves = nvd_client.find_cves_by_keywords("tj-actions")

    print(cves)

