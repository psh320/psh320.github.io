import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


def get_finance_data(code):
    url_temp = 'https://finance.naver.com/item/main.nhn?code=%s'
    url = url_temp % (code)

    item_info = requests.get(url).text
    soup = BeautifulSoup(item_info, 'html.parser')
    finance_info = soup.select('div.section.cop_analysis div.sub_section')[0]

    # get PER for similar company
    temp_per = soup.find("table", {"summary": "동일업종 PER 정보"})
    similar_per = temp_per.find('em')
    similar_per = similar_per.get_text()
    print(similar_per)

    th_data = [item.get_text().strip() for item in finance_info.select('thead th')]
    annual_date = th_data[3:7]
    quarter_date = th_data[7:13]

    finance_index = [item.get_text().strip() for item in finance_info.select('th.h_th2')][3:]

    finance_data = [item.get_text().strip() for item in finance_info.select('td')]
    finance_data = np.array(finance_data)
    finance_data.resize(len(finance_index), 10)

    finance_date = annual_date + quarter_date

    finance = pd.DataFrame(data=finance_data[0:,0:], index = finance_index, columns = finance_date)

    print(finance)
    return finance


def get_net_income(data):
    net_income = [0, 0, 0, 0]
    for i in range(4):
        net_income[i] = data.iloc[2].iloc[i]

    print(net_income)
    return(net_income)


def get_debt_ratio(data):
    debt_ratio = [0, 0, 0, 0]
    for i in range(4):
        debt_ratio[i] = data.iloc[6].iloc[i]

    print(debt_ratio)
    return(debt_ratio)


def get_quick_ratio(data):
    quick_ratio = [0, 0, 0, 0]
    for i in range(4):
        quick_ratio[i] = data.iloc[7].iloc[i]

    print(quick_ratio)
    return(quick_ratio)


def get_reserve_ratio(data):
    reserve_ratio = [0, 0, 0, 0]
    for i in range(4):
        reserve_ratio[i] = data.iloc[8].iloc[i]

    print(reserve_ratio)
    return(reserve_ratio)


df = get_finance_data('079430')
income = get_net_income(df)

print(df)
print(income)

