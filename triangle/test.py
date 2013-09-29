import math, unittest
from triangle import detect_triangle

class TestDetectTriangle(unittest.TestCase):
    # ----------------- Kiem thu gia tri dau vao ----------------------
    # Kiem thu kieu gia tri
    def testKieuGiaTri1(self):
        kq=detect_triangle('a', 1.0, 2.0)
        self.assertMultiLineEqual(kq, 'Sai kieu gia tri!', 'OK!')

    def testKieuGiaTri2(self):
        kq=detect_triangle(1.0, 'a', 2.0)
        self.assertMultiLineEqual(kq, 'Sai kieu gia tri!', 'OK!')

    def testKieuGiaTri3(self):
        kq=detect_triangle(1.0, 1.0, 'a')
        self.assertMultiLineEqual(kq, 'Sai kieu gia tri!', 'OK!')
    
    # Kiem thu gia tri bien duoi
    def testGiaTriBienDuoi1(self):
        kq=detect_triangle(0.0, 2.0, 3.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    def testGiaTriBienDuoi2(self):
        kq=detect_triangle(0.0, 0.0, 3.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    def testGiaTriBienDuoi3(self):
        kq=detect_triangle(0.0, 0.0, 0.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    # Kiem thu gia tri bien tren
    def testGiaTriBienTren1(self):
        kq=detect_triangle(2.0**32, 2.0**32-1, 2.0**32-5)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    def testGiaTriBienTren2(self):
        kq=detect_triangle(2.0**32, 2.0**32, 2.0**32-5)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    def testGiaTriBienTren3(self):
        kq=detect_triangle(2.0**32, 2.0**32, 2.0**32)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    # Kiem thu gia tri ngoai bien
    def testGiaTriNgoaiBien1(self):
        kq=detect_triangle(2.0**32+1, 2.0, 6.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien2(self):
        kq=detect_triangle(2.0, 2.0**32+40, 6.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien3(self):
        kq=detect_triangle(2.0, 5.0, 2.0**32+2.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien4(self):
        kq=detect_triangle(2.0, 2.0**32-1, -1.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien5(self):
        kq=detect_triangle(2.0, -1.0, 5.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien6(self):
        kq=detect_triangle(-2.0, 2.0, 7.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien7(self):
        kq=detect_triangle(2.0**32+1, -2.0, 6.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien8(self):
        kq=detect_triangle(2.0**32+5, 2.0, -6.0)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    def testGiaTriNgoaiBien9(self):
        kq=detect_triangle(-2.0, -2.0, 2.0**33)
        self.assertMultiLineEqual(kq, 'Sai mien gia tri!', 'OK!')
    
    # ------------------ Kiem thu tam giac ----------------------------
    # Kiem thu tam giac deu
    
    def testTamGiacDeu(self):
        kq=detect_triangle(6.0, 6.0, 6.0)
        self.assertMultiLineEqual(kq, 'Tam giac deu!', 'OK!')
    
    # Kiem thu tam giac vuong can
    def testTamGiacVuongCan1(self):
        kq=detect_triangle(2.0, 2.0, math.sqrt(8.0))
        self.assertMultiLineEqual(kq, 'Tam giac vuong can!', 'OK!')
    
    def testTamGiacVuongCan2(self):
        kq=detect_triangle(math.sqrt(8.0), 2.0, 2.0)
        self.assertMultiLineEqual(kq, 'Tam giac vuong can!', 'OK!')
    
    def testTamGiacVuongCan3(self):
        kq=detect_triangle(2.0, math.sqrt(8.0), 2.0)
        self.assertMultiLineEqual(kq, 'Tam giac vuong can!', 'OK!')
    
    # Kiem thu tam giac vuong
    def testTamGiacVuong1(self):
        kq=detect_triangle(3.0, 4.0, 5.0)
        self.assertMultiLineEqual(kq, 'Tam giac vuong!', 'OK!')
    
    def testTamGiacVuong2(self):
        kq=detect_triangle(4.0, 5.0, 3.0)
        self.assertMultiLineEqual(kq, 'Tam giac vuong!', 'OK!')
    
    def testTamGiacVuong3(self):
        kq=detect_triangle(5.0, 4.0, 3.0)
        self.assertMultiLineEqual(kq, 'Tam giac vuong!', 'OK!')
    
    # Kiem thu tam giac can
    def testTamGiacCan1(self):
        kq=detect_triangle(3.0, 3.0, 2.0)
        self.assertMultiLineEqual(kq, 'Tam giac can!', 'OK!')

    def testTamGiacCan2(self):
        kq=detect_triangle(3.0, 2.0, 3.0)
        self.assertMultiLineEqual(kq, 'Tam giac can!', 'OK!')

    def testTamGiacCan3(self):
        kq=detect_triangle(2.0, 3.0, 3.0)
        self.assertMultiLineEqual(kq, 'Tam giac can!', 'OK!')

    def testTamGiacCan4(self):
        kq=detect_triangle(2.0**32-1, 1.0, 2.0**32-1)
        self.assertMultiLineEqual(kq, 'Tam giac can!', 'OK!')

    def testTamGiacCan5(self):
        kq=detect_triangle(1.0, 2.0**32-1, 2.0**32-1)
        self.assertMultiLineEqual(kq, 'Tam giac can!', 'OK!')

    def testTamGiacCan6(self):
        kq=detect_triangle(2.0**32-1, 2.0**32-1, 1.0)
        self.assertMultiLineEqual(kq, 'Tam giac can!', 'OK!')

    # Kiem thu tam giac thuong
    def testTamGiacThuong(self):
        kq=detect_triangle(4.0, 5.0, 6.0)
        self.assertMultiLineEqual(kq, 'Tam giac thuong!', 'OK!')

def main():
    unittest.main()
if __name__ == "__main__":
    main()
    
