class Account:


    def getAllTag(self):
        tagDict = {}
        file = open("394028.txt", 'r')
        for i in range(4):
            file.readline()
            if i == 3:
                l = file.readline()
        file.close()
        sl = l.split(" ")
        for s in sl:
            temp = []
            tags = s.replace("(", " ").replace(")", "").replace("/", " ").replace("\n", "").split(" ")
            for i in range(1,len(tags)):
                temp.append(tags[i])
            tagDict[tags[0]] = temp
        return tagDict

    # def printMainTag(self):
    #     print("==========주태그==========")
    #     for key in self.tagDict.keys():
    #         print(key)
    #
    # def printSubTag(self, mainTag):
    #     m = 1
    #     for key in self.tagDict.keys():
    #         if key == mainTag:
    #             break
    #         m += 1
    #
    #     print("==========부태그==========")
    #     s = 1
    #     for val in self.tagDict[mainTag]:
    #         print(f"{m}.{s} {val}")
    #         s += 1


    # def getAllTag(self):
    #     print("==========태그목록============")
    #     m = 1
    #     s = 1
    #     for key in self.tagDict.keys():
    #         print(f"{m}  {key}")
    #         for val in self.tagDict[key]:
    #             print(f"\t{m}.{s}  {val}")
    #             s += 1
    #         m += 1
    #         s = 1
