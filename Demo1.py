class UserMainCode(object):
    @classmethod
    def iswhiteLine(cls, input1):
        import re
        str=input1
        pattern=r"\s"
        match = re.search(pattern,str)
        if match:
            print(True)
        else:print(False)





input1 = "\tn"
UserMainCode.iswhiteLine(input1)
