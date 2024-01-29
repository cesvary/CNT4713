import socket

class Assignment2:
    def __init__(self, year: int):
        self.year = year

    def tellAge(self, currentYear: int):
        birth_year = currentYear - self.year
        print(f'Your age is {birth_year}')

    def listAnniversaries(self):
        current_year = 2022
        anniversaries = [i for i in range(10, current_year - self.year + 1, 10)]
        return anniversaries

    def modifyYear(self, n: int):
        year_str = str(self.year)
        result = (year_str[:2] * n) + (year_str[::2] * n)
        return result

    @staticmethod
    def checkGoodString(string: str) -> bool:
        if len(string) >= 9 and string[0].islower() and string.count('0') == 1:
            return True
        return False

    @staticmethod
    def connectTcp(host: str, port: int):
        try:
            with socket.create_connection((host, port)) as s:
                return True
        except Exception as e:
            return False


