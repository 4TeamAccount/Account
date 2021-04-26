
import os
import fileinput
import sys
import os.path
import re
import random
import datetime
from datetime import datetime
import datetime as dt

#tags = dict()
#main_tag = []
#sub_tag = []

class CLIController:
    @staticmethod
    #Account class의 getAllTag()를 통해 가져온 dict를 출력


    def printAllTag(dict):
        print("==========태그목록============")
        m = 1
        s = 1
        for key in dict.keys():
            print(f"{m}  {key}")
            for val in dict[key]:
                print(f"\t{m}.{s}  {val}")
                s += 1
            m += 1
            s = 1
    def printSomeTag(self, m_tag, main_tag, sub_tag):
        print("===================[{}] 하위 태그 목록 출력====================" .format(m_tag))
        #ch = ChangeBuilder(ac_num)
        
        
        m = main_tag.index(m_tag) + 1
        s = 1
        print(f"{m}[{m_tag}]")
        for val in sub_tag[m-1]:
            print(f" ㄴ{m}.{s}  {val}")
            s += 1
        return 'e'

    def printAllUser(list):
        print("=========공용 계좌 사용자 목록=============")
        for user in list:
            if user[0][0] == '1':
                print(user[0][1:] + " 관리자 권한")
            elif user[0][0] == '2':
                print(user[0][1:] + " 수정 및 삭제 권한")
            elif user[0][0] == '3':
                print(user[0][1:] + " 읽기만 가능 권한")
            elif user[0][0] == '4':
                print(user[0][1:])
    def login_menu():
        print("=========로그인 메뉴 출력=============")
        print("1.로그인\t2.회원가입\t3.종료")
        select_sign=input("AccountBook >")
        return select_sign
    def account_manage_menu():
        print("=======================계좌 메뉴 출력==========================")
        print("1.계좌선택\t2.계좌생성\t3.권한요청") 
        select_account=input("AccountNumber >")
        return select_account
    
    def manager_menu():
        c,*t=input("AccountNumber >").split()
        return c,t
    def tag_menu():
        print("..! 원하시는 기능을 입력하세요.(숫자 하나)")
        print("\t1.태그 추가\t2.태그 수정\t3.태그삭제")
        select_num=int(input("AccountNumber >"))
        return select_num
    def printCommend():
        print("=====================================================================================================================")
        print("    명령어군         올바른인자들            설명        ")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("1 add        a  +       한 개 이상      추가 메뉴를 출력합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("2 find       f  /       없거나 여러 개  최근 내역을 출력하거나 인자의 날짜(혹은 구간), 태그로 내역을 검색합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("3 tag        t  [       없음            태그 메뉴를 출력합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("4 permission p  @       없음            권한 메뉴를 출력합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("5 manage     m  >       없음            전체 계좌 목록과 계좌 메뉴를 출력합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("6 verify     f  !       없음             데이터 무결성 확인 및 처리를 진행합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("7 quit       q  .       없음             프로그램을 종료합니다.")
        print("---------------------------------------------------------------------------------------------------------------------")

    def account_function(ID,account_num):
        while True:
            filemanager=FileManager()
            fileManager.accountBalanceFileCheck(os.path.expanduser('~') + "\\Account-data" + "\\Account\\"+str(account_num)+".txt")
            a=Account(account_num,ID)
            userType=a.userTypeCheck(account_num,ID)
            if userType=="1":
                try:
                    select_num,t=CLIController.manager_menu()
                except:
                    CLIController.printCommend()
                    continue
                if select_num == 'add' or select_num =='a' or select_num =='+' or select_num=="1":
                    ch = ChangeBuilder(account_num)
                    ch.tags = a.getAllTag(account_num)
                    ch.main_tag = list(ch.tags.keys())
                    ch.sub_tag = list(ch.tags.values())
                    
                    
                    if t == []:
                        print(".!! 오류: 추가 명령어 뒤에 하나의 [태그]나 태그 위치를 입력해야 합니다.")
                        print("")
                        CLIController.printAllTag(a.getAllTag(account_num))
                    else:
                        tmp = ' '.join(t)
                        tmp = tmp.strip()
                        at = ch.setTag(tmp)
                    
                        if at != 'e':
                            add_res = ch.addChange(account_num, at)
                            if add_res == 'back':
                                pass
                
                elif select_num=="2":
                    print("검색 및 수정부입니다")
                elif select_num=="3" or select_num=='tag' or select_num=='t' or select_num=='[':
                    while True:
                        CLIController.printAllTag(a.getAllTag(account_num))
                        print("..! 원하시는 기능을 입력하세요.(숫자 하나)")
                        print("\t1.태그 추가\t2.태그 수정\t3.태그삭제")
                        select=input("AccountNumber >")
                    
                        if select=="1":
                            a.addTag(a.getAllTag(account_num))
                            break
                        elif select=="2":
                            a.editTag(a.getAllTag(account_num))
                            break
                        elif select=="3":
                            a.deleteTag(a.getAllTag(account_num))
                            break
                        else:
                            print("..! 오류:1~3중의 숫자만 입력해주세요")
                            break

                    
                elif select_num=="4" or select_num=='permission' or select_num=='p' or select_num=='@':
                    if t ==[]:
                        CLIController.printAllUser(a.getAllUser(account_num))
                        a.isUser()
                        a.editPermission()
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                elif select_num=="5" or select_num=='manage' or select_num=='m' or select_num=='>':
                    if t ==[]:
                        break
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                elif select_num=="6" or select_num=='verify' or select_num=='f' or select_num=='!':
                    if t ==[]:
                        pass
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                    
                elif select_num=="7" or select_num=='quit' or select_num=='q' or select_num=='.':
                    if t ==[]:
                        sys.exit()
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                    
                else:
                    CLIController.printCommend()


            elif userType=="2":
                try:
                    select_num,t=CLIController.manager_menu()
                except:
                    CLIController.printCommend()
                    continue
                if select_num == 'add' or select_num =='a' or select_num =='+' or select_num=="1":
                    ch = ChangeBuilder(account_num)
                    ch.self.tags = a.getAllTag(account_num)
                    ch.self.main_tag = list(ch.self.tags.keys())
                    ch.self.sub_tag = list(ch.self.tags.values())
                    if t == []:
                        print(".!! 오류: 추가 명령어 뒤에 하나의 [태그]나 태그 위치를 입력해야 합니다.")
                        print("")
                        CLIController.printAllTag(a.getAllTag(account_num))
                    else:
                        tmp = ' '.join(t)
                        tmp = tmp.strip()
                        
                        at = ch.setTag(tmp)
                        if at != None:
                            add_res = ch.addChange(account_num, at)
                            if add_res == 'back':
                                pass
                elif select_num=="5" or select_num=='manage' or select_num=='m' or select_num=='>':
                    if t ==[]:
                        break
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                elif select_num=="7" or select_num=='quit' or select_num=='q' or select_num=='.':
                    if t ==[]:
                        sys.exit()
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                else:
                    CLIController.printCommend()
                
            elif userType=="3":
                try:
                    select_num,t=CLIController.manager_menu()
                except:
                    CLIController.printCommend()
                    continue
                if select_num==2:
                    print("검색 및 수정부입니다")
                elif select_num=="5" or select_num=='manage' or select_num=='m' or select_num=='>':
                    if t ==[]:
                        break
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                elif select_num=="7" or select_num=='quit' or select_num=='q' or select_num=='.':
                    if t ==[]:
                        sys.exit()
                    else:
                        print(".!! 오류: 인자가 없어야 합니다.")
                else:
                    CLIController.printCommend()
            elif userType=="4":
                print("..! 오류: 아직 계좌에 대한 권한이 없습니다")
                break
            else:
                print("!!! 경고: 사용자 권한에 오류가 있습니다 프로그램을 종료합니다.")
                sys.exit()
class UserManager:

    user_file = os.path.expanduser('~') + "\\Account-data" + "\\User" + "\\users.txt"
    account_folder = os.path.expanduser('~') + "\\Account-data" + "\\Account"

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
                file = open(UserManager.user_file, 'r', encoding = 'ANSI')
                info = file.readlines()
                del info[0] # 추가
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
                    print("로그인 완료")
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
                if not (iden_num[0:2] in map(lambda m: '0'+str(m) if m<10 else str(m), range(0, 100))):
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
            file = open(UserManager.user_file, 'r', encoding = 'ANSI')
            info = file.readlines()
            del info[0]         # 추가
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
                f = open(UserManager.user_file, 'a', encoding='ANSI')
                f.write(name + "\t" + iden_num + "\n")
                f.write(ID + " " + PW + "\n")
                f.write(str(new_account_num) +"\n\n")
                f.close()

                f = open(UserManager.account_folder + f"\\{new_account_num}.txt", 'w', encoding='ANSI')
                f.write("\n") # 추가
                f.write(f"1{name}({ID})" +"\n\n")
                f.write("음식(까페/식사/간식) 공부(책/인강/필기구) 수입(알바/용돈) 선물(반지)" + "\n\n")
                now = datetime.now().strftime('%Y.%m.%d')
                f.write(f"[계좌 생성] +{balance} {now} {balance}")
                f.close()

                return ID,new_account_num
class FileManager:
    path_home=""
    path_dataFile=""
    user_path=""
    account_path=""
    user_txt=""
    def __init__(self):
        try:
            self.path_home=os.path.expanduser('~')
            self.path_dataFile=self.path_home+r"\Account-data"
            self.user_path=self.path_dataFile+r"\User"
            self.account_path=self.path_dataFile+r"\Account"
            self.user_txt=self.user_path+r"\users.txt"
        except:
            print("!!! 오류: 홈경로를 파악할 수 없습니다! 프로그램을 종료합니다.")
            sys.exit()
    
    
    def executeProgramFileCheck(self):
        
       
        if not os.path.exists(self.path_dataFile):
            print("..! 경고: 홈 경로"+self.path_home+"\에 데이터 파일이 없습니다.")
            try:
                os.makedirs(self.path_dataFile)
                self.user_path=self.path_dataFile+r"\User"
                os.makedirs(self.user_path)
                self.account_path=self.path_dataFile+r"\Account"
                os.makedirs(self.account_path)
                with open(self.user_txt,'w',encoding='ANSI') as file:
                    file.write('\n')
                    pass
                print("... 홈 경로에 빈 데이터 파일을 새로 생성했습니다:")
                print(self.path_dataFile)
            except:
                print("!!! 오류: 홈 경로에 데이터 파일을 생성하지 못했습니다! 프로그램을 종료합니다.")
                sys.exit()
        else:
            if not FileManager.fileAccess(self.path_dataFile) or not FileManager.fileAccess(self.user_path) or not FileManager.fileAccess(self.account_path) :
                print(self.path_dataFile+"에 대한 입출력 권한이 없습니다! 프로그램을 종료합니다.")
                sys.exit()
               
    def fileAccess(fpath): # 권한을 알아보는 함수 정의
        check=True

        if not os.access(fpath,os.R_OK):
            check=False
        if not os.access(fpath,os.W_OK):
            check=False
        if not os.access(fpath,os.X_OK):
            check=False
        
        return check
               
    def userAccountFileCheck(self,ID):
        accountFactory=AccountFactory(ID)
        info = []
        find_index = -1
        with open(AccountFactory.user_file, 'r', encoding='ANSI') as file:
            strList=file.readlines()
            del strList[0]
            index=-1
            check=0
            user_check=0
            for txt in strList:
                index+=1
                if index%4==1:
                    user_id = txt.rstrip()
                    user_id = user_id.split(' ', 1)[0]
                    if user_id==ID:
                        string =strList[index+1]
                        user_check=1
                        if string=="\n":
                            print("!!! 경고: 사용자의 계좌가 하나도 존재하지 않습니다.")
                            check=1
                            break
        if user_check==0:
            print("... 사용자가 존재하지 않습니다")           
        if check==1:
            print("... 사용자의 개인 계좌를 생성하였습니다:")
            accountFactory.createAccountAsFileCheck(strList,index)
        
            
                   
        
    def balanceCheck(self,file_name):
        file=open(file_name,'r')
        check=1
        string=None
        while string != '':
            string=file.readline()
            list=string.split(" ")
            balance=list[len(list)-1]
            if not balance.find("-")==-1:
                check=0
                break
        file.close()
        return check
    
    def accountBalanceFileCheck(self,file_name):
        if self.balanceCheck(file_name)==0:
            print("..! 경고: 데이터 파일에 잔고에 이상이 있습니다!")
            temp=""
            
            with fileinput.FileInput(file_name,inplace=True,backup='.bak') as f:
                for line in f:
                    if line.find('[')!=-1:
                        list=line.split(" ")
                        balance=list[len(list)-1]
                        money=""
                        for word in list:
                            if word[0]=='+' or word[0]=='-':
                                money=word
                                break
                        consume=0
                        if money[0]=='+':
                            consume=int(money)
                        elif money[0]=='-':
                            consume=int(money)
                        changeBalance=balance.replace("\n","")
                        if not temp=="":
                            line=line.replace(changeBalance,str(int(temp)+consume))
                        print(line,end="")
                        if not temp=="":
                            temp=str(int(temp)+consume)
                        else:
                            temp=balance
                    else:
                        print(line,end="")
            if(self.balanceCheck(file_name)==0):
                print('!!! 오류: 데이터 파일에 이상이 생겨 프로그램을 종료합니다.')
            else:
                print('… 잔고를 새로 고침 하였습니다:')


class Account:
    #파일에서 5번째 줄 읽어와 Dict 구조로 태그 목록 return
    account_file = ""
    user = ""
    account_num=""
    ID=""
    account_folder = os.path.expanduser('~') + "\\Account-data" + "\\Account"
    def __init__(self):
        pass

    def __init__(self,account_num,ID):
        self.account_num=account_num
        self.ID=ID


    def userTypeCheck(self,account_num,ID):
        file_name = self.account_folder + "\\" + str(account_num) + ".txt"
        self.account_file = file_name
        file = open(file_name, 'r')
        string=file.readlines()

        userline=string[1]
        userList=userline.split("\t")
        file.close()
        for user in userList:
            if user.split("(")[1].replace(")","").replace("\n","")==ID:
                return user[0]
                break
        
        print("!!! 유저를 찾을 수 없습니다.")

    def getAllTag(self, account_num):

        tagDict = {}
        file_name = self.account_folder + "\\" + account_num + ".txt"
        self.account_file = file_name
        file = open(file_name, 'r')

        for i in range(3):
            file.readline()
            if i == 2:
                l = file.readline()
        file.close()
        sl = l.split(" ")
        for s in sl:
            temp = []
            tags = s.replace("(", " ").replace(")", "").replace("/", " ").replace("\n", "").split(" ")
            for i in range(1, len(tags)):
                if tags[i] != '':
                    temp.append(tags[i])
            tagDict[tags[0]] = temp
        return tagDict

    def addTag(self, dict):
        print("태그를 추가할 위치와 태그 이름을 입력하세요")
        tag_num, tag_name = input().replace(']', '').split('[')
        print(tag_num, tag_name)
        child_num = 0
        if '.' in tag_num:
            super_num, child_num = map(int, tag_num.split('.'))
        else:
            super_num = int(tag_num)
            if super_num <= len(dict):
                print(".!!오류 : 해당 위치에 태그가 이미 존재 합니다.")
                self.addTag(dict)
                return 0
        temp = 1
        for key in dict.keys():
            if dict[key] == ['']:
                dict[key] = []
            if temp == super_num:
                if len(dict[key]) >= child_num:
                    print(child_num, len(dict[key]), dict[key])
                    print(".!!오류 : 해당 위치에 태그가 이미 존재 합니다.")
                    self.addTag(dict)
                    return 0
            if tag_name == key:
                print(".!!오류 : 해당 이름의 태그가 이미 존재 합니다.")
                self.addTag(dict)
                return 0

            for val in dict[key]:
                if tag_name == val:
                    print(".!!오류 : 해당 이름의 태그가 이미 존재 합니다.")
                    self.addTag(dict)
                    return 0
            temp += 1
        if ' ' in tag_name or '\t' in tag_name:
            print(".!!오류 : 태그 이름에는 탭이나 개행 문자가 포함될 수 없습니다.")
            self.addTag(dict)
            return 0
        # 특수 문자와 숫자로만 이루어 졌을때랑 길이 넘을때 오류 넣어야함
        print(super_num, child_num)
        if child_num != 0:
            temp = 0
            for key in dict.keys():
                temp += 1
                if temp == super_num:
                    dict[key].append(tag_name)
                    break
        else:
            dict[tag_name] = []
        print(dict)
        new_tag = ""

        for key in dict.keys():
            new_tag += key + '('
            temp = 1
            if len(dict[key]) == 0:
                new_tag += ')'
            for val in dict[key]:
                if temp == len(dict[key]):
                    new_tag += val + ')'
                else:
                    new_tag += val + '/'
                temp += 1
            new_tag += " "
        new_tag = new_tag[:-1]
        new_tag += '\n'
        for line in fileinput.input(self.account_file, inplace=True):
            if '(' in line and '/' in line and ')' in line:
                line = line.replace(line, new_tag)
            sys.stdout.write(line)
        print(new_tag)

    def editTag(self, dict):
        print("태그를 수정 할 위치와 태그 이름을 입력하세요")
        tag_num, tag_name = input().replace(']', '').split('[')
        child_num = 0
        if '.' in tag_num:
            super_num, child_num = map(int, tag_num.split('.'))
        else:
            super_num = int(tag_num)
            if super_num > len(dict):
                print(".!!오류 : 해당 위치에 태그가 존재하지 않습니다.")
                self.editTag(dict)
                return 0
        temp = 1
        for key in dict.keys():
            if dict[key] == ['']:
                dict[key] = []
            if temp == super_num:
                if len(dict[key]) < child_num:
                    print(child_num, len(dict[key]), dict[key])
                    print(".!!오류 : 해당 위치에 태그가 존재하지 않습니다.")
                    self.editTag(dict)
                    return 0
            if tag_name == key:
                print(".!!오류 : 해당 이름의 태그가 이미 존재 합니다.")
                self.editTag(dict)
                return 0
                break
            for val in dict[key]:
                if tag_name == val:
                    print(".!!오류 : 해당 이름의 태그가 이미 존재 합니다.")
                    self.editTag(dict)
                    return 0
                    break
            temp += 1
        if ' ' in tag_name or '\t' in tag_name:
            print(".!!오류 : 태그 이름에는 탭이나 개행 문자가 포함될 수 없습니다.")
            self.editTag(dict)
            return 0
        # 특수 문자와 숫자로만 이루어 졌을때랑 길이 넘을때 오류 넣어야함
        if child_num != 0:
            dict[list(dict.keys())[super_num-1]][child_num-1] = tag_name
            new_dict = dict.copy()
        else:
            new_dict = {}
            new_keys = list(dict.keys())
            new_keys[super_num-1] = tag_name
            temp = 0
            for keys in new_keys:
                new_dict[keys] = dict[list(dict.keys())[temp]]
                temp += 1
        print(new_dict)
        new_tag = ""

        for key in new_dict.keys():
            new_tag += key + '('
            temp = 1
            if len(new_dict[key]) == 0:
                new_tag += ')'
            for val in new_dict[key]:
                if temp == len(new_dict[key]):
                    new_tag += val + ')'
                else:
                    new_tag += val + '/'
                temp += 1
            new_tag += " "
        new_tag = new_tag[:-1]
        new_tag += '\n'
        for line in fileinput.input(self.account_file, inplace=True):
            if '(' in line and '/' in line and ')' in line:
                line = line.replace(line, new_tag)
            sys.stdout.write(line)
        print(new_tag)

    def deleteTag(self, dict):
        print(dict)
        print("삭제할 태그 위치를 입력하세요")
        tag_num = input()
        for c in tag_num:
            if ord(c) < 48 and ord(c) >57 and ord(c) != 46:
                print(".!!오류 : 태그 위치에는 숫자와 . 만 입력 가능합니다.")
                self.deleteTag(dict)
                return 0

        if tag_num.count('.') > 1:
            print(".!!오류 : 태그 위치에는 숫자와 하나의 . 만 입력 가능합니다.")
            self.deleteTag(dict)
            return 0

        child_num = 0
        if '.' in tag_num:
            super_num, child_num = map(int, tag_num.split('.'))
        else:
            super_num = int(tag_num)
            if super_num > len(dict):
                print(".!!오류 : 해당 위치에 태그가 존재하지 않습니다.")
                self.deleteTag(dict)
                return 0
        #하위태그는 입력 안했을때
        if child_num == 0:
            #삭제하려는 태그의 하위태그가 존재할때
            print(super_num, child_num)
            if len(dict[list(dict.keys())[super_num-1]]) != 0:
                print(".!!오류 : 해당 위치에 태그에 하위 태그들이 존재하면 삭제 할 수 없습니다.")
                self.deleteTag(dict)
                return 0
            else:
                del dict[list(dict.keys())[super_num-1]]
        #하위태그 삭제할때
        else:
            if child_num > len(dict[list(dict.keys())[super_num-1]]):
                print(".!!오류 : 해당 위치에 태그가 존재하지 않습니다.")
                self.deleteTag(dict)
                return 0
            else:
                del dict[list(dict.keys())[super_num-1]][child_num-1]

        new_tag = ""

        for key in dict.keys():
            new_tag += key + '('
            temp = 1
            if len(dict[key]) == 0:
                new_tag += ')'
            for val in dict[key]:
                if temp == len(dict[key]):
                    new_tag += val + ')'
                else:
                    new_tag += val + '/'
                temp += 1
            new_tag += " "
        new_tag = new_tag[:-1]
        new_tag += '\n'
        for line in fileinput.input(self.account_file, inplace=True):
            if '(' in line and '/' in line and ')' in line:
                line = line.replace(line, new_tag)
            sys.stdout.write(line)
        print("...태그 삭제가 완료되었습니다.")
        print(new_tag)

    def getAllUser(self, account_num):

        file_name = self.account_folder + "\\" + account_num + ".txt"
        self.account_file = file_name
        file = open(file_name, 'r')
        file.readline()
        l = file.readline()[:-1]
        file.close()
        userList = l.split('\t') #이거 탭으로 바꿔야
        userIdList = list(map(lambda x: x[:-1].split('('), userList))
        print(userIdList)
        return userIdList
    #목록에 입력한 사용자가 있으면 True 없으면 False
    def isUser(self):
        user = input("사용자 이름>")
        account_num = self.account_file[0:-4]
        userList = self.getAllUser(account_num)
        userList = list(map(lambda x: x[0][1:], userList))
        result = user in userList
        if result:
            self.user = user
        return result

    def editPermission(self):
        file = open(self.account_file, 'r')
        file.readline()
        l = file.readline()[:-1]
        file.close()
        permission = input("권한 입력 >")
        account_num = self.account_file[0:-4]
        userList = self.getAllUser(account_num)
        perm_string = ""
        if permission == '1':
            perm_string = "관리자"
        elif permission == '2':
            perm_string = "수정 및 삭제"
        elif permission == '3':
            perm_string = "읽기만 가능"

        if '.' in permission or '-' in permission:
            print(".!! 오류: 소수점이 존재하지 않는 양의 정수여야 합니다.")
            self.editPermission()
            return
        if permission > '4' or permission < '1':
            print(".!! 오류: 권한 메뉴 번호가 아닙니다.")
        if permission + self.user in l:
            print(".!! 오류 : 기존 권한과 동일합니다.")
            self.editPermission()
            return
        else:
            for i, u in enumerate(userList):
                if self.user in u[0]:
                    userList[i][0] = permission + self.user
                    temp = userList.pop(i)
                    userList.append(temp)
                    break
        new_line = ""
        for li in userList:
            new_line += li[0] + '(' + li[1] + ')' + '\t'
        new_line = new_line[:-1] + '\n'


        print("... 현재까지 입력한 내역입니다.")
        print(f"=> 사용자 이름 : {self.user}")
        print(f"=> 변경 권한 : {perm_string}")

        re = input("정말 저장하시겠습니까?>(.../No)")
        if re == 'No' or re == 'N' or re == 'n' or re == 'no':
            return
        else:
            line_count = 0
            for line in fileinput.input(self.account_file, inplace=True):
                if line_count == 1:
                    line = line.replace(line, new_line)
                line_count += 1
                sys.stdout.write(line)
class AccountFactory:

    user_file = os.path.expanduser('~') + "\\Account-data" + "\\User" + "\\users.txt"
    account_folder = os.path.expanduser('~') + "\\Account-data" + "\\Account"
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
            del info[0] # 추가
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
                              line=int(line.split(' ')[-1])
                              account_print_list += [f"{account_num:<15}{format(line,',d'):<}"]
                    # 계좌 파일이 없을 경우 함수 반환
                    else:
                         print("파일이 존재하지 않는 계좌가 발견되었습니다") 
                         return

               # 여기까지 왔으면 모든 계좌를 출력가능
               print("============계좌 목록 출력============")
               print(f"{'계좌번호':<10} 잔고")
               for account in account_print_list:
                    print(account)

    def createAccountAsFileCheck(self,info,find_index):
        balance = 0
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
                info[find_index+1] = info[find_index+1][0:-1] + str(new_account_num) + "\n"
                info.insert(0, '\n') # 추가
                file.writelines(info)
                del info[0] # 추가

                # 계좌 파일 생성
                f = open(AccountFactory.account_folder + f"\\{new_account_num}.txt", 'w', encoding='ANSI')
                name = info[find_index-1].split('\t')[0]
                f.write("\n") # 추가
                f.write(f"1{name}({self.ID})" +"\n\n")
                f.write("음식(까페/식사/간식) 공부(책/인강/필기구) 수입(알바/용돈) 선물(반지)" + "\n\n")
                now = datetime.now().strftime('%Y.%m.%d')

                f.write(f"[계좌 생성] +{balance} {now} {balance}")
                f.close()
        else:
            print("!!! 오류:계좌 생성에 실패하였습니다. 프로그램을 종료합니다.")
            sys.exit()

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
                info.insert(0, '\n') # 추가
                file.writelines(info)
                del info[0] # 추가

                # 계좌 파일 생성
                f = open(AccountFactory.account_folder + f"\\{new_account_num}.txt", 'w', encoding='ANSI')
                name = info[find_index-1].split('\t')[0]
                f.write("\n") # 추가
                f.write(f"1{name}({self.ID})" +"\n\n")
                f.write("음식(까페/식사/간식) 공부(책/인강/필기구) 수입(알바/용돈) 선물(반지)" + "\n\n")
                now = datetime.now().strftime('%Y.%m.%d')

                f.write(f"[계좌 생성] +{balance} {now} {balance}")
                f.close()
        else:
            print("ID를 찾지 못했습니다")


    def selectAccount(self):
        self.printAccount()
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
                return select_account
            else:
                print("해당 계좌의 파일이 존재하지 않습니다")
                return False
        # 선택한 계좌가 회원의 계좌 목록에 없을 경우
        else:
            print("이용가능한 계좌 목록에 있는 계좌의 번호만 입력해주세요")
            return False


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
                        permission_list = account_data[1].rstrip().split('\t') # 추가
                        new_request = f"{name}({self.ID})"

                        # "이름(아이디)"가 동일한 정보가 있다면
                        for permission in permission_list:
                            if permission[1:] == new_request:
                                print("이미 권한 요청을 했거나 사용 가능한 계좌입니다.")
                                return

                        account_data[1] = account_data[1].rstrip() + f"\t4{new_request}\n" # 추가

                        # 회원관리파일에 방금 권한 요청한 계좌번호 기록
                        info, find_index = self.IDsearch()
                        with open(self.user_file, 'w', encoding='ANSI') as file:
                            info[find_index+1] = info[find_index+1][0:-1] + " " + request_account + "\n"
                            info.insert(0, '\n') # 추가
                            file.writelines(info)
                                 
                    with open(account_file, 'w', encoding='ANSI') as file:
                        file.writelines(account_data)                           
                        return
                elif answer == 'n':
                    return
                else:
                    print("응답은 y/n로만 가능합니다")
        else:
            print("해당 계좌 파일이 존재하지 않습니다.")

user_file = os.path.expanduser('~') + "\\Account-data" + "\\User" + "\\users.txt"
account_folder = os.path.expanduser('~') + "\\Account-data" + "\\Account"


#tags = dict()
#main_tag = []
#sub_tag = []
class ChangeBuilder:
    
    
    
    account_folder = os.path.expanduser('~') + "\\Account-data" + "\\Account"
    
    input_tag = ''
    input_money = ''
    input_date = ''
    total = ''
    new_total = ''
    ac_num = ''
    change_content = []
    
    
    def __init__(self,account_num):
        self.ac_num=account_num
        self.tags = dict()
        self.main_tag = []
        self.sub_tag = []
        self.flag = True

    
    def setTag(self, tag): #tag가 [태그] or x.x로 들어옴
        #비정상 결과: 인자가 없는 경우 -> main에서 처리
        ac=Account(self.ac_num,"")
        cli = CLIController()
        t = tag
        #print(f"값{t} 형태{type(t)}")
        main_tag = self.main_tag
        sub_tag = self.sub_tag
        
        
        if t[-1] == '.':
            print(".!! 오류: 태그 위치는 <숫자>.<숫자>로만 입력 가능합니다.")
            return 'e'
        
        
        if t[0].isdigit(): #입력이 숫자인지 판단: 숫자로 시작되는 경우 무조건 태그 위치 입력으로 봄
            t = t.replace(' ', '')
            
            if any(x.isalpha() for x in t): #숫자와 문자 혼합
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag(self.ac_num))
                return 'e'
            
            if t.count('.') >= 2:
                print(".!! 오류: 태그 위치는 <숫자>.<숫자>로만 입력 가능합니다.")
                return 'e'
            #elif not '.' in t and not 1 <= int(t) <= len(main_tag):
             #   print(".!! 오류: 태그 위치는 <숫자>.<숫자>로만 입력 가능합니다.")
              #  return
        
            
            if 1 <= float(t) < len(main_tag) + 0.1*len(sub_tag[-1]): #태그 목록 숫자 사이에 존재
                if not '.' in t: #상위 태그
                    print("..! 상위태그입니다. 하위 태그를 입력해주세요")
                    m_tag = main_tag[int(t)-1]
                    cli.printSomeTag(m_tag, self.main_tag, self.sub_tag)
                    return 'e'
                else:
                    
                    i = list(map(int,t.split('.')))
                    if i[1] <= len(sub_tag[i[0]-1]):
                        #input_tag = t #정상 결과: 하위 숫자
                        #print("정상 입력 숫자: {}" .format(t)) #확인용! 나중에 지우기
                        return i

                    else:
                        print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                        cli.printAllTag(ac.getAllTag(self.ac_num))
                        return 'e'
            else:
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag(self.ac_num))
                return 'e'
                
        else: #입력이 문자
            if t.count('[') >= 2:
                print(".!! 오류: 추가 명령어 뒤에 하나의 [태그]를 입력해야 합니다.")
                return
            elif t.count('[') == 0 or t.count(']') == 0:
                print(".!! 오류: 태그를 '[', ']'로 감싸야 합니다.")
                return 'e'
            
            tmp = t[1:-1].strip()
        
            
            if any(x == '\n' or x == '\t' for x in t): 
                print(".!! 오류: 태그는 탭과 개행 문자의 포함을 허용하지 않습니다.")
                return 'e'
            
            t = ' '.join(tmp.split())
            
            if t in main_tag: #[상위태그]
                print("..! 상위태그입니다. 하위 태그를 입력해주세요")
                cli.printSomeTag(t, self.main_tag, self.sub_tag)
                return 'e'
            elif not t in sum(sub_tag, []):
                print("..! 존재하지 않는 태그입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag(self.ac_num))
                return 'e'
            else:
                #print("정상 입력 태그: {}" .format(t)) #확인용 지우기
                return t
            

    def search(self, srh_date, *srh_money):
        
        if '원' in srh_money[0][-1]:
            srh_m = srh_money[0][:-1]
        else:
            srh_m = srh_money[0]
        
        self.input_money = srh_m
        srh_d = srh_date
        
        print()
    
        
        i = 0
    
        file_name = self.account_folder+"\\"+self.ac_num + ".txt"
        self.account_file = file_name
        f_s = open(file_name, 'r')
        lines = f_s.readlines()
        
        #print("파일 내용 출력", lines)
        f_s.close()
        
        
        days = [] #내역에서 날짜만 뽑은거
        for l in lines[5:]:
            p = l.split(' ')[-1]
            days.append(p)
        
        i = 4
        change_content = lines[int(i):]
        tmp = list(map(lambda x: x.rstrip(), change_content))
    
        current = list(map(lambda x: x.split(' ')[-1], tmp)) #합계만 자른거
        tmp2 = list(map(lambda x: x[:-1].split(' ')[:-1], tmp)) 
        tmp = list(map(lambda x: ' '.join(x), tmp2)) #합계 전까지만 자른거
      
        for index, t in enumerate(days):
            
            if srh_d < t:
                c_tmp = list(int(x) + int(srh_m) for x in current[index:])
                self.new_total = c_tmp[-1] + int(srh_m)
                
                if any(c < 0 for c in c_tmp): #이후 내역이 입력 금액 때문에 음수가 되는 상황
                    self.new_total = ''
                    return 'e'
                else:
                    res = list(map(lambda x, y: x+' '+str(y), tmp[index:], c_tmp))
                    self.change_content = res
                    return index+4
                
        calc = int(self.total) + int(srh_m)
        if  calc < 0:
            return 'e'
        else:
            self.new_total = calc
            return len(tmp)+4
        

    def setMoney(self, money, *date):
        mo = money
        da = ''
    
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        head = ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        mids = [',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        tail  = ['원', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        if len(mo) == 1 and not mo[0] in digits:
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("문자열 길이가 1이라면 그 문자는 무조건 숫자여야 함") #목업 따로 없어서 추가했습니다.
            #print("금액은 ‘,’, ‘원’, 숫자로만 써주세요.")
            return 'e'
        elif len(mo) == 1:
            return mo
        
        if not mo[0] in head: #숫자 맨 앞은 숫자랑 + -로만 가능"
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("금액은 ‘,’, ‘원’, 숫자로만 써주세요.")
            return 'e'
        
        for k in mo[1:-1]:
            flag = False
            for mid in mids:
                if mid in k:
                    flag = True
                
            if flag == False:
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print("금액은 ‘,’, ‘원’, 숫자로만 써주세요.")
                return 'e'
    
        if not mo[-1] in tail: #숫자 끝은 원이랑 숫자만 가능
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("금액은 ‘,’, ‘원’, 숫자로만 써주세요.")
            return 'e'
        
        
    def setDate(self, date):
        d = date
        num = re.findall("\d+", d)
    
        
        if '.' in d and (d.count('-') != 0 or d.count('/')):
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("날짜는 ‘-’, ‘/’, ‘.’를 하나 이하 포함하며 숫자로만 써주세요.") #이게 조금 더 명확한 것 같음?
            return 'e'
        
        elif '-' in d and (d.count('.') != 0 or d.count('/')):
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("날짜는 ‘-’, ‘/’, ‘.’를 하나 이하 포함하며 숫자로만 써주세요.")
            return 'e'
        elif '/' in d and (d.count('.') != 0 or d.count('-')):
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("날짜는 ‘-’, ‘/’, ‘.’를 하나 이하 포함하며 숫자로만 써주세요.")
            return 'e'
            
        #print(f"기존 숫자 {d} 변환 숫자{num}")
        if len(num) == 1:#20210102 경우
            num = "".join(num)
            if len(num) != 8:
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print(".!! 오류: 월과 일은 2자리로 입력해야 합니다.")
                return 'e'
            else:
                tmp = [num[:4], num[4:6], num[6:]]
                #res = num[:4] + '.' + num[4:6] + '.' + num[6:]
                num = tmp
                
        elif len(num) == 3:
            if len(num[0]) != 4:
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print(".!! 오류: 연도는 4자리로 입력해야 합니다.")
                return 'e'
            
            if any(map(lambda x: len(x) != 2, num[1:])):
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print(".!! 오류: 월과 일은 2자리로 입력해야 합니다.")
                return 'e'
        else:
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print(".!! 오류: 연도는 4자리, 월과 일은 2자리로 입력해야 합니다.")
            return 'e'
        
        num = list(map(int, num))
        check = ['-', '/', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        #print(num)
        
        
        for k in d:
            flag = False
            for ch in check:
                if ch in k:
                    flag = True
            if flag == False:
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print("날짜는 ‘-’, ‘/’, ‘.’, 숫자로만 써주세요.")
                return 'e'
        
        today = datetime.today()
        if 1970 > num[0] or num[0] > 2037:
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print(".!! 오류: 연도가 1970년 이후부터 2037년 이전까지여야 합니다.")
            return 'e'
        
        try: 
            day = datetime(num[0], num[1], num[2])
            if day > today:
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print(".!! 오류: 미래의 내역은 작성할 수 없습니다.")
                return 'e'
        except:
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print(".!! 오류: 해당 날짜가 현행 그레고리력에 존재하는 날짜여야 합니다.")
            return 'e'
        
        
        res = day.strftime("%Y.%m.%d")
        self.input_date = res
        return res
            

    def build(self, account_num, save_tag, i):
       
        
        money = self.input_money
        
        print(money)
        
        if '+' not in money and '-' not in money:
            money = '+' + money
            self.input_money = money
        
        save_date = self.input_date
        save_total = self.new_total
        
        #print("저장할 날짜 형태 보장", save_date)
        saved_data = f"{save_tag} {money} {save_date} {save_total}"
        
        if self.flag == True:
            print(f"입력 내용: {save_tag} {money[1:]}원 {save_date}") 
        else:
            print(f"입력 내용: {save_tag} {money[1:]}원 {save_date} (오늘)")
            self.flag = True
        
        save_check = input("AccountNumber> 정말 저장하시겠습니까? (.../No) >")
        
        if save_check == "No":
            return 'back'
        else:
            self.input_tag = save_tag
            
            file_name = self.account_folder + "\\"+self.ac_num+ ".txt" #파일 확정되지 않아 이름 한줄로 바꿔 해보았습니다.
            #file_name = account_num + ".txt"
            self.account_file = file_name
            f = open(file_name, 'r+')
            lines = f.readlines()
            line = lines[:i]
            print(line)
            
            cc = self.change_content
            cc.append(saved_data)
            cc = list(map(lambda x: x+'\n', cc))
            
            res = line + cc
            
            f.seek(0)
            f.writelines(res)
            f.truncate()
            f.close()
            
            self.input_tag = ''
            self.input_money = ''
            self.input_date = ''
            return 
            

    def addChange(self, account_num, atag):
        t = ''
        m = ''
        d = ''
        
        self.ac_num = account_num
        main_tag = self.main_tag
        
        file_name = self.account_folder +"\\"+ account_num + ".txt"
        self.account_file = file_name
        f = open(file_name, 'r')
        lines = f.readlines()
        self.total = lines[-1].split(' ')[-1]
        
        at = atag
        f.close()
    
        
        if type(atag) == list:
                try:
                    m, *d = map(str, input("AccountNumber > [{0}][{1}] 내역> " .format(self.main_tag[at[0]-1], self.sub_tag[at[0]-1][at[1]-1])).split(" "))
                    t = f"[{self.main_tag[at[0]-1]}][{self.sub_tag[at[0]-1][at[1]-1]}]"
                    
                except ValueError:
                    print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                    print(".!! 오류: 금액은 길이가 1 이상이어야 합니다.")
                    self.addChange(account_num, atag)
        elif type(atag) == str:
            main_key = ''
            for key, value in self.tags.items():
                if at in value:
                    main_key = key
                    break
            try:    
                m, *d = map(str, input("AccountNumber > [{0}][{1}] 내역> " .format(main_key, at)).split( ))
                t = f"[{main_key}][{at}]"
                
            except ValueError:
                    print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                    print(".!! 오류: 금액은 길이가 1 이상이어야 합니다.")
                    self.addChange(account_num, atag)
        
        if len(d) >= 2:
            print(".!! 오류: 인자가 너무 많습니다. 날짜와 금액은 공백을 허용하지 않습니다.")
            self.addChange(account_num, atag)
        else:
            #print("d형태", d[0])
            m_res = self.setMoney(m)
            
            if m_res == 'e':
                if d != [] and not(len(d[0]) == 8 or len(d[0]) == 10):
                    print("날짜는 ‘-’, ‘/’, ‘.’, 숫자로만 써주세요.")
                    self.addChange(account_num, atag)
                    return 'e'
                else:
                    self.addChange(account_num, atag)
                    return 'e'
                
              
                self.addChange(account_num, atag)
                
            else:
                if d != []: #날짜 입력된 경우
                    da = d[0]
                    
                    res_d = self.setDate(da)
                    
                    if res_d != 'e': #숫자 입력 규칙 만족 후 잔고 비교
                
                        s = self.search(res_d, m)
                        if  s != 'e':
                            
                            self.input_date = res_d
                        else:
                            print("입력한 금액이 사용자의 잔고에 있는 금액보다 큽니다.")
                            self.addChange(account_num, atag)
                            #return 'e'
                    else:
                        self.addChange(account_num, atag)
                        #return 'e'
                else: #날짜 입력 안된 경우 잔고 비교
                    res_d = datetime.today().strftime("%Y.%m.%d")
                    self.flag = False
                    self.input_date = res_d
                    s = self.search(res_d, m)
                    if s == 'e':
                        print("입력한 금액이 사용자의 잔고에 있는 금액보다 큽니다.")
                        self.addChange(account_num, atag)
                        #return s
                    #else:
                     #   print("입력한 금액이 사용자의 잔고에 있는 금액보다 큽니다.")
                      #  return 'e'
                
                
                save_res = self.build(account_num, t, m_res)
                if save_res == 'back':
                    
                    return 'back'
            
            
        #print("입력/지출 부분")
        





























if __name__ == "__main__":
    # fileManager=FileManager()
    # fileManager.executeProgramFileCheck()
    # fileManager.accountBalanceFileCheck(fileManager.account_path+r"\394028.txt")
    # fileManager.userAccountFileCheck('qhdksd89')
    # a = Account()
    # CLIController.printAllUser(a.getAllUser('394028'))
    # a.isUser()
    # a.editPermission()
    # a = Account('776401','qhdksd89')
    # CLIController.printAllTag(a.getAllTag('776401'))
    # a.addTag(a.getAllTag('394028'))
    # a.deleteTag(a.getAllTag('394028'))
    # a.editTag(a.getAllTag('394028'))
    while True:
        fileManager=FileManager()
        userManager=UserManager()
        fileManager.executeProgramFileCheck()
        try:
            select_sign=CLIController.login_menu()
        except:
            print("..! 오류: 인자는 1~3사이의 숫자 하나여야 합니다")
            continue
        account_num=""
        ID=""
        if select_sign=="1":
            ID=userManager.login()
            fileManager.userAccountFileCheck(ID)
            accountFactory=AccountFactory(ID)
            
            commandCheck=0
            while True:
                accountFactory.printAccount()
                try:
                    select_account=CLIController.account_manage_menu()
                except:
                    print("..! 오류: 인자는 1~3사이의 숫자 하나여야 합니다")
                    continue
                if select_account=="1":
                    account_num=accountFactory.selectAccount()
                    if account_num!=False:
                        CLIController.account_function(ID,account_num)
                elif select_account=="2":
                    accountFactory.createAccount()
                    
                elif select_account=="3":
                    accountFactory.requestPermission()
                else:
                    print("..! 오류: 인자는 1~3사이의 숫자 하나여야 합니다")

            
        elif select_sign=="2":
            ID,account_num=userManager.signUp()
            first_check=0
            while True:
                if first_check==0:
                    CLIController.account_function(ID,str(account_num))
                    first_check=1
                else:
                    accountFactory.printAccount()
                    try:
                        select_account=CLIController.account_manage_menu()
                    except:
                        print("..! 오류: 인자는 1~3사이의 숫자 하나여야 합니다")
                        continue
                    if select_account=="1":
                        account_num=accountFactory.selectAccount()
                        if account_num!=False:
                            CLIController.account_function(ID,account_num)
                    elif select_account=="2":
                        accountFactory.createAccount()
                    elif select_account=="3":
                        accountFactory.requestPermission()
                    else:
                        print("..! 오류: 인자는 1~3사이의 숫자 하나여야 합니다")
            
        elif select_sign=="3":
            sys.exit()
            break
        else:
            print("..! 오류: 인자는 1~3사이의 숫자 하나여야 합니다")

