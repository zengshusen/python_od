
def check_phone(phone):
    if not phone.isdigit():
        return f"当前手机号格式不正确!"
    if len(phone)!=11:
        return f"当前的手机号格式不正确，必须是11位!"
    if phone[0:2] not in ["13","14","15","17","18","19","16"]:
        return f"当前的手机号格式不正确，必须是13，15，17，18开头的手机号"
    return f"当前手机号格式正确：>>>>{phone}"
import re
def check_phone_re(phone):
    pattern="^1[3456789]\d{9}$"
    if not re.match(pattern,phone):
        return f"当前手机号格式不正确！"
    return f"当前手机号格式正确>>>>>{phone}"
phone=input("请输入手机号:>>>>")
# print(check_phone(phone))
print(check_phone_re(phone))

data="0123"
patten="[]"
print(re.findall(patten,data))

