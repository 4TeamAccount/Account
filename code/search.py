testlist1=["2021.02.", "2021.03."]
testlist2=["[책]", "[간식]"]

class SearchResult:
    def __init__(self):
        self.file=open('..\\394028.txt', encoding='UTF-8') #'ANSI'로 하니까 안되네요...
        for i in range(6):
            self.file.readline()
            if i==5:
                self.changes=self.file.readlines() #내역들을 저장한 리스트
    
    def searchChange(self, search_date_list, search_tag_list): #태그, 날짜 구분해 두 리스트로 받아오기
        date_match_set=set()
        tag_match_set=set()

        for k in search_date_list:
            for i, v in enumerate(self.changes):
                if k in v:
                    date_match_set.add(i)
                    
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
            select = int(input("내역 선택(취소는 0)> "))
            if select == 0:
                print("종료")
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
            select = int(input("검색 후 작업 > "))
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

#test
search1=SearchResult()
search1.after_find_menu(search1.select_change(search1.searchChange(testlist1,testlist2)))
