# 모듈 불러오기
import dart_fss as dart

api_key = '1d6d64597b62335da9ff581b734b17eda385ac39'  # api key 변수 설정
dart.set_api_key(api_key=api_key)   # 인증 설정
crp_list = dart.get_corp_list()  # 상장회사 정보 리스트 받아오기
basic_info = crp_list.find_by_corp_name('삼성전자', exactly=True)[0] # 삼성전자 종목코드를 파라미터로 넣어 삼성전자 기본 정보 가져오기
print(basic_info)

fs = basic_info.extract_fs(bgn_de='20180101')
print(fs)

#the_statements = fs['fs'[0]]  # 크롤링한 데이터 중 재무상태표(fs : financial statements)만 선택하여 변수 할당
fs_dict = fs.to_dict()
print(fs_dict)