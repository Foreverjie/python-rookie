class Student(object):

    @property
    def score(self):
        return self._score

    #若有 property 无 setter,即为只读属性
    @score.setter
    def score(self, value):
        self._score = value

s = Student()
s.score = 60
print(s.score)