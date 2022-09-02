# -*- coding:utf-8 -*-

import re
import sys
import subprocess
import datetime
import pandas as pd


# 传入url
def get_cert_info(url):
    try:
        cmd = f"curl -Ivs {url} --connect-timeout 10"
        exitcode, output = subprocess.getstatusoutput(cmd)
        common_name = re.search('common name: (.*)', output).group(1)
        start_date = re.search('start date: (.*)', output).group(1)
        expire_date = re.search('expire date: (.*)', output).group(1)
        return [common_name, start_date, expire_date]
    except:
        return ['', '', '']


# 证书信息扫描，生成df
def ssl_df(filepath):
    df_ssl = pd.DataFrame(columns=['url', 'common_name', 'start_date', 'expire_date'])
    f = open(filepath, 'r') 
    lines = f.readlines()
    for url in lines:
        if 'https://' in url:
            try:
                data = get_cert_info(url)
                common_name = data[0]
                GMT_FORMAT =  '%b %d %H:%M:%S %Y GMT'
                start_date = datetime.datetime.strptime(data[1],GMT_FORMAT)
                expire_date = datetime.datetime.strptime(data[2],GMT_FORMAT)

                df_ssl = df_ssl.append({'url':url, 'common_name':common_name, 'start_date':start_date, 'expire_date':expire_date}, ignore_index=True)
            except:
                continue
    df_ssl.index = df_ssl.index + 1
    return df_ssl


def main():
    filepath = sys.argv[1]
    with pd.ExcelWriter('./result.xlsx') as writer:
        ssl_df(filepath).to_excel(writer, sheet_name="ssl_info")


if __name__ == "__main__":
    main()
