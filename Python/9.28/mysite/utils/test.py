#-*- coding: UTF-8 -*-

import json
from aiapi import AiPlat

app_key = 'vEQWKdz21sJaplLT'
app_id = '2109279359'

str_text = ('今天天气怎么样')
type = 0
ai_obj = AiPlat(app_id, app_key)

print('----------------------SEND REQ----------------------')
rsp = ai_obj.getNlpTextTrans(str_text, type)
if rsp['ret'] == 0:
    print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
    print('----------------------API SUCC----------------------')
else:
    print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
    # print rsp
    print('----------------------API FAIL----------------------')




import os
import json
import hashlib
import base64

seq = 0
format_id = 3
rate = 16000
bits = 16
cont_res = 1
once_size = 6400
file_path = 'test.amr'
f = open(file_path, 'rb')
md5obj = hashlib.md5()
md5obj.update(f.read())
hash = md5obj.hexdigest()
speech_id = str(hash).upper()
# speech_id = "test12"
f.close()
f = open(file_path, 'rb')
file_size = os.path.getsize(file_path)
print(file_size)
try:
    while True:
        chunk = f.read()
        chunk_new = base64.b64encode(f.read())
        if not chunk:
            break
        else:
            chunk_size = len(chunk)
            if (seq + chunk_size) == file_size:
                end = 1
            else:
                end = 0

        ai_obj = AiPlat(app_id, app_key)

        print('----------------------SEND REQ----------------------')
        # rsp = ai_obj.getAaiWxAsrs(chunk, speech_id, end, for_mat, rate, bits, seq, chunk_size, cont_res)
        end=1
        rsp = ai_obj.getAaiAsr( chunk_new , end ,format_id, rate)
        seq += chunk_size
        if rsp['ret'] == 0:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
            print('----------------------API SUCC----------------------')
        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
            print('----------------------API FAIL----------------------')
finally:
    f.close()
