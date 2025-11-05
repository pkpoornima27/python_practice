"""Input:
str = DoctorPhenomenal
Output:
DcoPeoea"""


str = input("Enter the string")
print("String entered:", str)

str1 = ""
str_len = len(str)
print("Length of the string:", str_len)
#Display alternative character
for i in range(0, str_len):
    if i%2 == 0:
        str1 = str1 + str[i]

print(str1)
