
import os
import fileinput
import sys
import os.path
import re
import random
import datetime

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
        print("1.로그인")
        print("2.회원가입")
        print("3.종료")
        select_sign=int(input("숫자를 입력하세요:"))
        return select_sign
    def account_manage_menu():
        print("1.계좌선택")
        print("2.계좌생성")
        print("3.권한요청")
        select_account=int(input("숫자를 입력하세요:"))
        return select_account
    
    def manager_menu():
        print("1.수입지출 추가\n2.검색 및 수정\n3.태그편집\n4.권한이동\n5.계좌관리\n6.파일 무결성 체크\n7.종료")
        select_num=int(input("숫자를 입력하세요:"))
        return select_num

    def accout_list():
        print("=======================계좌 목록 출력======================\n계좌번호 \t잔고\n383902 \t500,000,000,000\n123412 \t123,456\n321432 \t3,000")

    def account_function():#주 프롬포트를 의미 합니다.
        #관리자라면 1 아니라면 0
        while True:#각 메뉴가 끝나면 다시 관리자 메뉴 혹은 개인메뉴로 돌아옴
        #계좌의 잔고 검사(파일무결성 검사) 되면1 종료해야하면0
            account_check=1
            if account_check==1:
                #관리자라면 1 아니라면 0
                manager=1
                if manager==1:
                    select_num=CLIController.manager_menu()
                    if select_num==1:
                        print("수입지출추가부입니다.")
                    elif select_num==2:
                        print("검색 및 수정부입니다")
                    elif select_num==3:

                        # f = open('394028.txt', '+r', encoding='UTF-8')
                        # l = f.readlines()
                        account = '394028'
                        CLIController.printAllTag(Account.getAllTag(Account, account))
                        # CLIController.printAllTag(Account.getAllTag(Account, account))
                        # print(len(Account.getAllTag(Account, account)))
                        Account.addTag(Account, Account.getAllTag(Account, account))
                        # print(l)
                    elif select_num==4:
                        print("권한이동부입니다")
                    elif select_num==5:
                        print("계좌관리부입니다")
                        break
                    elif select_num==6:
                        print("파일무결성체크부입니다")
                    elif select_num==7:
                        sys.exit()
                elif manager==0:
                    print("2.검색\n5.계좌관리\n7.종료")
                    select_num=int(input("숫자를 입력하세요:"))
                    if select_num==2:
                        print("검색 및 수정부입니다")
                    elif select_num==5:
                        print("계좌관리부입니다")
                    elif select_num==7:
                        sys.exit()
            else:
                sys.exit()
class FileManager:
    path_home=""
    path_dataFile=""
    user_path=""
    account_path=""
    
    def __init__(self):
        self.path_home=""
        self.path_dataFile=""
        self.user_path=""
        self.account_path=""
    
    
    def executeProgramFileCheck(self):
        try:
            self.path_home=os.path.expanduser('~')
            self.path_dataFile=self.path_home+r"\Account-data"
            self.user_path=self.path_dataFile+r"\User"
            self.account_path=self.path_dataFile+r"\Account"
        except:
            print("!!! 오류: 홈경로를 파악할 수 없습니다! 프로그램을 종료합니다.")
            sys.exit()
       
        if not os.path.exists(self.path_dataFile):
            print("..! 경고: 홈 경로"+self.path_home+"\에 데이터 파일이 없습니다.")
            try:
                os.makedirs(self.path_dataFile)
                self.user_path=self.path_dataFile+r"\User"
                os.makedirs(self.user_path)
                self.account_path=self.path_dataFile+r"\Account"
                os.makedirs(self.account_path)
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

    def getAllTag(self, account_num):

        tagDict = {}
        file_name = account_num + ".txt"
        self.account_file = file_name
        file = open(file_name, 'r')

        for i in range(4):
            file.readline()
            if i == 3:
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

        file_name = account_num + ".txt"
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






























if __name__ == "__main__":
    fileManager=FileManager()
    fileManager.executeProgramFileCheck()
    fileManager.accountBalanceFileCheck(fileManager.account_path+r"\394028.txt")
    fileManager.userAccountFileCheck('qhdksd89')
    # a = Account()
    # CLIController.printAllUser(a.getAllUser('394028'))
    # a.isUser()
    # a.editPermission()
    # a = Account()
    # CLIController.printAllTag(a.getAllTag('394028'))
    # a.addTag(a.getAllTag('394028'))
    # a.deleteTag(a.getAllTag('394028'))
    # a.editTag(a.getAllTag('394028'))
    # while True:
    #     #1.무결성 검사 후 실패시 리턴
    #     select_sign=CLIController.login_menu()
    #
    #     # 기획서상 이 부분의 목업이 따로 존재하지 않고, 로그인 회원가입등의 명령어가 없기 때문에 그냥 메뉴창에서 선택한다고 가정
    #     #일단 목업이 없기에 임의로 출력하겠습니다(로그인)
    #     if select_sign==1:
    #
    #         while True:
    #             input("ID:")
    #             input("PW:")
    #             #로그인에 대한 함수 return 1 -> 아이디와 파일 무결성 검사 통과 0->불통
    #             check=1
    #             if check==1:
    #                 break
    #             else:
    #                 sys.exit()
    #         #계좌목록 함수 *밑은 임의의 출력입니다.
    #         CLIController.accout_list()
    #         #계좌 선택
    #         #인자와의 구분?? manage 메뉴가 필요한가
    #         while True:
    #             select_account=CLIController.account_manage_menu()
    #             if select_account==1:#계좌가 존재하지 않으면 다시 반복
    #                 print("계좌선택함수")#존재하면1 아니면0
    #                 account_exist=1
    #                 if account_exist==1:
    #                     CLIController.account_function()
    #                 #존재하지 않으면 반복문 다시
    #
    #             elif select_account==2:
    #                 print("계좌생성함수")
    #                 #계좌목록 출력 함수 임의의 출력
    #                 print("=======================계좌 목록 출력======================\n계좌번호 \t잔고\n383902 \t500,000,000,000\n123412 \t123,456\n321432 \t3,000")
    #             elif select_account==3:
    #                 #다른계좌본호를 안다고 가정
    #                 print("권한 요청 함수")
    #                 #성공리턴 ->1 실패리턴 ->0
    #                 authority=1
    #                 if authority==1:
    #                     print("권한요청성공")
    #                 elif authority==0:
    #                     print("권한요청실패")
    #     elif select_sign==2:
    #
    #         print("회원가입 완료")
    #         CLIController.account_function()
    #         #계좌선택 클래스
    #     elif select_sign==3:
    #         print("종료")
    #         sys.exit()
    #         break
    #     else:
    #         print("올바른 인자를 입력해주세요")

