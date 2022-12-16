from student3 import SinhVien2
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, objs: list[SinhVien2]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_taptin: str) -> list[SinhVien2]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_sinhvien(content: list[SinhVien2]):
    for item in content:
        print(item)

def main():
    path = '/Users/trung/PycharmProjects/pythonProject'
    filename = 'sinhvien3.dat'
    sv3 = [SinhVien2('Thanh Duc', 2003, 10.0),
           SinhVien2('Thanh Thao', 2004, 12.0),
           SinhVien2('Quynh Anh', 2004, 3.0)]
    ghi_sinhvien(path, filename, sv3)
    noidung = doc_sinhvien(path, filename)
    in_list_sinhvien(noidung)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()