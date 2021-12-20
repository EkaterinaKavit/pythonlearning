# nums = [1,2,3]
# for num in nums:
#     print(num )

#print(dir(nums))

# i_nums = iter(nums)
# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))



class MyRange:
    def __init__(self,start,end,n):
        self.value = start
        self.end = end
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += self.n
        return current


def my_range(start,end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(5,20)

for num in nums:
    print(num)