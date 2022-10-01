import json
import re
import requests

class getGigazineInfo:
    def __init__(self, session=False):
        if session == False:
            self.session = requests.session()
        else:
            self.session = session

    def get(self, url):
        self.response = self.session.get(url)
        if self.response.status_code != 200:
            raise Exception('Request Error')
        reg_struct = r'<script type="application/ld\+json">\s([\s\S]*?)\s</script>'
        struct = json.loads(re.findall(reg_struct, self.response.text)[0])

        reg_tag = r'<span class="yeartime p-category"><a href="(\S*?)">(\S*?)</a></span>'
        tag = re.findall(reg_tag, self.response.text)[0]

        return {
            "struct":struct,
            "tag":tag
        }