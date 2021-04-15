#import os
import pandas as pd # [Ctrl+Alt+S] > Project Interpreter > + > pandas

ACCOUNT_PATH = "C:/Users/thekoo/Desktop/394028.txt"

main_tag = []
sub_tag = []

class ChangeBuilder:
    input_tag = ''
    input_money = ''
    input_date = ''
    
    def buildTag(self, tag): #tag가 [태그] or x.x로 들어옴
        #비정상 결과: 인자가 없는 경우 -> main에서 처리
        
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
                    print("===================[{}] 하위 태그 목록 출력====================" .format(t))
                    return t
                else:
                    i = list(map(int,t.split('.')))
                    if i[1] <= len(sub_tag[i[0]-1]):
                        input_tag = t #정상 결과: 하위 숫자
                        print("정상 입력 숫자: {}" .format(t)) #확인용! 나중에 지우기
                        #print("AccountNumber > [{0}][{1}]" .format(main_tag[i[0]-1], sub_tag[i[0]-1][i[1]-1]), end = ' ')
                        input_money, *input_date = map(str, input("AccountNumber > [{0}][{1}] > 내역 > " .format(main_tag[i[0]-1], sub_tag[i[0]-1][i[1]-1])).split())
                        
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
                print("===================[{}] 하위 태그 목록 출력====================" .format(t))
                return t
            elif not t in sum(sub_tag, []):
                print("..! 존재하지 않는 태그입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                return
            else:
                input_tag = t # 정상 결과:[하위태그]
                print("정상 입력 태그: {}" .format(t)) #확인용! 나중에 지우기
                #input_money, *input_date = map(str, input("AccountNumber > [{0}][{1}] > 내역 > " .format(main_tag[i[0]-1], sub_tag[i[0]-1][i[1]-1])).split())
                        
                    

    def buildMoney(money):
        return

    def buildDate(date):
        return

    def build():
        return

class Account:
    def getAllTag(self):
        tagDict = {}
        file = open(ACCOUNT_PATH, 'r', encoding='utf-8')
        for i in range(4):
            file.readline()
            if i == 3:
                l = file.readline()
        file.close()
        sl = l.split(" ")

        #print(l)
        for s in sl:
            temp = []
            tags = s.replace("(", " ").replace(")", "").replace("/", " ").replace("\n", "").split(" ")
            for i in range(1,len(tags)):
                temp.append(tags[i])
            tagDict[tags[0]] = temp
        return tagDict

    def addChange(userid, child_tag, money, *date):

        f = open(ACCOUNT_PATH, "r+", encoding= 'utf-8')


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

        print("입력/지출")
        f.close()

if __name__ == '__main__':
    
    ch = ChangeBuilder()
    ac = Account()
    tags = ac.getAllTag()
    main_tag = list(tags.keys())
    sub_tag = list(tags.values())
    
    tag_input = '1.2'
    ch.buildTag(tag_input)
    
    #ac.addChange(1234, 'a', 'b')
    
    #주태그 부태그 금액 내용 잔고 따로 담아놓기
    
    
    print("main")
