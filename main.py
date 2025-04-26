class Solution:
    
    # question number 1
    def thief_problem(self, arr, got_now):
        if len(arr) == 0:
            return 0
        b = self.thief_problem(arr[1:], got_now)
        got_now_temp = got_now + arr[0]
        a = arr[0] + self.thief_problem(arr[2:], got_now_temp)
        return max(a,b)
    
    # question number 2
    def pattern(self, n):
        for i in range(1, n+1):
            if i % 2 == 1:
                print( f'{i}' * (n-1) + f'{i+1}' )
            else:
                print( f'{i+1}' + f'{i}'*(n-1) )
    
    # question number 3
    def disarium(self, n):
        sum = 0
        number_list = str(n)
        for i, num in enumerate(number_list,1):
            sum += (int(num)**i)
        if sum == n:
            return True
        else:
            return False
    
    def disarium_upto_n(self, n):
        list_of_disarium = list()
        for i in range(n):
            if self.disarium(i):
                list_of_disarium.append(i)
        print(f'upto {n} disarium numbers are:\n', list_of_disarium)
    
    def disarium_in_range(self, a, b):
        list_of_disarium = list()
        for i in range(a, b+1):
            if self.disarium(i):
                list_of_disarium.append(i)
        
        print(f'disarium numbers in range {a}, {b}:\n', list_of_disarium)

# object creation

solution = Solution()

# For thief problem 
input_list = [6,7,1,3,8,2,5]
print(solution.thief_problem(input_list, 0))

# For printing pattern
n2 = 5
solution.pattern(n2)

# Desarium Number
n3 = 135
# print(solution.disarium(n3))
n3 = 200
solution.disarium_upto_n(n3)
a, b = 1, 200
solution.disarium_in_range(a, b)