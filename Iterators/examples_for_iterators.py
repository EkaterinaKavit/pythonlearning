#Решение задачи при помощи итератора

# class Sentence:
#
#     def __init__(self,sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.words[index]
#
#         return
#
#
# my_sentence = Sentence('This is my secret')
#
# for word in my_sentence:
#     print(word)


#  Решение задачи при помощи генератора
def my_sentense(sentence):
    for word in sentence.split():
        yield word

test_sentence = my_sentense('I am cool')

# for word in test_sentence:
#     print(word)
print(next(test_sentence))
print(next(test_sentence))
print(next(test_sentence))
print(next(test_sentence))





