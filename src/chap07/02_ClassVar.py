class ClassVar:
    text_list = [] # static변수(class변수)와 같은 개념 / golbal변수로 사용 하기 위함.

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == "__main__":
    ClassVar.text_list.append('a')

    print(ClassVar.text_list)

    x = ClassVar()
    x.add('b')
    x.print_list()

    print(ClassVar.text_list)

    y = ClassVar()
    y.add('c')
    y.print_list()

    print(ClassVar.text_list)