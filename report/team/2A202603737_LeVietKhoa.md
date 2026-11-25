# Báo cáo cá nhân — LeVietKhoa-2A202603737

## 1. Thông tin thành viên

- Họ tên: Lê Viết Khoa
- MSSV: 2A202603737
- Email: 26ai.khoalv2@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1 (TV3).

## 2. Phần việc phụ trách

- Nhiệm vụ C: phụ trách bộ nhãn 1 cho 20 ca; cùng TV4 so nhãn, giải thích ca khác nhau và hỗ trợ chọn cách khắc phục cho 5 loại lỗi.
- Nhiệm vụ E1–E2: hoàn thiện `chi_so.md`, gồm 5 chỉ số, 8 event có `trace_id`, kiểm tra chéo chỉ số với event và 3 rủi ro kinh tế.

## 3. Đóng góp cụ thể

- Với hỗ trợ của Codex, rà soát E1 theo output thật của `lab13.py`: Chính **82,83% (994/1.200)**, Dùng **27,12% (48/177)**, An toàn **4,25% (51/1.200)**.
- Đề xuất thêm 2 công thức: tỉ lệ mở xem gợi ý theo yêu cầu trong nhóm trợ lý và tỉ lệ hoàn trùng/sai tiền qua đối soát 7 ngày; chưa có số đo cho 2 chỉ số này.
- Hoàn thiện 8 event: bổ sung nhóm phân bổ ở `request_received`, thời điểm nhận/đóng/mở lại, đối soát hoàn tiền; đếm yêu cầu duy nhất để tránh tính lặp khi chạy 2–3 lần.
- Rà soát 3 rủi ro theo A4, B1–B4: làm lại ×2 → **6.787 đ (+51,8%) [simulated]**; xem lại 100% → **11.743–12.415 đ [simulated]**; nửa khối lượng → **2.370 đ cố định/việc**.
- Phần C: chọn sử dụng 20 nhãn có AI hỗ trợ và đã đối chiếu đề, hướng dẫn; điền bộ nhãn của TV3 vào cột người 1 để TV4 so sau. Chưa xác nhận quy trình 8 phút gắn độc lập.

## 4. Bằng chứng

- File phụ trách: [chi_so.md](chi_so.md), bảng 5 chỉ số, danh sách 8 event và bảng 3 rủi ro; nguồn số chi phí: [bang_chi_phi.md](bang_chi_phi.md), A4 và B1–B4.
- Codex đã chạy `python -B lab13.py` trong `src/` với thư viện ở thư mục tạm: 3 phép thử A1 ĐẠT, chạy hết chương trình; 3 dòng E1 khớp bảng chỉ số.
- Codex đã kiểm đếm độc lập bằng thư viện CSV của Python: **994 / 1.200 × 100 = 82,83%**; **48 / 177 × 100 = 27,12%**; **51 / 1.200 × 100 = 4,25%**, khớp cả 3 dòng output của `lab13.py`.
- Chi phí cố định khi nửa khối lượng: **40.000.000 / 16.875 = 2.370,37 đ/việc**, làm tròn 2.370 đ; tổng **5.784 đ/việc [simulated]** khi cộng chi phí biến đổi A4.
- Codex đã kiểm tra bảng gốc đủ 20 ca và đối chiếu nhãn hiện có: **20/20** khớp hướng dẫn; đây là mức khớp nhãn tham khảo, chưa phải đồng thuận giữa TV3 và TV4.
- Bằng chứng C: [bang_loi.md](bang_loi.md) có 20 nhãn TV3 chọn sử dụng, kèm lý do và nguồn AI hỗ trợ; đang chờ nhãn TV4, kết quả so nhãn và tỉ lệ đồng thuận trên nhánh `feature/gannhan1`.

## 5. Công cụ AI đã dùng

- Công cụ: Codex (ChatGPT), hỗ trợ đọc 20 ca trong đề gốc, tổng hợp nhãn tham khảo kèm lý do từ hướng dẫn; không tạo bằng chứng gắn độc lập hoặc tỉ lệ đồng thuận.
- Ở E1–E2, Codex đọc phân công và tài liệu, chạy code lấy 3 chỉ số thật, rà số với bảng chi phí, sửa công thức/event/ngưỡng theo dõi và soạn báo cáo cá nhân theo mẫu.
- Môi trường ban đầu thiếu `pandas`; Codex cài thư viện vào thư mục tạm rồi chạy code, không sửa mã nguồn hoặc 2 CSV.
- Kiểm tra kỹ thuật đã thực hiện bằng Codex: chạy lại `lab13.py`, kiểm đếm độc lập 3 tỉ lệ từ CSV, đối chiếu 20 nhãn tham khảo và xác nhận mã SHA256 của 2 CSV không đổi.
- Cách tự kiểm tra người học còn cần thực hiện: tính tay 3 tỉ lệ ở mục 4, giải thích công thức và kiểm tra 3 rủi ro với A4/B1/B3/B4; không coi lượt chạy của Codex là xác nhận người học đã tự chạy.
- Với C, người học chọn sử dụng bộ 20 nhãn do AI hỗ trợ; giữ rõ nguồn tham khảo và tự giải thích nguyên nhân gốc. Việc chọn bộ nhãn không xác nhận đã thực hiện 8 phút gắn độc lập.

## 6. Tự đánh giá

- E1–E2 đã có bản hoàn thiện để tự kiểm tra: 5 chỉ số, 8 event và 3 rủi ro; kết quả trong đợt chạy thử chưa chứng minh tác động vì chưa có đối chứng.
- [x] Kiểm tra kỹ thuật bằng Codex: chương trình chạy hết, 3 phép thử A1 ĐẠT và 3 tỉ lệ E1 khớp kiểm đếm độc lập từ CSV.
- [ ] Tự giải thích cách tính 3 chỉ số từ event và số bất lợi **12.415 đ = 1,03× [simulated]** của B4.
- [x] Chọn bộ 20 nhãn có AI hỗ trợ làm bộ nhãn TV3 để đối chiếu và điền cột người 1 trong `bang_loi.md`.
- [ ] Hoàn tất C với TV4: nhận đủ 20 nhãn người 2, tính đồng thuận = số ca trùng / 20 × 100, mục tiêu ít nhất **16/20 = 80%**; giải thích ca khác và góp ý bảng khắc phục 5 loại.
- [ ] Nếu chưa có bộ nhãn độc lập từ trước khi xem tham khảo, báo giảng viên để thống nhất cách xử lý yêu cầu 8 phút độc lập; không dựng lại bằng chứng hoặc sửa nhãn gốc sau khi so.
- [x] Bổ sung email **26ai.khoalv2@vinuni.edu.vn** do người học cung cấp cho TV3 (2A202603737).
- [x] Cập nhật thông tin và đóng góp TV3 (2A202603737) trong `TEAM.md`; phần việc được lưu trên nhánh `feature/gannhan1`, tra commit bằng `git log -1 -- TEAM.md report/team/2A202603737_LeVietKhoa.md`.
- [ ] Gửi TV4 kết quả E1–E2 để ghép 7 mục hồ sơ và cùng hoàn tất đối chiếu 20 nhãn.
- [ ] Tự nộp link repo nhóm trên LMS trước **23h59 GMT+7 ngày lab**, theo `SUBMISSION.md`.
