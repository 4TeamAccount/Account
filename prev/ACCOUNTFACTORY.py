import os.path
import sys
import random
import datetime

"""
<2021-04-24 15:55 수정>
1. 파일 인코딩 ANSI로 바꾸기
2. 계좌 파일에 회원 기록 구분자 탭으로 바꾸기

<2021-04-24 18:06 수정>
1. 디폴트 태그 반영해서 계좌 파일 생성하기
2. 계좌 선택시 자기 계좌 아니면 접근 못하게 하기
3. 계좌 목록 출력시, 파일이 없는 계좌 발견하면 출력하지 말고 함수 종료하기.

"""

class AccountFactory:
     
     user_file = os.path.expanduser('~') + "\\account-data" + "\\회원관리폴더" + "\\users.txt"
     account_folder = os.path.expanduser('~') + "\\account-data" + "\\계좌폴더"
     ID = ""
     
     # 이 클래스에서 제공하는 기능은 특정 회원(ID)에 맞춰진다.
     def __init__(self, ID):
          self.ID = ID
          
     # 회원관리파일에서 ID를 검색하는 코드가 중복돼서 메소드로 하나 만들었습니다.
     def IDsearch(self):
          info = []
          find_index = -1
          with open(AccountFactory.user_file, 'r', encoding='ANSI') as file:
               info = file.readlines()
               for index, user_account in enumerate(info):
               # ID를 담고있는 행에서만 검색
                    if index%4==1:
                         user_id = user_account.rstrip()
                         user_id = user_id.split(' ', 1)[0]
                         # 이 회원의 ID인지 확인
                         if self.ID == user_id:
                              find_index = index
                              break
          return info, find_index


     # 회원이 사용할 수 있는 계좌를 출력
     def printAccount(self):
          info, find_index = self.IDsearch()
          if not find_index == -1:
               account_list = info[find_index+1][0:-1].split(' ')
               account_print_list = []
               # 이 회원이 사용할 수 있는 계좌들이 실제 파일로 있는지 확인
               for account_num in account_list:
                    account_file = self.account_folder + f"\\{account_num}.txt"
                    # 계좌 파일이 존재할 경우
                    if os.path.isfile(account_file):
                         with open(account_file, mode='r', encoding='ANSI') as f:
                              for line in f:
                                   pass
                              # 각 파일의 잔고만 읽어오기(파일의 마지막 행)
                              account_print_list += [f"{account_num:<15}{line.split(' ')[-1]:<}"]
                    # 계좌 파일이 없을 경우 함수 반환
                    else:
                         print("파일이 존재하지 않는 계좌가 발견되었습니다") 
                         return
                    
               # 여기까지 왔으면 모든 계좌를 출력가능
               print("============계좌 목록 출력============")
               print(f"{'계좌번호':<10} 잔고")
               for account in account_print_list:
                    print(account)


     def createAccount(self):
          balance = 0
          while True:
               try:
                    balance = int(input("생성하려는 가계부의 시작 잔고를 입력해주세요 : "))
                    if balance < 0:
                         print("잔고는 0원보다 적을 수 없습니다.")
                         continue
                    else:
                         break
               except:
                    print("유효한 금액(숫자)로 입력해주세요.")
                    continue

          info, find_index = self.IDsearch()
          
          # 회원 ID를 찾았을 경우
          if not find_index == -1:
               with open(AccountFactory.user_file, 'w', encoding='ANSI') as file:
                    
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
                    
                    # 새 계좌의 계좌 번호 추가
                    info[find_index+1] = info[find_index+1][0:-1] + " " + str(new_account_num) + "\n"
                    file.writelines(info)

                    # 계좌 파일 생성
                    f = open(AccountFactory.account_folder + f"\\{new_account_num}.txt", 'w', encoding='ANSI')
                    name = info[find_index-1].split('\t')[0]
                    f.write(f"1{name}({self.ID})" +"\n\n")
                    f.write("음식(까페/식사/간식) 공부(책/인강/필기구) 수입(알바/용돈) 선물(반지)" + "\n\n")
                    now = datetime.datetime.now().strftime('%Y.%m.%d')
                    
                    f.write(f"[계좌 생성] +{balance} {now} {balance}")
                    f.close()
          else:
               print("ID를 찾지 못했습니다")


     def selectAccount(self):
          select_account = input("선택할 계좌의 계좌번호를 입력해주세요 : ")
          # 선택한 계좌가 회원이 접근가능한 한지를 검사
          info, find_index = self.IDsearch()
          accessible_account_list = info[find_index+1].rstrip().split(' ')
          that_is_my_account = False
          for account in accessible_account_list:
               if select_account == account:
                    that_is_my_account = True
                    break

          # 선택한 계좌가 회원의 계좌 목록에 실제로 있는 경우
          if that_is_my_account == True:                  
               # 선택한 계좌가 실제로 있는지 확인
               account_file = self.account_folder + f"\\{select_account}.txt"
               # 그러한 계좌 파일이 있을 경우
               if os.path.isfile(account_file):
                    # 여기서 계좌 파일 무결성 검사 클래스의 메소드를 호출해야 할 것 같습니다.
                    # 무결성 검사 시 중대오류가 발견되지 않는다면, 회원의 권한에 따라 메뉴를 출력해주는데 그것은 이 클래스의 역할이 아닌 것 같습니다.
                    # 예를들어 무결성 검사 결과를 True/False로 반환하는 식으로 이해했습니다.
                    pass
               else:
                    print("해당 계좌의 파일이 존재하지 않습니다")
                    return
          # 선택한 계좌가 회원의 계좌 목록에 없을 경우
          else:
               print("이용가능한 계좌 목록에 있는 계좌의 번호만 입력해주세요")
               return


     def requestPermission(self):
          request_account = input("권한요청을 할 계좌의 계좌번호를 입력해주세요 : ")
          # 권한 요청할 계좌가 실제로 있는지 확인
          account_file = AccountFactory.account_folder + f"\\{request_account}.txt"
          # 그러한 계좌 파일이 있을 경우
          if os.path.isfile(account_file):
               while True:
                    answer = input("해당 계좌에 권한을 요청할까요?(y/n) : ")
                    if answer == 'y':
                         # 해당 계좌 파일에 권한 요청을 기록
                         with open(account_file, 'r', encoding='ANSI') as file:
                              # 회원 이름도 같이 기록하기 위해 불러오기
                              info, find_index = self.IDsearch()
                              name = info[find_index-1].split('\t')[0]

                              # 계좌의 권한 현황을 불러온다
                              account_data = file.readlines()
                              permission_list = account_data[0].rstrip().split('\t')
                              new_request = f"{name}({self.ID})"

                              # "이름(아이디)"가 동일한 정보가 있다면
                              for permission in permission_list:
                                   if permission[1:] == new_request:
                                        print("이미 권한 요청을 했거나 사용 가능한 계좌입니다.")
                                        return

                              account_data[0] = account_data[0].rstrip() + f"\t4{new_request}\n"
                              
                         with open(account_file, 'w', encoding='ANSI') as file:
                             file.writelines(account_data)
                         return
                    elif answer == 'n':
                         return
                    else:
                         print("응답은 y/n로만 가능합니다")
          else:
               print("해당 계좌 파일이 존재하지 않습니다.")



f = AccountFactory("qhsl1213") # 특정 ID에 대한 AccountFactory 객체를 생성.
f.printAccount()
f.createAccount()
