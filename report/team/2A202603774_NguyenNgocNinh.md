# Báo cáo cá nhân — NguyenNgocNinh-2A202603774

## 1. Thông tin thành viên

- Họ tên: Nguyễn Ngọc Ninh
- MSSV: 2A202603774
- Email: sevenminutes2311@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ (TV4)

## 2. Phần việc phụ trách

- Nhiệm vụ C (CP3): gắn nhãn 20 ca lỗi độc lập với người gắn nhãn 1; tổng hợp `report/team/bang_loi.md`.
- Nhiệm vụ E3 (CP5): giữ `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

- Nhiệm vụ C: gắn 20 nhãn, trùng người 1 20/20 = 100%, 0 ca không trùng. Bộ nhãn người 1 có AI hỗ trợ nên không độc lập.
- `ho_so_launch_v0.md`: 7 mục, mỗi mục có con số, trạng thái và một vai trò phụ trách; đề xuất Go có điều kiện với 4 điều kiện có ngày kiểm tra.
- Nêu ba con số bất lợi kèm cách xử lý: power 0,64; xem lại 100% tốn 0,98–1,03× [simulated]; quoc_te 1,88× [simulated].

## 4. Bằng chứng

- File: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, báo cáo này.
- Bộ 20 nhãn của tôi: cột "Nhãn người 2" trong `bang_loi.md`; có ảnh tờ nhãn viết tay (gửi sau khi đã điền bảng), không có giờ làm (1/2 bằng chứng).
- Commit: `f04fffd` (hồ sơ launch, khung báo cáo).

## 5. Công cụ AI đã dùng

- Claude Code: đọc tài liệu của repo, chạy lại `src/lab13.py`, soạn nháp `ho_so_launch_v0.md` và báo cáo này; giải thích định nghĩa 5 loại và cách gắn bằng ví dụ ngoài 20 ca; chép nhãn vào bảng, tính đồng thuận, soạn nháp bảng khắc phục 5 ca.
- Claude Code không gắn nhãn ca nào trong 20 ca.
- Claude Code chạy lại `lab13.py`: in ĐẠT, `cps 4,472.0`, power 0,64, khớp `bang_chi_phi.md`.
- Cách tôi tự kiểm tra: Dùng Claude Code chạy `lab13.py` và lệnh python để kiểm tra: in ĐẠT, cps 4.472 đ [simulated], E1 82,83% / 27,12% / 4,25%; 890/177 = 5,03 phút [simulated]; 1.251 × 0,02 = 25,02; cột "Trùng?" có 20/20 "Có". Ba số mục 1 hồ sơ 4.472 đ, 16,3×, 92,5% [simulated] khớp `bang_chi_phi.md` (A2).

## 6. Tự đánh giá

- Đã làm được: giữ `ho_so_launch_v0.md` đủ 7 mục, mục nào cũng có con số, trạng thái và vai trò phụ trách; nêu 3 số bất lợi kèm cách xử lý (power 0,64; xem lại 100% 0,98–1,03× [simulated]; quoc_te 1,88× [simulated]); bảng khắc phục đủ 5 loại lỗi.
- Điểm yếu: tờ nhãn viết tay không ghi giờ làm và gửi sau khi đã điền bảng, nên chỉ có 1/2 bằng chứng, chưa chứng minh được nhãn của tôi gắn độc lập.
- Điểm yếu: dùng AI nhiều cho phần soạn thảo (nháp hồ sơ, báo cáo, bảng khắc phục); phần tự kiểm tra cũng chạy bằng lệnh, chưa có số nào tôi tự tính tay.
- Lần sau: gắn nhãn trên tờ có bấm giờ bắt đầu, kết thúc và chụp lại trước khi xem bảng chung; tự tính tay ít nhất 1 số (ví dụ 890/177) rồi mới so với kết quả của máy.
