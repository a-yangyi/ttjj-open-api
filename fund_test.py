# -*- coding: utf-8 -*-

from stock_open_api.utils import request_util
import time
import random
from pathlib import Path
import json

# 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNMangerList'


# url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/PageAjax'
# url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNMangerList'
# params = {
#     'FCODE': '003834',
# }

prodcut_list = [
    "013943",
    "005538",
    "004433",
    "019671",
    "025491",
    "016453",
    "008763",
    "161724"
]

tt_url = "https://fundcomapi.tiantianfunds.com/mm/newCore/FundVPageDiagram"

for product in prodcut_list:
    res = request_util.post_ttjj(tt_url, {"FCODE":product})
    with open(Path(f"data/{product}.json"), "w", encoding="utf-8") as f:
        chars_written = f.write(json.dumps(res.json(), indent=4) )
        # chars_written = f.write("hi")
    #     print(f"{chars_written} characters written.")
    wait_secs = random.randint(3, 5)
    print("=====\n")
    print(f"{product} finished, sleeping {wait_secs} secs \n")
    time.sleep(wait_secs)
    # print("===res===\n")
    # print(res.json())


# from stock_open_api.api.sse import sh_stock

# if __name__ == '__main__':
#     print(sh_stock.get_company_info('600010'))