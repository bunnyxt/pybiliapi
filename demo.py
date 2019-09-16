#import pybiliapi

from pybiliapi import *

bapi = BiliApi()

obj = bapi.get_video_view(456930)
print(obj)

obj = bapi.get_video_tags(456930)
print(obj)

obj = bapi.get_member(487708)
print(obj)