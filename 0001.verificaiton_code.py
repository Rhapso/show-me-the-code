import random
import string

class veriCode(object):
    def __init__(self, number):
        self._codeNum = number
        self._code = []
        self._codeLength = 10

    def genCode(self):
        self._code = []
        for i in range(self._codeNum):
            oriNum = [random.choice(string.digits) for _ in range(self._codeLength/2)]
            oriLet = [random.choice(string.ascii_letters) for _ in range(self._codeLength/2)]
            oriCode = oriNum + oriLet
            random.shuffle(oriCode)
            codeEnd = ''.join(oriCode)
            self._code += [codeEnd]

if __name__ == '__main__':
    code = veriCode(200)
    code.genCode()
    print(code._code)
    