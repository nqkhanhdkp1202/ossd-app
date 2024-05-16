
# Phần mềm Fancy App - Phần mềm nhận diện hình ảnh bằng AI

Phần mềm sẽ có một cửa sổ ứng dụng hiện lên sau khi kích hoạt ứng dụng, người dùng phần mềm có thể chọn các mục mà mình muốn sử dụng nhận dạng. Ở từng mục chức năng sẽ có những yêu cầu mà người dùng cần thực hiện đúng thì mới sử dụng được như là nhập vào hình ảnh,... Khi đã làm đúng theo các bước thì phần mềm sẽ xử lý và trả ra kết quả lên màn hình cho người xem.

Phần mềm sẽ có những chức năng chính như sau:

- Nhận dạng cảm xúc trên khuôn mặt.
- Nhận dạng các con vật.
- Nhận dạng chữ số viết tay.
- Nhận dạng giới tính.


## Hướng dẫn cài đặt
**Bước 1: Cài đặt môi trường python**
- Truy cập vào trang chủ của Python qua link sau https://www.python.org/downloads/
- Chọn phiên bản python mới nhất và thực hiện dowloads.
- Sau download hoàn tất. Chúng ta nhấn chọn chạy file python-3.12.3.exe để bắt đầu tiến trình cài đặt. Khi cài đặt sẽ có ô  Add Python.exe to PATH, hãy chọn ô đó và sau đó chọn Install Now.
- Khi cửa sổ hiển thị Setup was successful là ta đã cài đặt thành công môi trường Python > Close.

- Ta có thể kiểm tra phiên bản python bằng cách mở cmd và chạy dòng lệnh như sau:
```bash
python --version
```
**Bước 2: Cài đặt ứng dụng**

- Tải mã nguồn phần mềm tại đây: [github.com/nqkhanhdkp1202](https://github.com/nqkhanhdkp1202/ossd-app/releases/tag/v1.0)
- sau khi tải về ta thực hiện giải nén và mở file đó ở ví dụ này ta sẽ thực hiện trên
visual studio code
- Ta thực hiện dowload các model để sử dụng về trong phần mềm ở link sau: [model](https://drive.google.com/drive/folders/1ipZDhCQzeEFSN3ruRVybYqPG1uyLIryA?usp=sharing )
- Sau khi tải thành công ta thực hiện upload 5 file đó vào thư mục models của mã nguồn.
-  Sau khi thực hiện các bước trên ta sẽ mở terminal lên và nhập lệnh như sau:
```bash
python -m venv env
```
- Sau đó ta nhập tiếp lệnh:
```bash
.env\Scripts\activate
```
- trong trường hợp nếu như không thành công như hình phía trên thì ta thực hiện mở windows và nhập powershell và run as administrator. Sau đó nhập lệnh: 
```bash
Set-ExecutionPolicy RemoteSigned
```
- Khi đã thực hiện thành công các bước trên ta cần chạy thêm câu lệnh sau trong terminal:
```bash
 install tensorflow pillow
```
- Tiếp theo chạy lệnh:
```bash
pip install pyqt5
```
- Sau khi đã hoàn tất cài đặt ta sẽ nhập lệnh python 
```bash
.\src-main.py
```
- Sau bước này thì ứng dụng sẽ hiện lên và có thể sử dụng các chức năng.



