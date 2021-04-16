

import fileinput
import sys

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



class Account:
    #파일에서 5번째 줄 읽어와 Dict 구조로 태그 목록 return
    def getAllTag(self, account_num):
        tagDict = {}
        file_name = account_num + ".txt"
        file = open(file_name, 'r', encoding='UTF-8')

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
                self.addTag(self, dict)
        temp = 1
        for key in dict.keys():
            if dict[key] == ['']:
                dict[key] = []
            if temp == super_num:
                if len(dict[key]) >= child_num:
                    print(child_num, len(dict[key]), dict[key])
                    print(".!!오류 : 해당 위치에 태그가 이미 존재 합니다.")
                    self.addTag(self, dict)
            if tag_name == key:
                print(".!!오류 : 해당 이름의 태그가 이미 존재 합니다.")
                self.addTag(self, dict)
                break
            for val in dict[key]:
                if tag_name == val:
                    print(".!!오류 : 해당 이름의 태그가 이미 존재 합니다.")
                    self.addTag(self, dict)
                    break
            temp += 1
        if ' ' in tag_name or '\t' in tag_name:
            print(".!!오류 : 태그 이름에는 탭이나 개행 문자가 포함될 수 없습니다.")
            self.addTag(self, dict)
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
        for line in fileinput.input("394028.txt", inplace=True, encoding='UTF-8'):
            if '(' in line and '/' in line and ')' in line:
                line = line.replace(line, new_tag)
            sys.stdout.write(line)
        print(new_tag)




if __name__ == "__main__":
    while True:
        #1.무결성 검사 후 실패시 리턴
        select_sign=CLIController.login_menu()
        
        # 기획서상 이 부분의 목업이 따로 존재하지 않고, 로그인 회원가입등의 명령어가 없기 때문에 그냥 메뉴창에서 선택한다고 가정
        #일단 목업이 없기에 임의로 출력하겠습니다(로그인)
        if select_sign==1:
            
            while True:
                input("ID:")
                input("PW:")
                #로그인에 대한 함수 return 1 -> 아이디와 파일 무결성 검사 통과 0->불통 
                check=1
                if check==1:
                    break
                else:
                    sys.exit()
            #계좌목록 함수 *밑은 임의의 출력입니다.
            CLIController.accout_list()
            #계좌 선택
            #인자와의 구분?? manage 메뉴가 필요한가
            while True:
                select_account=CLIController.account_manage_menu()
                if select_account==1:#계좌가 존재하지 않으면 다시 반복
                    print("계좌선택함수")#존재하면1 아니면0 
                    account_exist=1
                    if account_exist==1:
                        CLIController.account_function()
                    #존재하지 않으면 반복문 다시

                elif select_account==2:
                    print("계좌생성함수")
                    #계좌목록 출력 함수 임의의 출력
                    print("=======================계좌 목록 출력======================\n계좌번호 \t잔고\n383902 \t500,000,000,000\n123412 \t123,456\n321432 \t3,000")
                elif select_account==3:
                    #다른계좌본호를 안다고 가정
                    print("권한 요청 함수")
                    #성공리턴 ->1 실패리턴 ->0
                    authority=1
                    if authority==1:
                        print("권한요청성공")
                    elif authority==0:
                        print("권한요청실패")
        elif select_sign==2:

            print("회원가입 완료")
            CLIController.account_function()
            #계좌선택 클래스
        elif select_sign==3:
            print("종료")
            sys.exit()
            break
        else:
            print("올바른 인자를 입력해주세요")

