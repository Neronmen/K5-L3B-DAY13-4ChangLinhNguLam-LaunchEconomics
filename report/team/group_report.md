# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: 4ChangLinhNguLam
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu cho trợ lý hoàn phí LogiX-VN trước Gate 2a: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Mọi con số do `src/lab13.py` tính từ hai file CSV giả lập; nhiệm vụ sau dùng lại số của nhiệm vụ trước.

## 3. Giải pháp

- **A · Mô hình chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): hàm `mo_hinh` cộng token + tool của mọi lần chạy, cộng phút xem lại / làm lại (simulated), chia cho số việc thành công; tách theo `loai`; cộng chi phí cố định 40 triệu đ/tháng cho phạm vi noi_dia + hang_nang.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` với 9 kịch bản, 1 cặp, giới hạn 1/2/3 lần chạy, kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): (điền sau CP3)
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): cỡ mẫu D1 tính trong `lab13.py`; (điền cách chia đã chọn sau CP4)
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): (điền sau CP5)

## 4. Kết quả

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%.
- So với nhân viên tự làm (12.000 đ): 5.865 đ/yêu cầu = 0,49× khi cộng 222 ca không thành công [simulated]; phạm vi noi_dia + hang_nang có cố định: 4.599 đ = 0,38× [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated].
- Con số bất lợi: xem lại 100% → 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated]; với 40 nhân viên không cách chia nào đủ mẫu cho mức chênh 5 điểm (power 0,64 nếu thiết kế cho 6 điểm).
- Đề xuất cuối trong `ho_so_launch_v0.md`: (điền sau CP5)
- Kết quả duyệt chéo nhận được từ hội đồng: (điền sau 17:45)

## 5. Khó khăn và cách xử lý

- Windows: tạo `.venv` trong thư mục có đường dẫn quá dài bị lỗi `ensurepip`; xử lý bằng cách tạo venv ở đường dẫn ngắn hơn rồi chạy `python -m pip install -r requirements.txt`.
- Windows console (cp1252) lỗi in tiếng Việt; thêm `sys.stdout.reconfigure(encoding='utf-8')` đầu `lab13.py`.
- (bổ sung khó khăn của các thành viên khác)

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; pilot cần đo phút thật qua event `staff_review_decision` và `staff_rework_completed`.
- Đợt chạy thử không có nhóm đối chứng nên chỉ nói "chỉ số trong đợt chạy thử là 82,83%", chưa kết luận được tác động.
- (bổ sung sau CP3–CP5)

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower` (mục `stats.power`).
- Tài liệu lab trong `docs/` của repo đề bài.
