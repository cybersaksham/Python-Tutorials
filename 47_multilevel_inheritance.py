"""
If we write any command to son then -
First search for any command in son,
then in father & then in grandfather
"""


class Grandfather:
    basketball = 1


class Father(Grandfather):
    dance = 1

    def father_det(self):
        return f"Yes i dance {self.dance} times"


class Son(Father):
    dance = 6

    def son_det(self):
        return f"Yes i dance awesomly {self.dance} times & play basketball {self.basketball} times"


darry = Grandfather()
larry = Father()
harry = Son()

print(f"harry :-\n{harry.son_det()}")
