import os

class SearchResult:
    def __init__(self, account_num, userid, search):
        self.account_num = account_num
        self.filepath = '..\\' + account_num + '.txt'
        self.file = open(self.filepath, 'r', encoding='ANSI')
        self.backup=[]
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
        # match_list = self.search_change(self.make_search_list(search))

        testlist1 = ["2021.", "2021.02."]
        testlist2 = []
        match_list = self.search_change([testlist1, testlist2])

        if self.usertype == 1 or self.usertype == 2:
            select_change = self.select_change(match_list)
            if select_change != None:
                self.after_find_menu(select_change)
        else:
            print("주프롬프트로 돌아감")
            return

    # def make_search_list(self, search):

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
            print(j, self.changes[i], end='')
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
        print("선택된 내역: ", self.changes[selected_change_num])
        print("..! 원하시는 기능을 입력하세요(숫자 하나)")
        print("1.내역 수정    2. 내역 삭제     3. 취소")
        while True:
            select = int(input("AccountNumber> 검색 후 작업 > "))
            if select == 1:
                self.edit_change(selected_change_num)
                break
            if select == 2:
                confirm = input("AccountNumber> 정말 삭제하시겠습니까? (Yes/...) >")
                if confirm == "Yes":
                    self.delete_change(selected_change_num)
                break
            if select == 3:
                break
            else:
                print("..! 1~3 중 원하는 기능의 메뉴 번호를 입력하세요.")
                print("1.내역 수정    2. 내역 삭제     3. 취소")
                print("선택된 내역: ", self.changes[selected_change_num])

        print("주프롬프트로 돌아감")
        return

    def edit_change(self, change_num):
        print("수정")

    def delete_change(self, change_num):
        money = int(self.changes[change_num].split(' ')[-3])
        if self.process_integrity(money, change_num)!=-1:
            del self.changes[change_num]
            self.update_file()
            print("..! 삭제 성공")
        # 무결성 처리 진행 후 종료

    def process_integrity(self, money, index):
        balances = []
        for i, change in enumerate(self.changes):
            if i >= index:
                balance = change.split(' ')[-1]
                new_balance = int(balance) - money
                if new_balance < 0:
                    print("..! 삭제 실패: 음수 잔고 발생")
                    return -1 # 잔고 음수 발생
                balances.append(str(new_balance))
        for i, change in enumerate(self.changes):
            if i >= index:
                balance = change.split(' ')[-1]
                self.changes[i] = change.replace(balance, balances[i-index]+'\n')

    def update_file(self):
        os.remove(self.filepath)
        self.file = open(self.filepath, 'w', encoding='ANSI')
        final_list=self.backup+self.changes
        self.file.seek(0)
        self.file.writelines(final_list)
        self.file.close()

# test = 기획서 상 main에 추가해주세요
if __name__ == '__main__':
    current_account = "394028"
    current_userid = "id"
    c, *t = input("AccountNumber > ").split()
    if c == 'find':  # 메인에서 그 외 명령어들 포함해주세요!
        SearchResult(current_account, current_userid, t)
        '''
        if t == []:
            # 인자 없으면 최근 10개 내역 검색되도록 해야함
            SearchResult(current_account, current_userid, t)
        else:
            tmp = ' '.join(t)
            tmp = tmp.strip()  # 앞뒤 공백 없앤 문자열로 다시 반환
            SearchResult(current_account, current_userid, t)
        '''
    # SearchResult("394028", "id", testlist1, testlist2)