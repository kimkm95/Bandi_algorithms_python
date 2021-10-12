import math

# # def russian_mul(m,n):
# #     def loop(m,n):
# #         if n > 1:
# #             m = m * 2
# #             n = math.trunc(n /2)
# #             if(n % 2 == 0):
# #                 return loop(m,n)
# #             else:
# #                 return m + loop(m,n)
# #         else:
# #             return 0;
# #     if n > 0:
# #         return loop(m,n)
# #     else:
# #         return 0

# # result = russian_mul(57,86)
# # print(result)



# def russian_mult(m,n):
#     a = 0
#     def loop(m,n,a):
#         if n > 1:
#             m = m * 2
#             n = math.trunc(n/2)
#             if (n % 2 == 0):
#                 return loop(m,n,a)
#             else:
#                 a += m
#                 return loop(m,n,a)
#         else:
#             return a
#     if n > 0:
#         return loop(m,n,a)
#     else:
#         return 0

# result = russian_mult(57,86)
# print(result)


# def russian_muls(m,n):
#     sum = 0
#     if n > 0:
#         while(1):
#             m = m *2
#             n = math.trunc(n/2)
#             if(n % 2 == 0):
#                 continue;
#             else:
#                 sum += m
#             if (n == 1):
#                 return sum
#     else:
#         return 0

# result = russian_muls(57,86)
# print(result)


# def fac(n):
#     if n > 1:
#         return fac(n-1) * n
#     else:
#         return 1

# def fac(n):
#     def loop(n, ans = 1):
#         if n > 1:
#             return loop(n-1,ans = ans * n)
#         else:
#             return ans
#     return loop(n,1)

# result = fac(3)
# print(result)

def fac(n):
    ans = 1
    while n > 1:
        n, ans = n-1, ans * n
    return ans

result = fac(3)
print(result)



