from pykiwoom.kiwoom import *

# https://wikidocs.net/77481
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# https://wikidocs.net/77482
account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부

print(account_num)
print(accounts)
print(user_id)
print(user_name)
print(keyboard)
print(firewall)

# https://wikidocs.net/77483
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)

# https://wikidocs.net/77484
name = kiwoom.GetMasterCodeName("005930")
print(name)

# https://wikidocs.net/77489
전일가 = kiwoom.GetMasterLastPrice("005930")
print(int(전일가))
print(type(전일가))