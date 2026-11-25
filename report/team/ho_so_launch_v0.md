# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: 4ChangLinhNguLam · Lớp: L3B

Số lấy từ `src/lab13.py`; chỗ tính tay ghi kèm cách tính. Nhãn [simulated] = tính từ cột `_simulated`. Trạng thái chỉ nhận: Xong, có bằng chứng · Chưa · Giả lập. Gate 2a chỉ duyệt kế hoạch pilot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** [simulated] = 4.373.585 đ / 978 việc, gấp 16,3 lần [simulated] hoá đơn token + tool (274,7 đ). Giờ nhân viên chiếm 92,5% [simulated]. ([bang_chi_phi.md](bang_chi_phi.md), A2) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Gấp đôi số ca làm lại **+51,8%**; gấp đôi tỉ lệ xem lại **+40,7%**; lương tăng 25% **+23,1%** [simulated]. Giá token gấp đôi chỉ +5,6% [simulated]. (B1, B2) | Giả lập | Kế toán trưởng |
| 3 · So với nhân viên tự làm (12.000 đ) | Toàn mẫu, cộng 222 ca không thành công: **5.865 đ/yêu cầu = 0,49×** [simulated], chưa cộng cố định. noi_dia + hang_nang, cộng cố định: **4.599 đ/việc = 0,38×** ở 45.000 yêu cầu/tháng, **0,48×** ở một nửa khối lượng [simulated], chưa cộng ca không thành công. Bất lợi: quoc_te **1,88×**; xem lại 100% **0,98–1,03×** [simulated]. (A2, A3, A4, B4) | Giả lập | Kế toán trưởng |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử là: chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200); không có đối chứng nên chưa kết luận tác động. Thiết kế 8 event có `trace_id`. ([chi_so.md](chi_so.md)) | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, cần đồng thuận ≥ 16/20; [bang_loi.md](bang_loi.md) hiện có 0/20 ca đã so nhãn, 0/5 dòng khắc phục. | Chưa | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên **20 + 20**, mde **6 điểm**, 859/nhóm, DE 6,96 (≥ 299 yêu cầu/người), 3 luật dừng, ngày quyết định **2027-01-11**. Bất lợi: tác động thật 5 điểm thì power chỉ **0,64**. ([pilot_plan.yaml](pilot_plan.yaml)) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: **6.787 đ (+51,8%)**; xem lại 100%: **11.743–12.415 đ (0,98–1,03×)**; khối lượng giảm một nửa: cố định **1.185 → 2.370 đ/việc** [simulated]. (B1, B4, A4; ba dòng rủi ro ở [chi_so.md](chi_so.md), E2) | Giả lập | Kế toán trưởng |

**Con số bất lợi và cách xử lý**

- **Power 0,64** nếu tác động thật là 5 điểm (bỏ sót khoảng 36%): 5 điểm cần n hiệu dụng 1.251, 20 nhân viên chỉ cho tối đa 1.000. Nếu ngày 2027-01-11 chưa có ý nghĩa ở alpha 0,05 thì ghi "chưa kết luận" và không mở rộng; muốn đo 5 điểm cần ≥ 26 người/nhóm (tính tay 1.251 × 0,02 = 25,02).
- **Xem lại 100% tốn 0,98–1,03×** [simulated]: chỉ hoà vốn khi mỗi lần xem lại ≤ 4,8–5,1 phút, trong khi mẫu là 5,03 phút (890/177) [simulated]. Pilot phải đo phút thật; dừng theo luật chi phí nếu > 8.000 đ/việc trong 2 tuần.
- **quoc_te 1,88×** [simulated], thành công 27,3%, lần chạy 3 chỉ ok 2,2%: loại khỏi phạm vi. doi_tac 0,85× [simulated], điều khoản riêng: cũng loại. Phạm vi còn 982/1.200 yêu cầu (81,8%).

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang, 20 + 20 nhân viên, với 4 điều kiện:

| # | Điều kiện (không đạt thì không mở rộng) | Người phụ trách | Ngày kiểm tra |
| --: | --- | --- | --- |
| 1 | Trợ lý chỉ nhận noi_dia + hang_nang; 0 yêu cầu quoc_te, doi_tac đi qua trợ lý trong bản cấu hình pilot. | Kỹ sư trưởng agent | 2026-12-04 |
| 2 | 8/8 event trong `chi_so.md` ghi được log kèm `trace_id` khi chạy thử; `bang_loi.md` có hai bộ nhãn độc lập, đồng thuận ≥ 16/20 và đủ 5 dòng khắc phục. | PM trợ lý hoàn phí | 2026-12-04 |
| 3 | Thay phút xem lại, làm lại [simulated] bằng phút đo thật; chi phí mỗi việc gồm cố định ≤ 8.000 đ. | Kế toán trưởng | 2026-12-21 |
| 4 | Đủ ≥ 299 yêu cầu/người ở cả 40 nhân viên; nhóm trợ lý mở lại cao hơn đối chứng < 2 điểm và không vượt 6%. | Giám đốc vận hành | 2027-01-11 |

**Đề xuất cuối: Go có điều kiện**
