testlist1=["2021.02.", "2021.03."]
testlist2=["[책]", "[간식]"]

class SearchResult:
    def __init__(self, accountnum, userid):
        self.accountnum=accountnum
        self.file=open('..\\'+accountnum+'.txt', encoding='UTF-8') #'ANSI'로 하니까 안되네요...
        for i in range(6):
            self.file.readline()
            if i==2:
                self.usertype = 1 #아이디 찾아서 권한 넣는 함수 넣기(주프롬프트에서 사용한거 그대로 넣으면 될것같아요!)
            if i==5:
                self.changes=self.file.readlines() #내역들을 저장한 리스트
        self.file.close()
        self.days=[]
        for change in changes:
            d = change.split(' ')[-2]
            self.days.append(d)
        print(days)
    '''
    def search_change(self, search_date_list, search_tag_list): #태그, 날짜 구분해 두 리스트로 받아오기
        date_match_set=set()
        tag_match_set=set()

        if len(search_date_list)==1:
            for i, v in enumerate(self.changes):
                if k in v:
                    date_match_set.add(i)
                    
        elif len(search_date_list)==2:
            self.changes
            sort(search_date_list)
            for i, day in enumerate(self.days):
                if search_date_list[0]<1:
            
            search_date_list[1]
            
            for k in search_date_list:
                for i, v in enumerate(self.days):
                    if k in v:
                        date_match_set.add(i)

        else:
            print("날짜는 두개만 가능.... 여기서 예외처리해도되나")
                    
        for k in search_tag_list:
            for i, v in enumerate(self.changes):
                if k in v:
                    tag_match_set.add(i)

        match_set=(date_match_set & tag_match_set)
        match_list = sorted(match_set)
        return match_list

    def select_change(self, search_list):
        while(True):
            j=1
            for i in search_list:
                print(j, self.changes[i])
                j+=1
            select = int(input("AccountNum> 내역 선택(취소는 0)> "))
            if select == 0:
                print("주프롬프트로 돌아감")
                return
            elif 0<select<=len(search_list):
                return self.changes[search_list[select-1]]
            else:
                print("..! 존재하지 않는 번호입니다. 범위 내의 정수만 입력할 수 있습니다.")

    def after_find_menu(self,selected_change):
        while(True):
            print("..! 원하시는 기능을 입력하세요(숫자 하나)")
            print("1.내역 수정    2. 내역 삭제     3. 취소")
            print("선택된 내역: ", selected_change)
            select = int(input("AccountNumber> 검색 후 작업 > "))
            if select==1:
                print("수정 메뉴")
                break
            if select==2:
                print("취소 메뉴")
                break
            if select==3:
                return
            else:
                print("..! 1~3중 원하는 기능의 메뉴 번호를 입력하세요.")
'''
#test
if __name__ == '__main__':
    search1=SearchResult()
   # search1.after_find_menu(search1.select_change(search1.search_change(testlist1,testlist2)))
