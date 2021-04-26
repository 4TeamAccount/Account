import os

#AccountAdd파일의 CLIController, Account와 동일합니다. (39, 42, 45번째줄 제외)
tags = dict()
main_tag = []
sub_tag = []
class CLIController:
    @staticmethod
    # Account class의 getAllTag()를 통해 가져온 dict를 출력

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
        print("===================[{}] 하위 태그 목록 출력====================".format(m_tag))
        m = main_tag.index(m_tag) + 1
        s = 1
        print(f"{m}[{m_tag}]")
        for val in sub_tag[m - 1]:
            print(f" ㄴ{m}.{s}  {val}")
            s += 1

class Account:
    account_folder = os.path.expanduser('~') + "\\Account-data" + "\\Account"

    def getAllTag(self, account_num):
        tagDict = {}
        file_name = self.account_folder + account_num + ".txt"
        self.account_file = file_name
        #file = open(file_name, 'r') 절대경로로 되어있어서 안되네요 아래줄로 이 줄만 변경해서 했습니다! 합칠때 봐주세요
        file=open('..\\' + account_num + '.txt','r')
        #for i in range(2):  # 파일 형식 이름 한줄로 바꿔서 값 바뀐 부분1
        for i in range(3): #저랑 파일이 다른가요...? 4번째줄이 tag목록인데... 일단 윗줄을 이렇게 바꿔서 했습니다.
            file.readline()
            #if i == 1:  # 바뀐 부분2
            if i == 2: #마찬가지로 윗줄이 원본입니다.
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

#여기서부터 넣어주세요
class SearchResult:
    def __init__(self, account_num, userid, search):
        self.account_num = account_num
        self.filepath = '..\\' + account_num + '.txt'
        self.file = open(self.filepath, 'r', encoding='ANSI')
        self.backup = []
        for i in range(5):
            l = self.file.readline()
            if i == 2:
                self.usertype = 2  # l에서 아이디 찾아서 권한 넣는 함수 넣기(주프롬프트에서 사용한거 그대로 넣으면 될것같아요!)
            self.backup.append(l)
            if i == 4:
                self.changes = self.file.readlines()  # 내역들을 저장한 리스트
        self.file.close()
        self.days = []
        for change in self.changes:
            d = change.split(' ')[-2]
            self.days.append(d)
        # run
        match_list = self.search_change(self.make_search_list(search))
        if self.usertype == 1 or self.usertype == 2:
            select_change = self.select_change(match_list)
            if select_change is not None:
                self.after_find_menu(select_change)
        else:
            print("주프롬프트로 돌아감")
            return

    def make_search_list(self, search):

        search_list = [["2021.02", "2021.03."], []]
        # search에서 search_list[search_date_list,search_tag_list] 만들어 반환
        return search_list

    def search_change(self, search_list):  # 태그, 날짜 구분해 두 리스트로 받아오기
        search_date_list = search_list[0]
        search_tag_list = search_list[1]
        date_match_set = set()
        tag_match_set = set()

        if len(search_date_list) == 0 and len(search_tag_list) == 0:
            for i in range(min(10, len(self.changes))):
                date_match_set.add(i)

        if len(search_date_list) == 1:
            for k in search_date_list:
                for i, v in enumerate(self.changes):
                    if k in v:
                        date_match_set.add(i)

        elif len(search_date_list) == 2:
            search_date_list.sort()
            start = -1
            end = len(self.days) - 1

            if len(search_date_list[1]) < 8:
                search_date_list[1] += "12.31."
            elif len(search_date_list[1]) < 10:
                search_date_list[1] += "31."

            for i, day in enumerate(self.days):
                if start == -1:
                    if search_date_list[0] < day:
                        start = i
                else:
                    if search_date_list[1] < day:
                        end = i - 1
                        break;
            for i in range(start, end + 1):
                date_match_set.add(i)

        for k in search_tag_list:
            for i, v in enumerate(self.changes):
                if k in v:
                    tag_match_set.add(i)

        if len(search_date_list) != 0 and len(search_tag_list) != 0:
            match_set = (date_match_set & tag_match_set)
        else:
            match_set = (date_match_set | tag_match_set)
        match_list = sorted(match_set)
        j = 1
        for i in match_list:
            print(j, " ".join(self.changes[i].split()[:-1]))
            j += 1
        print()
        return match_list  # 파일에서 각 change의 줄(line) 수만 저장해 반환

    def select_change(self, match_list):
        while True:
            select = int(input("AccountNum> 내역 선택(취소는 0)> "))
            if select == 0:
                print("주프롬프트로 돌아감")
                return
            elif 0 < select <= len(match_list):
                return match_list[select - 1]
            else:
                print("..! 존재하지 않는 번호입니다. 범위 내의 정수만 입력할 수 있습니다.")

    def after_find_menu(self, selected_change_num):
        print("선택된 내역: ", " ".join(self.changes[selected_change_num].split()[:-1]))
        print("..! 원하시는 기능을 입력하세요(숫자 하나)")
        print("1.내역 수정    2. 내역 삭제     3. 취소")
        while True:
            select = int(input("AccountNumber> 검색 후 작업 > "))
            if select == 1:
                self.edit_change(selected_change_num)
                break
            if select == 2:
                confirm = input("AccountNumber> 정말 삭제하시겠습니까? (Yes/...) > ")
                if confirm == "Yes":
                    self.delete_change(selected_change_num)
                break
            if select == 3:
                break
            else:
                print("..! 1~3 중 원하는 기능의 메뉴 번호를 입력하세요.")
                print("1.내역 수정    2. 내역 삭제     3. 취소")
                print("선택된 내역: ", " ".join(self.changes[selected_change_num].split()[:-1]))

        print("주프롬프트로 돌아감")
        return

    def edit_change(self, change_num):
        while True:
            s = input("AccountNumber> 내역 수정> ")
            if len(s) != 0 and s != ' ':  # 공백 여러개 입력 시 예외처리...
                c, *t = s.split()
                t = ' '.join(t)
                if c == 'tag':
                    new_change = self.set_tag(t)
                    print(new_change)
                    break;
                elif c == 'date':
                    new_change = self.set_date(t)
                    break;
                elif c == 'money':
                    new_change = self.set_money(t)
                    break;
            print("..! 수정하고 싶은 항목에 따라 tag, date, money와 수정할 내용을 입력하세요.")
            print("입력 예시) tag [카페]")
            print("          date 2021.01.02")
            print("          moeny -1000원")
            print()

        new_change = "[음식][식사] -2000 2021.01.25 13000\n"
        print("수정된 내역: ", " ".join(new_change.split()[:-1]))
        confirm = input("AccountNumber> 정말 수정하시겠습니까? (.../No) > ")
        if confirm == "No":
            return

        if self.process_integrity(int(new_change.split(' ')[-3]), change_num) != -1:
            self.changes[change_num] = new_change
            self.update_file()
            print("..! 수정 성공")

    def set_tag(self, tag): #tag가 [태그] or x.x로 들어옴
        #비정상 결과: 인자가 없는 경우 -> main에서 처리
        cli = CLIController()
        t = tag
        #print(f"값{t} 형태{type(t)}")

        if t[0].isdigit(): #입력이 숫자인지 판단: 숫자로 시작되는 경우 무조건 태그 위치 입력으로 봄
            t = t.replace(' ', '')
            if any(x.isalpha() for x in t): #숫자와 문자 혼합
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag(self.account_num))
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
                        cli.printAllTag(ac.getAllTag(self.account_num))
                        return
            else:
                print("..! 존재하지 않는 태그 위치입니다. 태그 추가 및 관리는 메인 메뉴에서 tag, t, [ 로 열 수 있습니다.")
                cli.printAllTag(ac.getAllTag(self.account_num))
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


    def set_date(self):
        print()


    def set_money(self):
        print()


    def delete_change(self, change_num):
        if self.process_integrity(0, change_num) != -1:
            del self.changes[change_num]
            self.update_file()
            print("..! 삭제 성공")
            # 무결성 처리 진행 후 종료

    def process_integrity(self, new_money, index):
        balances = []
        gap = int(self.changes[index].split(' ')[-3]) - new_money
        for i, change in enumerate(self.changes):
            if i >= index:
                balance = change.split(' ')[-1]
                new_balance = int(balance) - gap
                if new_balance < 0:
                    print("..! 작업 실패: 음수 잔고 발생")
                    return -1  # 잔고 음수 발생
                balances.append(str(new_balance))
        for i, change in enumerate(self.changes):
            if i >= index:
                balance = change.split(' ')[-1]
                self.changes[i] = change.replace(balance, balances[i - index] + '\n')

    def update_file(self):
        os.remove(self.filepath)
        self.file = open(self.filepath, 'w', encoding='ANSI')
        final_list = self.backup + self.changes
        self.file.seek(0)
        self.file.writelines(final_list)
        self.file.close()

# test = 기획서 상 main에 추가해주세요
if __name__ == '__main__':
    #AccountAdd.py의 main부분과 동일합니다.
    #ch = ChangeBuilder()
    ac = Account()
    tags = ac.getAllTag('394028')
    main_tag = list(tags.keys())
    sub_tag = list(tags.values())

    #여기부터 넣어주세요
    current_account = "394028"
    current_userid = "id"
    c, *t = input("AccountNumber > ").split()
    if c == 'find':  # 메인에서 그 외 명령어들 포함해주세요!
        SearchResult(current_account, current_userid, t)
