import requests
import json
import pandas

def get_swaggerData(url):
    res = requests.get(url)
    res.encoding = "utf-8"
    jd = json.loads(res.text)
    #print(jd['paths'])  #输出所有接口
    result = []
    for api_message in jd['paths']:
        result_list = {} #用于放每个请求的信息
        result_list['接口名'] = api_message
        msg1 = jd['paths'][api_message] #每个接口的详细信息

        for key2 in msg1:
            result_list['请求方式']= key2 #请求方式
            #接口的明细信息，msg1[key2]代表请求方式中的dict{}
            result_list['接口描述'] = msg1[key2]['summary'] #备注
            result_list['版本标记'] = msg1[key2]['tags'] #tag信息
        result.append(result_list)

    # print(result)
    # print(len(result))
    return result

def output_api(api_data,tag = ""):
    df = pandas.DataFrame(api_data)
    df.to_excel("API-"+tag+".xlsx") #导出文件
    #print(df.head(5)) 打印前几条数据
    return None


def get_api_result(url,tag=None):
    api_datas = get_swaggerData(url)
    if tag is None:
        search_api = get_swaggerData(url)
        output_api(search_api,"all")

    else:
        search_api = []
        for api in api_datas:
            if tag in api["版本标记"]:
                search_api.append(api)
            else:
                pass
        print(search_api)
        print(len(search_api))
        output_api(search_api,tag)

    return search_api

if __name__ == '__main__':
    url = "http://xqy-finance.sit.91lyd.com/xqy-portal-web/finance/v2/api-docs"
    get_api_result(url)