class SuperStr(str):
    def is_repeatance(self, s):
        if s == '':
            return False
        if self == '':
            return True
        if len(self) % len(s) != 0:
            return False
        if self == s * (len(self) // len(s)):
            return True
        return False

    def is_palindrome(self):
        if self.lower() == self.lower()[::-1]:
            return True
        return False

s = SuperStr('abcabcabc')
print(s.is_repeatance('abc'))

s = SuperStr('abcabcabc')
print(s.is_repeatance('cba'))

s = SuperStr('abcabcabc')
print(s.is_repeatance(''))

s = SuperStr('level')
print(s.is_palindrome())

s = SuperStr('LeVel')
print(s.is_palindrome())

s = SuperStr('hello')
print(s.is_palindrome())