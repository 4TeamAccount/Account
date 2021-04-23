from datetime import datetime
import datetime as dt
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
    total = ''
    new_total = ''
    ac_num = ''
    change_content = []
    
    
    def setTag(self, tag): #tag가 [태그] or x.x로 들어옴
        #비정상 결과: 인자가 없는 경우 -> main에서 처리
        cli = CLIController()
        t = tag
        if t[0].isdigit(): #입력이 숫자인지 판단: 숫자로 시작되는 경우 무조건 태그 위치 입력으로 봄
        
            if any(x.isalpha() for x in t): #숫자와 문자 혼합
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag('394028'))
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
                        cli.printAllTag(ac.getAllTag('394028'))
                        return
            else:
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag('394028'))
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
                cli.printAllTag(ac.getAllTag('394028'))
                return
            else:
                #print("정상 입력 태그: {}" .format(t)) #확인용 지우기
                return t
            

    def search(self, srh_date, *srh_money):
        
        if '원' in srh_money[0][-1]:
            srh_m = srh_money[0][:-1]
        else:
            srh_m = srh_money[0]
        
        self.input_money = srh_m
            
        #print("인자 ", srh_date)
        srh_d = srh_date
        #srh_d = ''.join(srh_d)
        #s_tmp = srh_d[:4] + '.' + srh_d[4:6] + '.' + srh_d[6:]
        #srh_d = s_tmp
        i = 0
        
        print("emfdjdhaus djEjgpehlsk", srh_m, type(srh_m))
        
        file_name = self.ac_num + ".txt"
        self.account_file = file_name
        f_s = open(file_name, 'r', encoding='UTF-8')
        lines = f_s.readlines()
        #print(lines[4:])
        
        f_s.close()
        
        
        days = [] #내역에서 날짜만 뽑은거
        for l in lines[4:]:
            p = l.split(' ')[-2]
            days.append(p)
        
        i = 4
        change_content = lines[int(i):]
        tmp = list(map(lambda x: x.rstrip(), change_content))
    
        current = list(map(lambda x: x.split(' ')[-1], tmp)) #합계만 자른거
        tmp2 = list(map(lambda x: x[:-1].split(' ')[:-1], tmp)) 
        tmp = list(map(lambda x: ' '.join(x), tmp2)) #합계 전까지만 자른거
      
        for index, t in enumerate(days):
            
            if srh_d < t:
                print("srh, t", srh_d, t)
                #tmp = list(map(lambda x: x[:-1].split(' ')[-1], change_content[:-1]))
                #tmp.append(change_content[-1].split(' ')[-1])
               
                #change_content = list(map(int, tmp))
                
                print("머니 뭐힘", srh_m, type(srh_m))
                c_tmp = list(int(x) + int(srh_m) for x in current[index:])
                self.new_total = c_tmp[-1] + int(srh_m)
                
                #c_tmp = any(int(x) + int(srh_m[0]) < 0 for x in current)
                if any(c < 0 for c in c_tmp): #이후 내역이 입력 금액 때문에 음수가 되는 상황
                    self.new_total = ''
                    return 'e'
                else:
                    
                    print("된다!")
                    print("c_tmp", c_tmp)
                    res = list(map(lambda x, y: x+' '+str(y), tmp[index:], c_tmp))
                    print(res)
                    self.change_content = res
                    return index+4
                
                
                #return index+4 #찾은거 다음에 넣어야하므로!
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
            #print("문자열 길이가 1이라면 그 문자는 무조건 숫자여야 함")
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("금액은 ‘,’, ‘원’, 숫자로만 써주세요.")
            return 'e'
        elif len(mo) == 1:
            return mo
        
        if not mo[0] in head:
            #print("숫자 맨 앞은 숫자랑 + -로만 가능")
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
    
        if not mo[-1] in tail:
            #print("숫자 끝은 원이랑 숫자만 가능")
            print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
            print("금액은 ‘,’, ‘원’, 숫자로만 써주세요.")
            return 'e'
        
        if date != ():
            da = date[0]
            print("확인", da)
            res_d = self.setDate(da)
            if res_d != 'e': #숫자 입력 규칙 만족!
                print("금액 비교하러 출동")
                s = self.search(res_d, mo)
                if  s != 'e':
                    print("인덱스 보자", s)
                    print("금액 가능!")
                    return s
                else:
                    print("입력한 금액이 사용자의 잔고에 있는 금액보다 큽니다.")
                    return 'e'
            else:
                return 'e'
        else:
            res_d = datetime.today().strftime("%Y.%m.%d")
            self.input_date = res_d
            s = self.search(res_d, mo)
            if s != 'e':
                return s
            else:
                print("입력한 금액이 사용자의 잔고에 있는 금액보다 큽니다.")
                return 'e'
        
        """
        elif mo[0] == '-' and int(self.total) < int(mo[1:]):
            print("입력한 금액이 사용자의 잔고에 있는 금액보다 큽니다.")
            return 'e'
        else:
            self.input_date = datetime.today().strftime("%Y.%m.%d")
            return 'today'
         """   
    
    def setDate(self, date):
        d = date
        num = re.findall("\d+", d)
        #num = "".join(num) #문자열 하나로 합침
        #res = ''
        
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
            
        print(f"기존 숫자 {d} 변환 숫자{num}")
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
        
        print("setDate 부분")
        res = day.strftime("%Y.%m.%d")
        self.input_date = res
        return res
            

    def build(self, account_num, save_tag, i):
        #save_date = date[0]
        #print(save_date)
        #print(len(save_date))
        
        """
        if '원' in money[-1]:
            money = money[:-1]
            """
        
        money = self.input_money
        
        if '+' not in self.input_money and '-' not in self.input_money:
            self.input_money = '+' + self.input_money
        
        save_date = self.input_date
        save_total = self.new_total
        
        print("저장할 날짜 형태 보장", save_date)
        saved_data = f"{save_tag} {money} {save_date} {save_total}"
        
        print(f"입력 내용: {save_tag} {money}원 {save_date} {save_total}")    
        
        """
        if len(save_date) == 0:
            save_date = datetime.date.today()
            save_date = save_date.strftime("%Y.%m.%d")
            print(f"입력 내용: {save_tag} {money} {save_date} (오늘)")
        else:
            save_date = save_date[0].replace('-', '.').replace('/', '.')
            print(f"입력 내용: {save_tag} {money} {save_date}")
        """
        save_check = input("AccountNumber> 정말 저장하시겠습니까? (.../No) >")
        
        if save_check == "No":
            return 'back'
        else:
            self.input_tag = save_tag
            #self.input_money = money
        
            #print(self.input_tag)
            #print(self.input_money)
            #print(self.input_date)
            
            file_name = 'tmp_change' + '.txt' #파일 확정되지 않아 이름 한줄로 바꿔 했습니다.
            #file_name = account_num + ".txt"
            self.account_file = file_name
            f = open(file_name, 'r+', encoding='UTF-8')
            lines = f.readlines()
            line = lines[:i]
            print(line)
            
            cc = self.change_content
            cc.append(saved_data)
            cc = list(map(lambda x: x+'\n', cc))
            print("입력할거다!")
            print(cc)
            res = line + cc
            
            f.seek(0)
            f.writelines(res)
            f.truncate()
            f.close()
            """
            f.seek(0)
            for i in range()
            for c in cc:
                f.write(c)
            f.truncate()
            f.close()
            """
            
            #if i == 'today':
             #   print("그냥 파일 마지막에 쓰기")
              #  for l in f:
               #     pass
                #f.write(f"\n{saved_data}")
                #f.close()
            #else:
                
               
            #print(lines)
            
            self.input_tag = ''
            self.input_money = ''
            self.input_date = ''
            return 
            
    
    def addChange(self, account_num, atag):
        #print("들어온 금액 인자", money)
        #print("들어온 날짜 인자", date)
        t = ''
        m = ''
        d = ''
        
        self.ac_num = account_num
        
        file_name = account_num + ".txt"
        self.account_file = file_name
        f = open(file_name, 'r', encoding='UTF-8')
        lines = f.readlines()
        self.total = lines[-1].split(' ')[3]
        
        f.close()
        
        
        if type(atag) == list:
                try:
                    m, *d = map(str, input("AccountNumber > [{0}][{1}] 내역> " .format(main_tag[at[0]-1], sub_tag[at[0]-1][at[1]-1])).split( ))
                    t = f"[{main_tag[at[0]-1]}][{sub_tag[at[0]-1][at[1]-1]}]"
                    
                except ValueError:
                    print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                    print(".!! 오류: 금액은 길이가 1 이상이어야 합니다.")
                    self.addChange(account_num, atag)
        elif type(atag) == str:
            main_key = ''
            for key, value in tags.items():
                if at in value:
                    main_key = key
                    break
            try:    
                m, *d = map(str, input("AccountNumber > [{0}][{1}] 내역> " .format(main_key, at)).split( ))
                t = f"[{main_key}][{at}]"
                
            except ValueError:
                    print(".!! 오류: 금액, 날짜 순서로 입력해 주세요. 날짜만 생략할 수 있습니다.")
                    print(".!! 오류: 금액은 길이가 1 이상이어야 합니다.")
        
        if len(d) >= 2:
            print(".!! 오류: 인자가 너무 많습니다. 날짜와 금액은 공백을 허용하지 않습니다.")
            self.addChange(account_num, atag)
        else:
            #print("d형태", d[0])
            if len(d) == 0:    
                m_res = self.setMoney(m)
            else:
                m_res = self.setMoney(m, d[0])
            
            if m_res == 'e':
                if d:
                    for k in d:
                        for c in [',', '원']:
                            if c in k:
                                print("날짜는 ‘-’, ‘/’, ‘.’, 숫자로만 써주세요.")
        
                self.addChange(account_num, atag)
                
          
            #elif d:
             #   d_res = self.setDate(d[0])
              #  if d_res != 'e':
               #     save_res = self.build(account_num, t, m)
                #    if save_res == 'back':
                 #       print("주 프롬프트 출력해야함!")
                  #      return
                #else:
                 #   self.addChange(account_num, atag)
          
            else:
                save_res = self.build(account_num, t, m_res)
                if save_res == 'back':
                    print("주 프롬프트 출력해야함!")
                    return 'back'
            #ch.addChange('394028', ch.input_money, *ch.input_date)


        
    
        #d = date[0]

        """
        if m:
            m_res = self.setMoney(m)
            if m_res != 'e' and d:
                #print(date[0])
                if self.setDate(d) == 'e':
                    self.addChange(account_num, atag)
                else:
                    self.input_date = d
                    
            elif any(map(lambda x: x in d, [',', '원'])):
                print("날짜는 ‘-’, ‘/’, ‘.’, 숫자로만 써주세요.")
           """     
                
                
        """
        if date:
            d = date[0]
            #print(date[0])
            if self.setDate(d) == 'e':
                return
            else:
                self.input_date = d
    """
        print("입력/지출")
        
        #f.close()

class Account:
    def getAllTag(self, account_num):

        tagDict = {}
        file_name = account_num + ".txt"
        self.account_file = file_name
        file = open(file_name, 'r', encoding='UTF-8')

        for i in range(2):
            file.readline()
            if i == 1:
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

    
    #print(ch.setMoney('1000원'))

    #기획서 상 메인 출력
    c, *t = input("AccountNumber > ").split()
    if c == 'add':
        if t == []:
            print(".!! 오류: 추가 명령어 뒤에 하나의 [태그]나 태그 위치를 입력해야 합니다.")
            print("")
            CLIController.printAllTag(ac.getAllTag('394028'))
        else:
            at = ch.setTag(t[0])
            if at != None:
                add_res = ch.addChange('394028', at)
                if add_res == 'back':
                    print("주프롬프트 출력")
            """
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
                """
        #print(type(ch.setTag(t)))
        #if ch.setTag(t)[0] == 't':

    
    #ac.addChange(1234, 'a', 'b')
    
    #주태그 부태그 금액 내용 잔고 따로 담아놓기
    
    
    print("main")
