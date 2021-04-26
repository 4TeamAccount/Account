import os
import re

import AccountBook


# 여기서부터 넣어주세요
class SearchResult:
    def __init__(self, account_num, userid, search):
        self.account_num = account_num
        self.userid = userid
        self.filepath = '..\\' + account_num + '.txt'  # 테스트때문에 실행중인 .py 파일 기준으로 상대경로로 해뒀는데 합치실 때 홈경로로 수정부탁드립니다!
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
        search_list = self.make_search_list(search)
        if search_list is not None:
            match_list = self.search_change(search_list)
            if len(match_list) == 0:
                print("검색결과가 없습니다.")
            elif self.usertype == 1 or self.usertype == 2:
                select_change = self.select_change(match_list)
                if select_change is not None:
                    self.after_find_menu(select_change)
        else:
            print("주프롬프트로 돌아감")
            return

    def insert_seporator(self, date):
        if len(date) == 8:
            return date[:4] + '.' + date[4:6] + '.' + date[6:] + '.'
        elif len(date) == 6:
            return date[:4] + '.' + date[4:] + '.'
        else:
            return date + '.'

    def make_search_list(self, search):
        search_list = [[], []]
        tmp = ""
        for v in search:
            if (len(tmp) == 0 and v[0] == '[') or (v[-1] != ']' and len(tmp) != 0):
                tmp = tmp + ' ' + v
                if v[-1] == ']':
                    tag = tmp.strip()
                    search_list[1].append(tag)
                    tmp = ""
            elif v[-1] == ']' and len(tmp) != 0:
                tmp = tmp + ' ' + v
                tag = tmp.strip()
                search_list[1].append(tag)
                tmp = ""
            elif len(tmp) == 0 and v[0].isdigit():
                if len(search_list[0]) >= 2:
                    print("..! 날짜는 2개까지만 입력할 수 있습니다.")
                    return
                else:
                    # 해석 들어가기 전에 여기서 사실 문법규칙 검사 해야함.... 2021.0813이 틀렸다던가...
                    date = "".join(re.findall("\d+", v))
                    if len(date) == 8 or len(date) == 6 or len(date) == 4:
                        # if(check_date(date)):#날짜 의미 규칙 검사
                        if True:  # 위 함수 통과했다 가정
                            search_list[0].append(self.insert_seporator(date))  # 구분자 삽입
                        else:
                            print("..! 날짜 의미 규칙 위배")
                            return
                    else:
                        print("..! 날짜는 구분자를 제외하고 셌을 때 4자리(연도만 입력), 6자리(연, 월만 입력), 8자리(연, 월, 일 입력)로만 검색 가능합니다.")
                        return
            else:
                print("..! 오류: 태그를 '[', ']'로 감싸야 합니다.")
                return
        if 0 != len(tmp):
            print("..! 오류: 태그를 '[', ']'로 감싸야 합니다.")
            return

        # search_list = [["2021.02", "2021.03."], ["[식사]"]] #테스트용
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
            end = len(self.days)

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
                        end = i
                        break
            for i in range(start, end):
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
            change_builder = AccountBook.ChangeBuilder(self.account_num)
            if c == 'tag':
                a = AccountBook.Account(self.account_num, self.userid)
                change_builder.tags = a.getAllTag(self.account_num)
                change_builder.main_tag = list(change_builder.tags.keys())
                change_builder.sub_tag = list(change_builder.tags.values())
                tag = change_builder.setTag(t)
                print(tag)
                if tag != 'e':
                    new_change = " "  # tag 넣은 새 내역 문자열
                    break
            elif c == 'date':
                date = change_builder.setDate(t)
                print(date)
                if date != 'e':
                    new_change = " "  # date 넣은 새 내역 문자열
                    break
            elif c == 'money':
                money = change_builder.setMoney(t)
                print(money)
                if money != 'e':
                    new_change = " "  # money 넣은 새 내역 문자열
                    break
            else:
                print("..! 수정하고 싶은 항목에 따라 tag, date, money와 수정할 내용을 입력하세요.")
                print("입력 예시) tag [카페]")
                print("          date 2021.01.02")
                print("          moeny -1000원")

        # new_change = "[음식][식사] -2000 2021.01.25 13000\n" #임시 테스트용(new_change생성 전 수정기능 테스트)
        print("수정된 내역: ", " ".join(new_change.split()[:-1]))
        confirm = input("AccountNumber> 정말 수정하시겠습니까? (.../No) > ")
        if confirm == "No":
            return

        if self.process_integrity(int(new_change.split(' ')[-3]), change_num) != -1:
            self.changes[change_num] = new_change
            self.update_file()
            print("..! 수정 성공")

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
