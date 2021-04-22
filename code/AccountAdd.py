from datetime import datetime
import re
import fileinput
import sys

#ACCOUNT_PATH = "C:/Users/thekoo/Documents/GitHub/Account/394028.txt"

tags = dict()
main_tag = []
sub_tag = []

class CLIController:
    @staticmethod
    #Account class의 getAllTag()를 통해 가져온 dict를 출력

    def printAllTag(dict):
        print("======================태그 목록 출력=======================")
        m = 1
        s = 1
        for key in dict.keys():
            print(f"{m}[{key}]")
            for val in dict[key]:
                print(f" ㄴ{m}.{s}  {val}")
                s += 1
            m += 1
            s = 1
            
    def printSomeTag(self, m_tag):
        print("===================[{}] 하위 태그 목록 출력====================" .format(m_tag))
        m = main_tag.index(m_tag) + 1
        s = 1
        print(f"{m}[{m_tag}]")
        for val in sub_tag[m-1]:
            print(f" ㄴ{m}.{s}  {val}")
            s += 1
            
class ChangeBuilder:
    input_tag = ''
    input_money = ''
    input_date = ''
    
    
    def setTag(self, tag): #tag가 [태그] or x.x로 들어옴
        #비정상 결과: 인자가 없는 경우 -> main에서 처리
        cli = CLIController()
        t = tag
        if t[0].isdigit(): #입력이 숫자인지 판단: 숫자로 시작되는 경우 무조건 태그 위치 입력으로 봄
        
            if any(x.isalpha() for x in t): #숫자와 문자 혼합
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                return
            
            if t.count('.') >= 2:
                print(".!! 오류: 태그 위치는 <숫자>.<숫자>로만 입력 가능합니다.")
                return
            elif not '.' in t and not 1 <= int(t) <= len(main_tag):
                print(".!! 오류: 태그 위치는 <숫자>.<숫자>로만 입력 가능합니다.")
                return
                
            if 1 <= float(t) < len(main_tag) + 0.1*len(sub_tag[-1]): #태그 목록 숫자 사이에 존재
                if not '.' in t: #상위 태그
                    print("..! 상위태그입니다. 하위 태그를 입력해주세요")
                    print("")
                    m_tag = main_tag[int(t)-1]
                    cli.printSomeTag(m_tag)
                    return
                else:
                    """
                    if t[-1] == '.':
                        print("오류 체크 추가 필요")
                        return
                    """
                    i = list(map(int,t.split('.')))
                    if i[1] <= len(sub_tag[i[0]-1]):
                        #input_tag = t #정상 결과: 하위 숫자
                        #print("정상 입력 숫자: {}" .format(t)) #확인용! 나중에 지우기
                        return i

                    else:
                        print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
            else:
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                return
                
        else: #입력이 문자
            if t.count('[') >= 2:
                print(".!! 오류: 추가 명령어 뒤에 하나의 [태그]를 입력해야 합니다.")
                return
            elif t.count('[') == 0 or t.count(']') == 0:
                print(".!! 오류: 태그를 '[', ']'로 감싸야 합니다.")
                return
            
            tmp = t[1:-1].strip()
            
            if any(x == '\n' or x == '\t' for x in t): 
                print(".!! 오류: 태그는 탭과 개행 문자의 포함을 허용하지 않습니다.")
                return
            
            t = ' '.join(tmp.split())
            if t in main_tag: #[상위태그]
                print("..! 상위태그입니다. 하위 태그를 입력해주세요")
                print("")
                cli.printSomeTag(t)
                return 
            elif not t in sum(sub_tag, []):
                print("..! 존재하지 않는 태그입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                return
            else:
                #print("정상 입력 태그: {}" .format(t)) #확인용 지우기
                return t
            


    def setMoney(self, money):
        
        return

    def setDate(self, date):
        d = date
        num = re.findall("\d+", d)
        
        if any(map(lambda x: len(x) < 2, num)):
            print(".!! 오류: 월과 일은 2자리로 입력해야 합니다.")
            return 'e'
        
        num = list(map(int, num))
        check = ['-', '/', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        print(num)
        
        for k in d:
            flag = False
            for ch in check:
                if ch in k:
                    flag = True
            if flag == False:
                print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                print("날짜는 ‘-’, ‘/’, ‘.’, 숫자로만 써주세요.")
                return 'e'
        
        today = datetime.now()
        if 1970 > num[0] or num[0] > 2037:
            print(".!! 오류: 연도가 1970년 이후부터 2037년 이전까지여야 합니다.")
            return 'e'
        
        try: 
            day = datetime(num[0], num[1], num[2])
            if day > today:
                print(".!! 오류: 미래의 내역은 작성할 수 없습니다.")
                return 'e'
        except:
            print(".!! 오류: 해당 날짜가 현행 그레고리력에 존재하는 날짜여야 합니다.")
            return 'e'
            

    def build():
        return
    
    def addChange(self, account_num, money, *date):
        print("들어온 금액 인자", money)
        print("들어온 날짜 인자", date)
        
        #f = open(ACCOUNT_PATH, "r+", encoding= 'utf-8')
        file_name = account_num + ".txt"
        self.account_file = file_name
        f = open(file_name, 'r', encoding='UTF-8')
        lines = f.readlines()
        total = lines[-1].split(' ')[1]
    
        
        if money:
            m = money
            
            self.setMoney(money)
        
        
        if date:
            d = date[0]
            #print(date[0])
            if self.setDate(d) == 'e':
                return
            else:
                self.input_date = d
    
        """
        print(len(f.readlines()))
        f.seek(0)
        n = 0
        for line in f.readlines():
            if '20' in line:
                n += 1
                print("line num: {}" .format(n))
                print("content: {}".format(line))
            else:
                n+=1
"""
        print("입력/지출")
        
        f.close()

class Account:
    def getAllTag(self, account_num):

        tagDict = {}
        file_name = account_num + ".txt"
        self.account_file = file_name
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
                if tags[i] != '':
                    temp.append(tags[i])
            tagDict[tags[0]] = temp
        return tagDict
    
    
      
        
if __name__ == '__main__':
    ch = ChangeBuilder()
    ac = Account()
    tags = ac.getAllTag('394028')
    main_tag = list(tags.keys())
    sub_tag = list(tags.values())

    
    
    #기획서 상 메인 출력
    c, *t = input("AccountNumber > ").split()
    if c == 'add':
        if t == []:
            print(".!! 오류: 추가 명령어 뒤에 하나의 [태그]나 태그 위치를 입력해야 합니다.")
            print("")
            CLIController.printAllTag(ac.getAllTag('394028'))
        else:
            at = ch.setTag(t[0])
            if type(at) == list:
                try:
                    input_m, *input_d = map(str, input("AccountNumber > [{0}][{1}] 내역> " .format(main_tag[at[0]-1], sub_tag[at[0]-1][at[1]-1])).split())
                    if len(input_d) >= 2:
                        print(".!! 오류: 인자가 너무 많습니다. 날짜와 금액은 공백을 허용하지 않습니다.")
                    else:
                        ch.addChange('394028', input_m, *input_d)
                except ValueError:
                    print("길이가 1이하 입니다!")
            elif type(at) == str:
                m = ''
                for key, value in tags.items():
                    if at in value:
                        m = key
                        break
                ch.input_money, *ch.input_date = map(str, input("AccountNumber > [{0}]{1} 내역> " .format(m, t[0])).split())
                ch.addChange('394028', ch.input_money, *ch.input_date)

        #print(type(ch.setTag(t)))
        #if ch.setTag(t)[0] == 't':

        
    
    #ac.addChange(1234, 'a', 'b')
    
    #주태그 부태그 금액 내용 잔고 따로 담아놓기
    
    
    print("main")
