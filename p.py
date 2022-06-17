question_list=["How many continents are there?",
              "which is the capital of india",
              "who is the pm of india?",
              "How many colors are there in indian flag?"]
option_list=[["four","nine","seven","two"],
            ["Delhi","mumbai","Bangalore","kolkata"],
            ["Narendra Modi","Ramanath Kovind","APJ Abdul kalam","Manmohan singh"],
            ["Two","Three","Four","five"]]
solution_list=[3,1,1,2]
solution=[2,1,1,2]
fiftyfifty=[["four","seven"],
["Delhi","mumbai"],
["Narendra Modi","Ramanath Kovind"],
["Two","Three"]]
print("CO-POWERED by Dabar Amala presents,Koun Banega Crorepati")
print("wlecome")
i=0
c=0
while i<len(question_list):
    print("your question is on screen")
    print(i+1,question_list[i])
    a=0
    while a<len(option_list):
        print(a+1,option_list[i][a])
        a+=1
    j=int(input("enter solution"))
    if j==solution_list[i]:
        print("congrats")
    elif j==5050:
        if c==0:
            m=0
            while m<len(fiftyfifty[i]):
                print(m+1,fiftyfifty[i][m])
                m+=1
            c+=1
            num=int(input("enter solution"))
            if num==solution[i]:
                print("congrats")
            else:
                print("your ans is worng")
                break
        else:
            print("you already used lifeline")
            num1=int(input("enter solution"))
            if num1==solution_list[i]:
                print("congratulations")
            else:
                print("your ans is wrong")
                print("quit")
                break
    else:
        print("you used 5050")
        print("quit")
        break
    i+=1     