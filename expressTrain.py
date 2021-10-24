# D = 325
# H = 16.0 / 60.0
# print(int(D / H)) 

# D = 42195
# S = ((121*60) + 39)

# print(int(D / S))


# def celsius2fahrenheit(C):
#     F = 9/5 * C + 32
#     return F
# print(celsius2fahrenheit(19.4))
# print(round(celsius2fahrenheit(19.4),1))


# # 대출 상환금 계산 서비스
# # 대출금 상환금액을 계산해주는 프로그램
# #
# # 입력
# print("자유은행 대출 상환금 계산 서비스에 오심을 환영합니다.")
# principal = int(input("대출원금이 얼마인가요? (백만원이상) "))
# interest = float(input("연 이자율은 몇% 인가요? (0.0~9.9) "))
# year = int(input("상환기간은 몇 년인가요? "))

# # 상환금 계산
# p = principal
# r = (interest / 12) / 100
# m = year * 12
# print(r)

# def monthly_payment_plan(principal, interest, year):
#     d = int((1+r)**m * p * r/ ((1 + r)**m - 1))
#     return d

# payment_monthly = monthly_payment_plan(p,r,m)

# # 출력
# print()
# print("대출 상환금 내역을 알려드리겠습니다.")
# print("대출원금:", principal, "원")
# print("연 이자율", interest, "%로", year, "년 동안 매월 원리금 균등 상환")
# print("매월", payment_monthly, "원씩 지불하셔야 합니다.")
# print("상환 완료시까지 총 상환금액은", payment_monthly * 12 * year, "원 입니다.")
# print()
# print("저희 자유은행은 항상 여러분과 함께 합니다.")
# print("또 들려주세요.")




# # ##### 연습 문제

# # ### 3.1 - 윤년 확인 함수 (p.130-131)

# def isleapyear(year):
#     if year >= 0:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             return True
#         else:
#             return False



# # # Test code
# # for y in range(5):
# #     print(y, isleapyear(y))
# # # True False False False True
# # for y in range(2010,2017):
# #     print(y, isleapyear(y))
# # # False False True False False False True
# # for y in range(1900, 2600, 100):
# #     print(y, isleapyear(y))
# # # False True False False False True False
# # print(-2000, isleapyear(-2000))
# # # None



# ### 3.2 - 유효 날짜 검증 함수 (p.131-132)

# def is_valid_date(year, month, day):
#     if(year < 0 ):
#         return False
#     if 1 > month and month > 12:
#         return False
#     if 1 > day and day > 31:
#         return False
    
#     month_31arr = [1,3,5,7,8,10,12]
#     month_30arr = [4,6,9,11]

#     for i in month_31arr:
#         if(month == i):
#             if(day <= 31 and day >= 1):
#                 return True
#     for i in month_30arr:
#         if(month == i):
#             if(day <= 30 and day >= 1):
#                 return True

#     if(isleapyear(year)):
#         if(month == 2):
#             if(day <= 29 and day >= 1):
#                 return True
#         else:
#             if(day <= 28 and day >= 1):
#                 return True
#     return False


# # # # Test code
# # print(is_valid_date(2020,11,31)) # False
# # print(is_valid_date(2020,2,29))  # True



# def front_ok(s):
#     year = int(s[:2])
#     month = int(s[2:4])
#     day = int(s[4:6])
#     century = int(s[-1])
    
#     century1990 = [1,2,5,6]
#     century2000 = [3,4,7,8]
#     century1800 = [9,0]

#     #  짝수는 여성, 홀수는 남성
#     if(century in century1990):
#         year += 1900
#     if(century in century2000):
#         year += 2000
#     if(century in century1800):
#         year += 1800

#     return is_valid_date(year,month,day)

# def back_ok(s):
#     a =[]
#     for i in range(0, len(s)):
#         a.append(int(s[i]))
#     check = 11 - ((2*a[0]+3*a[1]+4*a[2]+5*a[3]+6*a[4]+7*a[5]+8*a[6]+9*a[7]+2*a[8]+3*a[9]+4*a[10]+5*a[11]) % 11)
#     if(check == 10):
#         check = 0
#     if(check == 11):
#         check = 1
#     return check == int(s[-1])


# def isRRN(s):
#     (front, mid, back) = s.partition("-")
#     return front_ok(front+back[0]) and mid == "-" and back_ok(front + back)

# # Test your RRN number
# print(isRRN("000101-0000000")) # True
# print(isRRN("991231-9999991")) # True



# def smaller(x,y):
#     if x < y:
#         return x
#     else:
#         return y

        
# def smallest(x,y,z):
#     if x < y:
#         if x < z:
#             return x
#         else:
#             return z
#     else:
#         if y < z:
#             return y
#         else:
#             return z

# def smallest(x,y,z):
#     return smaller(smaller(x,y),z)


# ### 3.4 - 셋 중 가운데 수 찾기 함수 (p.133-134)

# def median(x,y,z):
#     one = smallest(x,y,z)
#     if(one == x):
#         return smaller(y,z)
#     if(one == y):
#         return smaller(x,z)
#     if(one == z):
#         return smaller(x,y)



# # # Test code
# print(median(1,3,5)) # 3
# print(median(3,5,1)) # 3
# print(median(3,3,3)) # 3
# print(median(3,5,3)) # 3
# print(median(3,5,5)) # 5 


# def even(x):
#     return x % 2 == 0

# def smaller_odd(x,y):
# # x 가 y보다 작은경우
#     if(x < y):
#         # 근데, x가 짝수인 경우
#         if(even(x)):
#             # y 마저 짝수
#             if(even(y)):
#                 return None
#             return y
#         return x
#     # y가 x보다 크거나 작을 경우
#     else:
#         if(even(y)):
#             # y 마저 짝수
#             if (even(x)):
#                 return None
#             return x
#         return y

        
# def smallest_odd(x,y,z):
#     one = smaller_odd(x,y)
#     # x나 y중에 홀수가 있었던 경우
#     if(one != None):
#         # z가 짝수였던 경우 
#         if(even(z)):
#             return one
#         return smaller_odd(one,z)
#     else:
#         if(even(z)):
#             return None
#         return z


# # # Test code
# print(smallest_odd(3,2,2))  # 3 
# print(smallest_odd(3,5,7))  # 3 
# print(smallest_odd(3,5,1))  # 1 
# print(smallest_odd(8,3,4))  # 3
# print(smallest_odd(8,3,5))  # 3
# print(smallest_odd(8,5,3))  # 3
# print(smallest_odd(2,8,3)) # 3
# print(smallest_odd(2,8,4))  # None    


# ### 3.6 - 이차방정식 근 구하는 함수 (p.135-136)

# import math
# def quadratic_equation_positive(a,b,c):
#     if a != 0:
#         delta = b**2 - (4 * a * c)
#         if(delta > 0):
#             root = math.sqrt(delta)
#             ans1 = ((-b) + root) / (2 * a)
#             ans2 = ((-b) - root) / (2 * a)
            
#             return ans1, ans2
#         else:
#             return None
#     else:
#         return None


# print(quadratic_equation_positive(1,-1,-2)) # (2.0, -1.0)
# print(quadratic_equation_positive(3,3,3)) # None
# print(quadratic_equation_positive(0,3,4)) # None






# ### 3.7 - 수강과목 점수 평균 구하기 프로시저 (과락 제외 버전) (p.136-137)


# print("Score Average Calculator")
# number = input("How many classes? ")
# while not (number.isdigit() and int(number) > 0):
#     number = input("Enter a positive number: ")
# print("The number of classes =", number)

# score_arr = []
# count = 0
# for i in range(0, int(number)):
#     one = int(input("Enter your score "))
#     score_arr.append(one)
#     print(f"Your score = {one}")
#     if(one < 60):
#         score_arr.pop()
#         count += 1
# total = sum(score_arr)
# if(score_arr):
#     average_score = total / len(score_arr)
# else:
#     average_score = 0.0
# print(f"Your average score = {average_score}")
# print(f"Failed = {count}")


# ### 3.8 - 24시간 시계 형식 확인 (p.137-138)

# # code : 3-23.py
# def validclock24(time):
#     (hour, colon, minute) = time.partition(":")
#     return len(hour) == 2 and len(minute) == 2 and \
#            colon == ":" and \
#            0 <= int(hour) <= 23 and 0 <= int(minute) <= 59 or \
#            int(hour) == 24 and int(minute) == 0

# # # Test code
# print(validclock24("00:00"))  # True
# print(validclock24("00:30"))  # True
# print(validclock24("09:58"))  # True
# print(validclock24("12:15"))  # True
# print(validclock24("23:59"))  # True
# print(validclock24("24:00"))  # True
# print(validclock24("7:07"))   # False
# print(validclock24("07:121")) # False
# print(validclock24("13:4"))   # False
# print(validclock24("00:60"))  # False
# print(validclock24("24:01"))  # False
# print(validclock24("25:10"))  # False




# # code : 3-24.py
# def validclock12(time):
#     (hour, colon, minuteplus) = time.partition(":")
#     minute = minuteplus[:-2]
#     am_or_pm = minuteplus[-2:]
#     return (len(hour) == 1 and 1 <= int(hour) <= 9 or \
#             len(hour) == 2 and 10 <= int(hour) <= 12) and \
#            colon == ":" and \
#            len(minute) == 2 and 0 <= int(minute) <= 59 and \
#            (am_or_pm == "am" or am_or_pm == "pm")


# # # Test code
# print(validclock12("1:30am"))  # True
# print(validclock12("9:12pm"))  # True
# print(validclock12("3:05am"))  # True
# print(validclock12("10:14pm")) # True
# print(validclock12("11:59pm")) # True
# print(validclock12("12:00am")) # True
# print(validclock12("12:00pm")) # True
# print(validclock12("0:15am"))  # False
# print(validclock12("09:18pm")) # False
# print(validclock12("3:5am"))   # False
# print(validclock12("00:00pm")) # False
# print(validclock12("5:60am"))  # False


### 3.9 - 12시간 시계 형식 확인 (p.138-139)

# code : 3-24.py
def clock12to24(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    am_or_pm = minuteplus[-2:]

    if(am_or_pm == 'am'):
        if(int(hour) == 12):
            hour = '00'
        if(len(hour) != 2):
            hour = '0' + hour
        return hour + colon + minute
    elif(am_or_pm == 'pm'):
        if(int(hour) <12):
            hour = str(int(hour) + 12)
        return hour + colon + minute

    return hour + colon + minute

# Test code
print(clock12to24("12:00am")) # "00:00"
print(clock12to24("12:05am")) # "00:05"
print(clock12to24("1:30am"))  # "01:30"
print(clock12to24("3:05am"))  # "03:05"
print(clock12to24("12:00pm")) # "12:00"
print(clock12to24("12:08pm")) # "12:08"
print(clock12to24("3:50pm"))  # "15:50"
print(clock12to24("9:12pm"))  # "21:12"
print(clock12to24("11:59pm")) # "23:59"


# ### 3.10 - 24시간 시계를 12시간 시계로 변환 (p.140)

# # code : 3-25.py
# def clock24to12(time):
#     (hour, colon, minute) = time.partition(":")
#     if int(hour) == 0 or int(hour) == 24:
#         return "12" + colon + minute + "am"
#     elif int(hour) < 12:
#         return hour + colon + minute + "am"
#     elif int(hour) == 12:
#         return hour + colon + minute + "pm"
#     else: # int(hour) > 12
#         return str(int(hour)-12) + colon + minute + "pm"

# # # Test code
# # print(clock24to12("00:00")) # "12:00am"
# # print(clock24to12("00:05")) # "12:05am"
# # print(clock24to12("09:58")) # "9:58am"
# # print(clock24to12("11:43")) # "11:43am"
# # print(clock24to12("12:08")) # "12:08pm"
# # print(clock24to12("15:50")) # "3:50pm"
# # print(clock24to12("20:20")) # "8:20pm"
# # print(clock24to12("24:00")) # "12:00am"