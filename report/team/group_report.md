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
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): gắn nhãn 20 ca theo năm loại Google PAIR. Bộ nhãn người 1 (TV3) đã có, nhưng có AI hỗ trợ và đối chiếu nhãn tham khảo, không phải gắn độc lập (ghi rõ trong file); bộ nhãn người 2 (TV4) gắn tay, có ảnh tờ nhãn nhưng không có giờ làm. Đồng thuận 20/20 = 100% (ngưỡng 16/20), nhưng không phải đồng thuận giữa hai bộ độc lập. Bảng khắc phục đủ 5 loại (ca 1, 20, 18, 19, 17), mỗi dòng có event + ngưỡng + tần suất và một vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): cỡ mẫu D1 tính trong `lab13.py` (1.251 · DE 2,48 / 3.103 · 1.000 · 300 · m ≥ 299). Chọn chia ngẫu nhiên theo nhân viên 20 + 20, phân tầng theo depot, chấp nhận mde 6 điểm (859/nhóm, DE 6,96); ba luật dừng an toàn, chi phí, sử dụng đủ NẾU – TRONG – THÌ – KHÔNG THÌ; ngày quyết định 2027-01-11.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số tính thử, hai chỉ số tự đề xuất, 8 event có `trace_id` kèm kiểm tra chéo, 3 dòng rủi ro kinh tế; hồ sơ một trang đủ 7 mục, nêu con số bất lợi và cách xử lý.

## 4. Kết quả

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5%.
- So với nhân viên tự làm (12.000 đ): 5.865 đ/yêu cầu = 0,49× khi cộng 222 ca không thành công [simulated]; phạm vi noi_dia + hang_nang có cố định: 4.599 đ = 0,38× [simulated].
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated].
- Con số bất lợi: xem lại 100% → 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated]; với 40 nhân viên không cách chia nào đủ mẫu cho mức chênh 5 điểm (power 0,64 nếu thiết kế cho 6 điểm).
- Chỉ số trong đợt chạy thử là: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); chưa có đối chứng nên chưa kết luận tác động.
- Pilot: 20 + 20 nhân viên, mde 6 điểm, power chỉ 0,64 nếu tác động thật là 5 điểm.
- Đề xuất cuối trong `ho_so_launch_v0.md`: **Go có điều kiện** cho pilot noi_dia + hang_nang, 4 điều kiện có người phụ trách và ngày kiểm tra.
- Kết quả duyệt chéo nhận được từ hội đồng: (ghi điểm và quyết định nhóm hội đồng chấm nhóm mình)

## 5. Khó khăn và cách xử lý

- Windows: tạo `.venv` trong thư mục có đường dẫn quá dài bị lỗi `ensurepip`; xử lý bằng cách tạo venv ở đường dẫn ngắn hơn rồi chạy `python -m pip install -r requirements.txt`.
- Windows console (cp1252) lỗi in tiếng Việt; thêm `sys.stdout.reconfigure(encoding='utf-8')` đầu `lab13.py`.
- TV3 dùng AI hỗ trợ và đối chiếu nhãn tham khảo khi gắn bộ nhãn 1, nên bộ nhãn này không đạt yêu cầu gắn độc lập. Nhóm giữ nguyên bộ nhãn, ghi rõ nguồn trong `bang_loi.md`, sẽ báo coach để thống nhất cách xử lý; TV4 gắn bộ nhãn 2 độc lập, không dùng AI.
- TV3 làm trên nhánh riêng `feature/gannhan1`; TV1 merge vào `main` (không conflict).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; pilot cần đo phút thật qua event `staff_review_decision` và `staff_rework_completed`.
- Đợt chạy thử không có nhóm đối chứng nên chỉ nói "chỉ số trong đợt chạy thử là 82,83%", chưa kết luận được tác động.
- Bộ nhãn 1 của nhiệm vụ C không độc lập; lần sau hai người gắn nhãn phải gắn trên giấy trước khi dùng bất kỳ công cụ nào.
- Pilot 20 + 20 chỉ đủ mẫu cho mức chênh 6 điểm; muốn đo 5 điểm cần ít nhất 26 nhân viên mỗi nhóm (tổng 52 > 40).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower` (mục `stats.power`).
- Tài liệu lab trong `docs/` của repo đề bài.
