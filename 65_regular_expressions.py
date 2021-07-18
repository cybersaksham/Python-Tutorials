"""
Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
"""

import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Phone numbers : -
+91 9455462134
+91 9455445634
+91 9445123834
+91 9468462134
+91 9456245878
+91 9455462514
+91 4565485134
+91 9458592134

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii1234567891011'''

# findall, search, split, sub, finditer

# META CHARACTERS
# patt = re.compile(r'fass') --> search fass anywhere
# patt = re.compile(r'.adm') --> search for adm anywhere
# patt = re.compile(r'.') --> search for all characters except newline character
# patt = re.compile(r'^Tata') --> match if string starts with Tata
# patt = re.compile(r'iin$') --> match if string ends with iin
# patt = re.compile(r'ai*') --> match for a, ai, aii, aiii, aiiii....... (for any number of i)
# patt = re.compile(r'ai+') --> match for ai, aii, aiii, aiiii....... (for any number of i > 0)
# patt = re.compile(r'ai{2}') --> match for only aii (for 2 number of i)
# patt = re.compile(r'(ai){2}') --> match for aiai (for 2 number of ai)
# patt = re.compile(r'ai{1}|Fax') --> match for either ai or Fax


# SPECIAL SEQUENCES
# patt = re.compile(r'/AFax') --> match if string starts with Fax
# patt = re.compile(r'Fax\b') --> match for words starting or ending with Fax
# patt = re.compile(r'Fax\B') --> match for words containing Fax but not at starting or ending
# patt = re.compile(r'\d{5}') --> search for a number of 5 digits
# patt = re.compile(r'\D{11}') --> search all substring of length 11 without digits
# patt = re.compile(r'\s') --> search whitespaces or newline character
# patt = re.compile(r'\S') --> search characters except whitespaces & \n
# patt = re.compile(r'\w') --> search alphabets, numbers, '_' character
# patt = re.compile(r'\W') --> search except alphabets, numbers, '_' character
# patt = re.compile(r'11\Z') --> search if 11 is at end of string

numbers = re.compile('\+91 \d{10}').finditer(mystr)
# for match in numbers:
#     print(match)
ls = []
for i in numbers:
    ls.append(i)
print(ls)
