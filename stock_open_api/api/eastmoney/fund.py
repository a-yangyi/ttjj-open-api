
from stock_open_api.utils import request_util

# 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNMangerList'


# url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/PageAjax'
url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNMangerList'

params = {
    'FCODE': '003834',
}

tt_url = "https://fundcomapi.tiantianfunds.com/mm/newCore/FundVPageDiagram"
res = request_util.post_ttjj(tt_url, {"FCODE":"025491"})
print("=====\n")
# print(res.json())