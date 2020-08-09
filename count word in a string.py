"""Count Words in a String - 
Counts the number of individual words in a string. For added 
complexity read these strings in from a text file and generate a summary."""

def countw(st):
    st = st.split(' ')
    counts = 0
    for i in st:
        counts = counts + 1
    print("Your sentence has", counts, "words.")
    return counts

count=0

file_name = input("please enter the file name: ")

try:
    file_handle = open(file_name)
    
except:
    print("not a real file")
    string = input("Let me count your words - ")
    countw(string)
    quit()
    
for line in file_handle:
    for word in line.split():
        count = count+1
        #print(word)

print("Your sentence has", count, "words.")

