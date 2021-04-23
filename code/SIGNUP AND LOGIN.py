#import FILEMANAGE
import os.path
import sys
import re
import random
import datetime

"""
마지막 수정 : 2021-04-18 03:12 am
<수정 사항>
1. 회원 정보 입력 : <이름><비개행공백열1><주민등록번호>로 바꾸기 O
2. 회원관리파일에 회원 정보 저장할 때, 구분자 탭으로 바꾸기 O
3. 회원 정보 기획서대로 짜맞추기 O
4. ID 문법 규칙 수정 O

<수정 사항>
마지막 수장 : 2021-04-24 01:40 am
1. 주민등록번호 의미규칙(중복 처리) 반영
2. open()하면 close() 명확히 처리

"""

class UserManager:

     user_file = os.path.expanduser('~') + "\\account-data" + "\\회원관리폴더" + "\\users.txt"
     account_folder = os.path.expanduser('~') + "\\account-data" + "\\계좌폴더"

     # ID 문법 규칙
     ID_match1 = "^(?=.*[a-z])(?=.*\d)[a-z\d]{1,}$"
     ID_match2 = "^(?=.*[a-z])(?=.*[-_])[a-z-_]{1,}$"
     ID_match3 = "^(?=.*\d)(?=.*[-_])[\d_-]{1,}$"
     ID_match4 = "^(?=.*[a-z])(?=.*\d)(?=.*[-_])[a-z\d_-]{1,}$"
     ID_match5 = "^(?=.*[a-z])[a-z]{1,}$"
     ID_match6 = "^(?=.*\d)[\d]{1,}$"
     ID_match7 = "^(?=.*[-_])[-_]{1,}$"

     # 비밀번호 문법 규칙
     PW_match1 = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{3,}$"
     PW_match2 = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*])[A-Za-z!@#$%^&*]{3,}$"
     PW_match3 = "^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Z\d!@#$%^&*]{3,}$"
     PW_match4 = "^(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[a-z\d!@#$%^&*]{3,}$"
     PW_match5 = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{4,}$"
     
     def __init__(self):
          pass

     def login(self):
          ID = ""
          correspond_PW = ""
          # ID 문법 규칙
          while True :
               ID = input("ID : ")
               if (len(ID) >= 5 and len(ID) <= 20) and (re.fullmatch(UserManager.ID_match1, ID)
                                                        or re.fullmatch(UserManager.ID_match2, ID) or re.fullmatch(UserManager.ID_match3, ID)
                                                        or re.fullmatch(UserManager.ID_match4, ID) or re.fullmatch(UserManager.ID_match5, ID)
                                                        or re.fullmatch(UserManager.ID_match6, ID) or re.fullmatch(UserManager.ID_match7, ID)) and ID[0] not in ['-', '_']:
                    # 문법 규칙 맞았을 경우, 해당 아이디가 유효한지 확인
                    file = open(UserManager.user_file, 'r', encoding = 'UTF-8')
                    info = file.readlines()
                    file.close()
                    find_index = -1
                    for index, user_account in enumerate(info):
                         # ID를 담는 행에서만 검색
                         if index % 4 == 1:
                              user_id = user_account.rstrip()
                              user_id = user_id.split(' ', 1)[0]
                              if ID == user_id:
                                   find_index = index
                                   correspond_PW = user_account.rstrip()
                                   correspond_PW = correspond_PW.split(' ', 1)[1]
                                   break
                    # ID가 유효할 경우
                    if not find_index == -1:
                         break
                    else:
                         print("ID를 다시 확인해주세요")
                         continue
                    
               else:
                    print("ID를 다시 확인해주세요")
                    continue
                              

                    
          # 비밀번호 문법 규칙
          while True:
               PW = input("비밀번호 : ")

               # 비밀번호 문법 규칙
               if (len(PW) >= 8 and len(PW) <= 20) and (re.fullmatch(UserManager.PW_match1, PW) or
                                                        re.fullmatch(UserManager.PW_match2, PW) or re.fullmatch(UserManager.PW_match3, PW)
                                                        or re.fullmatch(UserManager.PW_match4, PW) or re.fullmatch(UserManager.PW_match5, PW)):
                    # ID에 해당하는 비밀번호인가?
                    if PW == correspond_PW:
                         ########## 로그인 완료 ##########
                         print("로그인 완료")
                         ####### 파일 무결성 체크2 #######
                         
                         return ID # 일단 로그인 완료한 ID를 반환함으로써 메소드가 종료된다.
                    else:
                         print("비밀번호가 올바르지 않습니다.")
                         continue
               else:
                    print("비밀번호를 다시 확인해주세요")
                    continue
                 

          
     def signUp(self):
          
          # 회원 정보 입력
          while True:
               info = input("회원 정보를 입력해 주세요 : ")
               if not len(info) >= 16:
                    print("잘못된 회원정보입니다.")
                    continue
               if not info[-15].isspace():
                    print("잘못된 회원정보입니다.")
                    continue
                    
               name = ""
               iden_num = info[-14:]

               for i in range(-16, -(len(info)+1), -1):
                    if info[i].isprintable() and not info[i].isspace():
                         name = info[0:i+1]
                         break

               
               # 이름 문법 규칙 : 길이 >=1, 첫/마지막은 실상 문자, 탭/개행 X
               if not (len(name)>=1 and (name[0].isprintable() and not name[0].isspace() and name[-1].isprintable()
                                         and not name[-1].isspace()) and not any(ch in name for ch in [u'\u0009', u'\u000A', u'\u000D'])):
                    print("잘못된 이름입니다. 다시 입력해주세요")
                    continue
               

               # 주민등록번호 문법 규칙 : <6자리 생년월일><표준 공백><1,2,3,4 중 1개><6자리 숫자>
               # 14글자가 아니거나, 숫자와 표준 공백 외 다른 문자가 있을 경우
               if not len(iden_num)==14 or not iden_num[6]==' ':
                    print("잘못된 주민등록번호 형식입니다.")
                    continue
               for ch in iden_num[0:6]+iden_num[7:15]:
                    if ch not in map(lambda ch: str(ch), range(0,10)):
                         print("잘못된 주민등록번호 형식입니다.")
                         continue

               # 문법 규칙1 : 세대
               generation=0
               if iden_num[7] in ['1', '2']:
                    generation = 19
               elif iden_num[7] in ['3', '4']:
                    generation = 20
               else:
                    print("잘못된 출생 세대입니다.")
                    continue

               # 문법 규칙2 : 출생 연도(1900~2002)
               if generation==19:
                    if not (iden_num[0:2] in map(lambda m: '0'+str(m) if m<10 else str(m), range(0, 99))):
                         print("잘못된 출생연도입니다.")
                         continue
               elif generation==20:
                    if not iden_num[0:2] in ["00", "01", "02"]:
                         print("잘못된 출생연도입니다.")
                         continue
               birth_year = iden_num[0:2]

               # 문법 규칙3 : 월(01~12)
               if iden_num[2]=='0':
                    if not (iden_num[3] in map(lambda m: str(m), range(1, 10))):
                         print("잘못된 출생월입니다.")
                         continue
               elif iden_num[2]=='1':
                    if not (iden_num[3] in map(lambda m: str(m), range(0, 3))):
                         print("잘못된 출생월입니다.")
                         continue
               else:
                    print("잘못된 출생월입니다.")
                    continue
               birth_month = iden_num[2:4]

               # 문법 규칙4 : 일(각 월의 일 수 + 2월 윤년 처리)
               year = generation+int(birth_year)
               isLeap = (year%4==0 and (year%100!=0) or (year%400==0))
               birth_day = iden_num[4:6]
               if birth_month in ["01", "03", "05", "07", "08", "10", "12"]:
                    if not (birth_day in map(lambda d: '0'+str(d) if d<10 else str(d), range(1, 32))):
                         print("잘못된 출생일입니다.")
                         continue
               elif birth_month in ["04", "06", "09", "11"]:
                    if not (birth_day in map(lambda d: '0'+str(d) if d<10 else str(d), range(1, 31))):
                         print("잘못된 출생일입니다.")
                         continue
               elif birth_month=="02":
                    if isLeap:
                         if not (birth_day in map(lambda d: '0'+str(d) if d<10 else str(d), range(1, 30))):
                              print("잘못된 출생일입니다.")
                              continue
                    else:
                         if not (birth_day in map(lambda d: '0'+str(d) if d<10 else str(d), range(1, 29))):
                              print("잘못된 출생일입니다.")
                              continue

             
               # 여기까지 왔으면, 주민등록번호 문법 규칙은 통과
               

               # 회원 관리 파일 해당 회원 찾기
               file = open(UserManager.user_file, 'r', encoding = 'UTF-8')
               info = file.readlines()
               file.close()
               find_index = -1
               for index, user in enumerate(info):
                    # 회원 정보를 담고 있는 행에서만 검색
                    if index%4==0:
                          user = user.rstrip()
                          f_name, f_iden_num = user.split('\t', 1)
                          # 회원일 경우
                          if f_name == name and f_iden_num == iden_num:
                               find_index = index
                               break

               # 이미 회원인 경우
               if not find_index == -1:
                    # 제대로 된 입력을 받을 때까지 반복
                    while(True):
                         ans = input("이미 가입된 회원이십니다. 계정 찾기를 원하십니까?(y/n) : ")
                         if ans=="y":
                              account_info = info[find_index+1].rstrip()
                              account_id, account_pw = account_info.split(' ')
                              account_id = account_id[0:len(account_id)-2] + "***"
                              account_pw = account_pw[0:len(account_pw)-2] + "***"
                              # 특정 인덱스를 가린 계정 출력
                              print(f"ID : {account_id}\n비밀번호 : {account_pw}")
                              # 메서드 종료
                              return
                         elif ans=="n":
                              # 회원 정보 입력으로 돌아가기
                              break
                         else:
                              print("정확히 y 혹은 n으로만 입력해주시기 바랍니다.")
                              
               # 신규 회원인 경우
               else:
                    
                    # 주민등록번호 의미 규칙 : 다른 회원들의 주민등록번호와 중복되지 않아야 함
                    # 회원관리파일에서 모든 주민등록번호 불러오기
                    find_index = -1
                    for index, user in enumerate(info):
                         # 회원 정보를 담고 있는 행에서만 검색
                         if index%4==0:
                              user = user.rstrip()
                              f_iden_num = user.split('\t', 1)[1]
                              # 중복되는 주민등록번호인지 확인
                              if f_iden_num == iden_num:
                                   find_index = index
                                   break

                    if find_index != -1:
                         print("이미 등록된 주민등록번호입니다.")
                         continue


                    # 여기까지 왔으면, 진짜 신규 회원인 것으로 확인
                    print("신규 회원이십니다! 계정 생성을 위해 ID와 비밀번호를 생성해주세요")

                    ID = ""
                    PW = ""
                    
                    # ID 문법 규칙
                    while(True):
                         ID = input("ID : ")
                         r1 = True
                         r2 = True
                         r3 = True
                         if not (len(ID)>=5 and len(ID) <=20):
                              r1 = False
                         if not (re.fullmatch(UserManager.ID_match1, ID) or re.fullmatch(UserManager.ID_match2, ID) or re.fullmatch(UserManager.ID_match3, ID)
                                                        or re.fullmatch(UserManager.ID_match4, ID) or re.fullmatch(UserManager.ID_match5, ID)
                                                        or re.fullmatch(UserManager.ID_match6, ID) or re.fullmatch(UserManager.ID_match7, ID)):
                              r2 = False
                         if not ID[0] not in ['-', '_']:
                              r3 = False

                         # 문법 규칙 틀렸을 경우 안내
                         if not (r1 == True and r2 == True and r3 == True):
                              numbering = 1
                              print("사용할 수 없는 ID입니다. 아래의 사항을 확인해주세요.")
                              if r1 == False:
                                   print(f"{numbering}. 5~20자리로 입력해주세요.")
                                   numbering+=1
                              if r2 == False:
                                   print(f"{numbering}. 영문 소문자 및 숫자, 특수 기호(_),(-)로만 구성해주세요.")
                                   numbering+=1
                              if r3 == False:
                                   print(f"{numbering}. 첫 문자로 특수 기호가 올 수 없습니다")
                              continue
                         # 문법 규칙 맞았을 경우, 의미 규칙 확인
                         else:
                              find_index = -1
                              for index, user_account in enumerate(info):
                                   # ID를 담는 행에서만 검색
                                   if index%4==1:
                                        user_id = user_account.rstrip()
                                        user_id = user_id.split(' ', 1)[0]
                                        # ID가 중복인지 확인
                                        if ID == user_id:
                                             find_index=index
                                             break

                              # ID가 중복일 경우
                              if not find_index == -1:
                                   print("이미 사용중인 ID입니다")
                                   continue
                              # 중복이 아닌 경우
                              else:
                                   break


                    # 비밀번호 문법 규칙
                    while(True):
                         PW = input("비밀번호 : ")
                         r1 = True
                         r2 = True
                         
                         if not (len(PW)>=8 and len(PW) <=20):
                              r1 = False
                         if not (re.fullmatch(UserManager.PW_match1, PW) or re.fullmatch(UserManager.PW_match2, PW)
                                 or re.fullmatch(UserManager.PW_match3, PW) or re.fullmatch(UserManager.PW_match4, PW) or re.fullmatch(UserManager.PW_match5, PW)):
                              r2 = False

                         # 문법 규칙 틀렸을 경우 안내
                         if not (r1 == True and r2 == True):
                              numbering = 1
                              print("사용할 수 없는 비밀번호입니다. 아래의 사항을 확인해주세요.")
                              if r1 == False:
                                   print(f"{numbering}. 8~20자리로 입력해주세요.")
                                   numbering+=1
                              if r2 == False:
                                   print(f"{numbering}. 영문 대문자, 소문자, 숫자, 특수문자 중 3종류 이상의 조합으로 구성해주세요.")
                              continue
                         # 문법 규칙 맞았을 경우, 의미 규칙 확인
                         else:
                              if not len(set(ID) & set(PW)) / len(set(ID) | set(PW)) <= 0.4:
                                   print("ID와 너무 비슷합니다.")
                                   continue
                              else:
                                   break


                    ######## 계정 생성 완료 ########
                    balance = 0
                    while True:
                         try:
                              balance = int(input("계정 생성이 완료되었습니다. 기본 개인 가계부의 시작 잔고를 입력해주세요 : "))
                              if balance < 0:
                                   print("잔고는 0원보다 적을 수 없습니다.")
                                   continue
                              else:
                                   break
                         except:
                              print("유효한 금액(숫자)로 입력해주세요.")
                              continue

                    # 계좌번호 생성 과정
                    account_num_list = []
                    for index, account_num in enumerate(info):
                         # 계좌번호를 담고 있는 행에서만 검색
                         if index%4==2:
                              account_num = account_num.rstrip()
                              account_nums = account_num.split(' ')
                              account_num_list += account_nums

                    # 계좌번호는 6자리 랜덤 숫자
                    new_account_num = random.randint(100000, 999999)
                    # 기존 계좌번호와 중복되지 않게하기
                    while new_account_num in account_num_list:
                         new_account_num = random.randint(100000, 999999)

                    ######## 계좌파일 만들기 + 회원정보파일에 해당 회원 정보/계정/계좌번호 기록 ########
                    f = open(UserManager.user_file, 'a', encoding='UTF-8')
                    f.write(name + "\t" + iden_num + "\n")
                    f.write(ID + " " + PW + "\n")
                    f.write(str(new_account_num) +"\n\n")
                    f.close()
                    
                    f = open(UserManager.account_folder + f"\\{new_account_num}.txt", 'w', encoding='utf-8')
                    f.write(f"1{name}({ID})" +"\n\n")
                    f.write("태그" + "\n\n")
                    now = datetime.datetime.now().strftime('%Y-%m-%d')
                    f.write(f"[계좌 생성] +{balance} {now} {balance}")
                    f.close()
                    return

                         
u=UserManager()
u.signUp()
