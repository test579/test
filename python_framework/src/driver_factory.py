import os


class DriverFactory:
    def aaa(self):
        print(os.getcwd())
x = DriverFactory()
x.aaa()