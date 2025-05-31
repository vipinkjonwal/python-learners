class TestClass:
    def __init__(self, initArg):
        self.initArf = initArg

    @classmethod
    def testEnum(cls):
        countryList = ["India", "Australia", "USA", "France", "Japan", "Korea"]

        for i in dict(enumerate(countryList)):
            print(i)


    def displayOutput(self):
        """_summary_
        """
        print(self.initArf)
        try:
            print(10/8)
        except Exception as e:
            print(e)

def main():
    obj = TestClass("hello")
    # TestClass.testEnum()
    obj.displayOutput()


if __name__ == '__main__':
    main()
