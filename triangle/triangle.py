import math, decimal
# Cho dau vao 3 canh, nhan xet do la tam giac gi?
def ktrDauVao(a, b, c):
    max = float(2**32)
    if type(a) is int:
        a = float(a)
    if type(b) is int:
        b = float(b)
    if type(c) is int:
        c = float(c)
    if type(a) is float and type(b) is float and type(c) is float:
        if (a > 0 and a < max) and (b > 0 and b < max) and (c > 0 and c < max):
            return 0
        else:
            return 1
    else:
        return 2
def ktrDieuKienTamGiac(a, b, c):
    if (a+b <= c) or (a+c <= b) or (b+c <= a):
        return 0
def ktrTamGiacDeu(a, b, c):
    if a == b and a == c:
        return 1
    else:
        return -1
def ktrTamGiacCan(a, b, c):
    if a == b or a == c or b == c:
        return 2
    else:
        return -1
def ktrTamGiacVuong(a, b, c):
    e = 1e-10
    tA = decimal.Decimal(a)
    tB = decimal.Decimal(b)
    tC = decimal.Decimal(c)
    if (tA**2+tB**2-tC**2)<e or (tA**2+tC**2-tB**2)<e or (tC**2+tB**2-tA**2)<e:
        return 3
    else:
        return -1

def detect_triangle(a, b, c):
    # Kiem tra dau vao
    if ktrDauVao(a, b, c) == 1:
        return "Sai mien gia tri!"
    elif ktrDauVao(a, b, c) == 2:
        return "Sai kieu gia tri!"
    else:
        pass
    if ktrDieuKienTamGiac(a, b, c) == 0:
        return "Day khong phai la tam giac!"
    elif ktrTamGiacDeu(a, b, c) == 1:
        return "Tam giac deu!"
    elif ktrTamGiacCan(a, b, c) == 2 and ktrTamGiacVuong(a, b, c) == 3:
        return "Tam giac vuong can!"
    elif ktrTamGiacCan(a, b, c) == 2:
        return "Tam giac can!"
    elif ktrTamGiacVuong(a, b, c) == 3:
        return "Tam giac vuong!"
    else:
        return "Tam giac thuong!"
