# Báo cáo cá nhân — PhamNguyenKhoa-2A202603795

## 1. Thông tin thành viên

- Họ tên: Phạm Nguyên Khoa
- MSSV: 2A202603795
- Email:
- Vai trong nhóm: Người viết code (trước giờ giải lao), kiêm tổng hợp `TEAM.md`, `group_report.md` và push bài

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1) và B (CP2): viết `src/lab13.py`, điền `report/team/bang_chi_phi.md`.
- Tính sẵn số D1 (cỡ mẫu), tỉ lệ mở lại 7 ngày và ba chỉ số E1 trong `lab13.py` để TV2, TV3, TV4 dùng.
- Chia việc cho nhóm (`PHAN_CONG.md`), điền `TEAM.md`, `report/team/group_report.md`, kiểm checklist `SUBMISSION.md`, commit và push.

## 3. Đóng góp cụ thể

- A1: viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: viết `mo_hinh(...)`; tử số cộng token + tool của **mọi** 1.624 lần chạy (kể cả lần lỗi), mẫu số chỉ đếm 978 yêu cầu `thanh_cong` → 4.472 đ [simulated], gấp 16,3 lần hoá đơn 274,7 đ.
- A3, A4: tách theo `loai` (quoc_te 1,88× [simulated], chạy lại không giúp: ok lần 1/2/3 = 30,0% / 11,4% / 2,2%); cộng chi phí cố định cho phạm vi noi_dia + hang_nang → 4.599 đ = 0,38× [simulated].
- B1–B4: 9 kịch bản độ nhạy, cặp B2 6.543 đ (+46,3%), B3 giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ [simulated]), B4 xem lại 100% = 11.743 đ (0,98×) hoặc 12.415 đ (1,03×) [simulated].
- D1: hàm `co_mau`, `he_so_thiet_ke`; kết quả 1.251 · DE 2,48 / 3.103 · 1.000 · 300 · m ≥ 299; power ở 5 điểm với n = 859 là 0,64.

## 4. Bằng chứng

- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `PHAN_CONG.md`, `TEAM.md`.
- Commit trên nhánh `main` của repo nhóm (tác giả Neronmen).
- Output `cd src && python lab13.py`: dòng `Ba phép thử đáp án biết trước: ĐẠT`; `cps 4,472.0`; `thanh_cong 978`.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề, gợi ý code cho `mo_hinh` và `co_mau`, soát định dạng bảng markdown.
- Cách tự kiểm tra: mọi số trong `bang_chi_phi.md` lấy từ output `lab13.py`, không chép từ AI; đối chiếu với số tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch 0%); kiểm tính tuyến tính của B1 (mỗi kịch bản "giảm một nửa" bằng nửa "gấp đôi": 5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9); tính tay lại (245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.472 đ.

## 6. Tự đánh giá

- Hiểu được vì sao tử số tính mọi lần chạy (lần lỗi vẫn tốn token) còn mẫu số chỉ đếm việc thành công, và vì sao 4.472 đ chưa so thẳng được với 12.000 đ khi chưa cộng 222 ca không thành công (5.865 đ = 0,49× [simulated]).
- Điểm cần cải thiện: số phút xem lại / làm lại đều là simulated, cần thay bằng phút đo thật trong pilot.
