"""Count Vowels - 
Enter a string and the program counts the number of vowels in the text. 
For added complexity have it report a sum of each vowel found."""
import pandas as pd 

string = input('Please enter a work - ')
string = string.lower()
#string =list(string)
s = pd.Series([string])
no = s.str.count('[aeiou]')

print(no.at[0])