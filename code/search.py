import os
import AccountBook

#여기서부터 넣어주세요
class SearchResult:
    def __init__(self, account_num, userid, search):
        self.account_num = account_num
        self.filepath = '..\\' + account_num + '.txt' #테스트때문에 실행중인 .py 파일 기준으로 상대경로로 해뒀는데 합치실 때 홈경로로 수정부탁드립니다!
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
        print(search)
        search_list=self.make_search_list(search)
        if search_list is not None:
            match_list = self.search_change(search_list)
            if self.usertype == 1 or self.usertype == 2:
                select_change = self.select_change(match_list)
                if select_change is not None:
                    self.after_find_menu(select_change)
        else:
            print("주프롬프트로 돌아감")
            return

    def insert_seporator(self, date):
        print("")

    def make_search_list(self, search):
        '''search_list = [[], []]
        if len(search)>0:
            while i<len(search):
                i=0
                v=search[i]
                if v[0].isdigit():
                    if len(search_list[0])>=2:
                        print("..! 날짜는 2개까지만 입력할 수 있습니다.")
                        return
                    else:
                        #구분자 삭제
                        if len(v)==8 or len(v)==6 or len(v)==4:
                            if(check_date(v)):#날짜 의미 규칙 검사
                                search_list[0].append(self.insert_seporator(v)) #구분자 삽입
                            else:
                                print("..! 날짜 의미 규칙 위배")
                                return
                        else:
                            print("..! 날짜는 구분자를 제외하고 셌을 때 4자리(연도만 입력), 6자리(연, 월만 입력), 8자리(연, 월, 일 입력)로만 검색 가능합니다.")
                            return

                elif v[0]=='[':
                    for j in range(i, len(search)):
                        if v[-1]==']':
                            end=i
                    #end = search에서 최초로 ]로 끝나는 v 인덱스 -> 다음 for에서 그 다음부터 돌도록...
                    search_tag=' ' #i, end까지 합쳐서 하나의 문자열 만들기
                    if(check_tag(search_tag)):#만든 문자열에 대해 태그 의미 규칙 검사
                        search_list[1].append(search_tag)
                else:
                    print("..! 오류: 태그를 '[', ']'로 감싸야 합니다.")
                    return
                i += 1'''
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
            try:
                select = int(input("AccountNum> 내역 선택(취소는 0)> "))
            except:
                print("..! 존재하지 않는 번호입니다. 범위 내의 정수만 입력할 수 있습니다.")
                continue
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
            try:
                select = int(input("\nAccountNumber> 검색 후 작업 > "))
            except:
                print("..! 1~3 중 원하는 기능의 메뉴 번호를 입력하세요.")
                print("1.내역 수정    2. 내역 삭제     3. 취소")
                print("선택된 내역: ", " ".join(self.changes[selected_change_num].split()[:-1]))
                continue
            if select == 1:
                self.edit_change(selected_change_num)
                break
            elif select == 2:
                confirm = input("AccountNumber> 정말 삭제하시겠습니까? (Yes/...) > ")
                if confirm == "Yes":
                    self.delete_change(selected_change_num)
                break
            elif select == 3:
                break
            else:
                print("..! 1~3 중 원하는 기능의 메뉴 번호를 입력하세요.")
                print("1.내역 수정    2. 내역 삭제     3. 취소")
                print("선택된 내역: ", " ".join(self.changes[selected_change_num].split()[:-1]))
        print("주프롬프트로 돌아감")
        return

    def edit_change(self, change_num):
        while True:
            try:
                c, *t = input("\nAccountNumber> 내역 수정> ").split()
                t = ' '.join(t)
            except:
                print("..! 수정하고 싶은 항목에 따라 tag, date, money와 수정할 내용을 입력하세요.")
                print("입력 예시) tag [카페]")
                print("          date 2021.01.02")
                print("          moeny -1000원")
                continue
            if c == 'tag':
                tag = AccountBook.ChangeBuilder.setTag(t)
                print(tag)
                if tag != 'e':
                    new_change=" " #tag 넣은 새 내역 문자열
                    break;
            elif c == 'date':
                date = AccountBook.ChangeBuilder.setDate(t)
                print(date)
                if date != 'e':
                    new_change = " "  # date 넣은 새 내역 문자열
                    break;
            elif c == 'money':
                money = AccountBook.ChangeBuilder.setMoney(t)
                print(money)
                if money != 'e':
                    new_change = " "  # money 넣은 새 내역 문자열
                    break;
            else:
                print("..! 수정하고 싶은 항목에 따라 tag, date, money와 수정할 내용을 입력하세요.")
                print("입력 예시) tag [카페]")
                print("          date 2021.01.02")
                print("          moeny -1000원")

        #new_change = "[음식][식사] -2000 2021.01.25 13000\n" #임시 테스트용(new_change생성 전 수정기능 테스트)
        print("수정된 내역: ", " ".join(new_change.split()[:-1]))
        confirm = input("AccountNumber> 정말 수정하시겠습니까? (.../No) > ")
        if confirm == "No":
            return

        if self.process_integrity(int(new_change.split(' ')[-3]), change_num) != -1:
            self.changes[change_num] = new_change
            self.update_file()
            print("..! 수정 성공")

    def set_tag(self, tag):
        print()

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
    current_account = "394028"
    current_userid = "id"
    while True:
        try:
            select_num, *t = input("\nAccountNumber> ").split()
        except:
            AccountBook.CLIController.printCommend()
            continue
        if select_num == "2" or select_num == 'find' or select_num == 'f' or select_num == '/':
            SearchResult(current_account, current_userid, t)
        else:
            AccountBook.CLIController.printCommend()