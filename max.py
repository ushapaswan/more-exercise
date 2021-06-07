# def max_marks(marks):
#         print(max(marks[0]))
#         print(max(marks[1]))
#         print(max(marks[2]))
#         print(max(marks[3]))
#         print(max(marks[4]))
# max_marks([[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]])

# a=[[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]]
# print(len(a))

# def brek_sentance(word):
#         print(word.split())
# brek_sentance("my name is usha")

def max_marks(num):
        i=0
        while i<len(num):
            j=0
            k=num[i][0]
            while j<len(num[i]):
                if num[i][j]>k:
                    j=j+1
                print(num[i][j])
        i=i+1
max_marks([[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]])

