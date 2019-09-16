import urllib3
import json

# disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class BiliApi:
    '''Main class for api call.'''

    def __init__(self):
        self.http = urllib3.PoolManager()


    def get_video_view(self, aid):
        response = self.http.request('GET', 'https://api.bilibili.com/x/web-interface/view?aid={0}'.format(aid))
        if response.status == 200:
            html = response.data.decode()
            obj = json.loads(html)
        return obj


    def get_video_tags(self, aid):
        response = self.http.request('GET', 'https://api.bilibili.com/x/tag/archive/tags?aid={0}'.format(aid))
        if response.status == 200:
            html = response.data.decode()
            obj = json.loads(html)
        return obj


    def get_member(self, mid):
        response = self.http.request('GET', 'https://api.bilibili.com/x/space/acc/info?mid={0}'.format(mid))
        if response.status == 200:
            html = response.data.decode()
            obj = json.loads(html)
        return obj
