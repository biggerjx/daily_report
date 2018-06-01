import requests
import json
import pandas

def get_swaggerData(url ):
    res = requests.get(url)
    res.encoding = "utf-8"
    jd = json.loads(res.text)
    print(jd['paths'])  #输出所有接口
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

    #print(result) #接口list
    #print(len(result)) #接口数

    #df = pandas.DataFrame(result)
    #print(df.head(5)) 打印前几条数据
    #df.to_excel("API.xlsx") #导出文件

    return result

def get_tag_result(url,tag= ''):
    get_swaggerData(url)


if __name__ == '__main__':
    url = "http://xqy-finance.sit.91lyd.com/xqy-portal-web/finance/v2/api-docs"
  #  flieName = 'output1.xlsx'
    get_swaggerData(url)


            # if "tags" in  msg1[key2]:
            #     print(msg1[key2]['tags'])
            #     #result['tags'] = msg1[key2]['tags']
            # else:
            #     result['tags'] = ''
            # if tag in msg1[key2]['tags']:
            #     result_list['tags'] = msg1[key2]['tags']
            #     print(result_list)
            # else:
            #     pass