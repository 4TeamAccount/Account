testlist1=["2021.01", "2021.04"]
testlist2=["[공부]", "[간식]"]

class SearchResult:
    def __init__(self, accountnum, userid, search_date_list, search_tag_list):
        self.accountnum=accountnum
        self.file=open('..\\'+accountnum+'.txt', encoding='UTF-8') #'ANSI'로 하니까 안되네요...
        for i in range(5):
            l=self.file.readline()
            if i==2:
                self.usertype = 2 #l에서 아이디 찾아서 권한 넣는 함수 넣기(주프롬프트에서 사용한거 그대로 넣으면 될것같아요!)
            if i==4:
                self.changes=self.file.readlines() #내역들을 저장한 리스트
        self.file.close()
        self.days=[]
        for change in self.changes:
            d = change.split(' ')[-2]
            self.days.append(d)
        #run
        match_list=self.search_change(search_date_list, search_tag_list)
        if(self.usertype==1 or self.usertype==2):
            select_change=self.select_change(match_list)
            if(select_change!=None):
                self.after_find_menu(select_change)
            
    def search_change(self, search_date_list, search_tag_list): #태그, 날짜 구분해 두 리스트로 받아오기
        date_match_set=set()
        tag_match_set=set()

        if len(search_date_list)==1:
            for i, v in enumerate(self.changes):
                if k in v:
                    date_match_set.add(i)        
        elif len(search_date_list)==2:
            search_date_list.sort()
            start=-1
            end=len(self.days)-1
            
            if len(search_date_list[1])<8:
                search_date_list[1]+="12.31."
            elif len(search_date_list[1])<10:
                search_date_list[1]+="31."
            
            for i, day in enumerate(self.days):
                if start==-1:
                    if search_date_list[0]<day:
                        start=i
                else:
                    if search_date_list[1]<day:
                        end=i-1
            for i in range(start,end+1):
                date_match_set.add(i)
        else:
            print("날짜는 두개만 가능.... 여기서 예외처리해도되나")
                    
        for k in search_tag_list:
            for i, v in enumerate(self.changes):
                if k in v:
                    tag_match_set.add(i)

        if(len(search_date_list)!=0 and len(search_tag_list)!=0):
            match_set=(date_match_set & tag_match_set)
        else:
            match_set=(date_match_set | tag_match_set)
        match_list = sorted(match_set)
        j=1
        for i in match_list:
                print(j, self.changes[i])
                j+=1
        return match_list

    def select_change(self, search_list):
        while(True):
            select = int(input("AccountNum> 내역 선택(취소는 0)> "))
            if select == 0:
                print("주프롬프트로 돌아감")
                return
            elif 0<select<=len(search_list):
                return self.changes[search_list[select-1]]
            else:
                print("..! 존재하지 않는 번호입니다. 범위 내의 정수만 입력할 수 있습니다.")

    def after_find_menu(self,selected_change):
        print("선택된 내역: ", selected_change)
        print("..! 원하시는 기능을 입력하세요(숫자 하나)")
        print("1.내역 수정    2. 내역 삭제     3. 취소")
        while(True):
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
                print("..! 1~3 중 원하는 기능의 메뉴 번호를 입력하세요.")
                print("1.내역 수정    2. 내역 삭제     3. 취소")
                print("선택된 내역: ", selected_change)

#test
if __name__ == '__main__':
    SearchResult("394028", "id",testlist1,testlist2)
