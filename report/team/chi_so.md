# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Nguồn tính thử: chạy `python lab13.py` trong `src/`, đối chiếu mục E1 với 1.200 yêu cầu trong CSV; dữ liệu của lab là giả lập.

Output E1 thực tế của lần chạy kiểm tra:

```text
Chính  : 82.83% (994/1200)
Dùng   : 27.12% (48/177)
An toàn: 4.25% (51/1200)
```

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | 100 × số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | 100 × số yêu cầu có `duoc_xem_lai = 1` và quyết định `sua` hoặc `bo` / số yêu cầu có `duoc_xem_lai = 1` | **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách, đo bằng yêu cầu mở lại trong 7 ngày | 100 × số yêu cầu có `mo_lai_trong_7_ngay = 1` / tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng (tự đề xuất) | Tỉ lệ mở xem gợi ý trong phạm vi pilot | 100 × số `request_id` duy nhất có `assistant_opened` / số `request_id` duy nhất có `request_received`; cả 2 vế lọc `group_arm = assistant`, loại `noi_dia` hoặc `hang_nang` | Chỉ đề xuất công thức, chưa tính |
| An toàn (tự đề xuất) | Tỉ lệ yêu cầu có hoàn trùng hoặc sai tiền qua đối soát 7 ngày | 100 × số `request_id` duy nhất có `duplicate_refund_flag = true` hoặc `wrong_amount_flag = true` trong đối soát 7 ngày từ lượt chạy đầu / số `request_id` duy nhất có `agent_run_finished` và đã đối soát đủ 7 ngày | Chỉ đề xuất công thức, chưa tính |

Chỉ số trong đợt chạy thử là: Chính **82,83%** (994/1.200), Dùng **27,12%** (48/177), An toàn **4,25%** (51/1.200); chưa có nhóm đối chứng để kết luận tác động của trợ lý.

Ba chỉ số E1 không dùng 2 cột `_simulated`; chỉ số mở lại 7 ngày là đại diện an toàn theo đề, có thể bỏ sót hoàn sai tiền mà khách không báo.

## Danh sách event

Đề xuất 8 event; mỗi event có `event_id`, `occurred_at`, `request_id`, `trace_id`. Đây là thiết kế ghi log cho pilot, chưa phải event đã thu trong 2 CSV.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_received` | Hệ thống CSKH | `request_id, depot, staff_id, group_arm, loai, so_tien_vnd, received_at, trace_id` | Khi tiếp nhận yêu cầu và ghi nhóm phân bổ của nhân viên |
| `assistant_opened` | Giao diện trợ lý CSKH | `request_id, staff_id, group_arm, trace_id` | Khi nhân viên mở xem gợi ý của trợ lý |
| `agent_run_finished` | Agent hoàn phí | `request_id, run_id, attempt, status, tokens_in, tokens_out, tool_calls, trace_id` | Khi kết thúc mỗi lần chạy của agent |
| `staff_review_decision` | Giao diện CSKH | `request_id, staff_id, duoc_xem_lai, quyet_dinh_xem_lai, review_duration_sec, trace_id` | Khi nhân viên chốt `giu`, `sua` hoặc `bo` gợi ý |
| `request_closed` | Hệ thống CSKH | `request_id, staff_id, ket_qua, dong_trong_24h, closed_at, trace_id` | Khi yêu cầu hoàn phí được đóng |
| `request_reopened` | Hệ thống CSKH | `request_id, reopen_reason, reopened_at, closed_at, reopened_within_7d, trace_id` | Mỗi lần mở lại; đánh dấu có nằm trong 7 ngày từ lần đóng được đánh giá hay không |
| `staff_rework_completed` | Hệ thống CSKH | `request_id, staff_id, rework_reason, rework_duration_sec, trace_id` | Khi nhân viên hoàn tất xử lý lại 1 yêu cầu |
| `refund_audit_completed` | Hệ thống đối soát kế toán | `request_id, transaction_ids, first_run_at, audit_window_end, audit_complete, actual_amount_vnd, expected_amount_vnd, policy_version, duplicate_refund_flag, wrong_amount_flag, trace_id` | Đối soát sổ cái và chính sách 1 lần/ngày; chốt `audit_complete = true` sau đủ 7 ngày từ lượt chạy đầu |

Nối theo `request_id` để gom mọi lần chạy; dùng `trace_id` để truy vết từng lần chạy, tránh bỏ sót lần thử thứ 2–3. Loại event trùng bằng `event_id`, mỗi yêu cầu chỉ đếm 1 lần trong mỗi vế của tỉ lệ.

### Kiểm tra chéo 5 chỉ số với event

| Chỉ số | Event và cách tính |
| --- | --- |
| Chính | Mẫu số: `request_received`; tử số: yêu cầu có `request_closed` trong 24 giờ từ `received_at` và không có `request_reopened` trong 7 ngày từ lần đóng đó. |
| Dùng | `staff_review_decision`: lấy quyết định cuối cùng cho mỗi yêu cầu có `duoc_xem_lai = 1`; số quyết định `sua` hoặc `bo` chia tổng số yêu cầu được xem lại. |
| An toàn | Số yêu cầu có `request_reopened` với `reopened_within_7d = true` chia tổng yêu cầu từ `request_received`; chỉ đếm 1 lần nếu mở lại nhiều lần. |
| Dùng tự đề xuất | `assistant_opened` / `request_received`, nối theo `request_id`, lọc cùng nhóm `assistant` và 2 loại `noi_dia`, `hang_nang`; đếm yêu cầu duy nhất ở cả 2 vế. |
| An toàn tự đề xuất | Từ `agent_run_finished`, lấy yêu cầu đã có `refund_audit_completed.audit_complete = true` sau 7 ngày; tử số là các yêu cầu trong chính mẫu số có ít nhất 1 cờ hoàn trùng/sai tiền. |

Chỉ chốt chỉ số Chính sau 24 giờ xử lý và đủ 7 ngày theo dõi các ca đóng trong hạn; ca không đóng trong 24 giờ vẫn ở mẫu số và không đạt tử số. Chỉ số An toàn chờ đủ 7 ngày sau đóng; báo riêng ca chưa đóng/chưa đủ thời gian theo dõi.

Với chỉ số An toàn mới, báo riêng số ca chưa đối soát đủ 7 ngày; mẫu số chỉ gồm ca có `audit_complete = true`, không coi thiếu đối soát là không có lỗi.

Đo thời gian thật: phút xem lại = `review_duration_sec / 60`, phút làm lại = `rework_duration_sec / 60`; lấy từ 2 event tương ứng, thay cho phút `_simulated` khi chạy pilot.

## E2 · Rủi ro kinh tế

Số tác động lấy từ [bảng chi phí](bang_chi_phi.md), mục A4 và B1–B4; 3 ngưỡng vận hành dưới đây là đề xuất. Các đại lượng phụ thuộc thời gian `_simulated` đều ghi `[simulated]`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1, toàn mẫu 1.200 yêu cầu: **4.472 đ → 6.787 đ (+51,8%) [simulated]**, giữ nguyên thời gian làm lại trung bình và các yếu tố khác. | Theo tuần, trong 2 loại thuộc pilot: số yêu cầu `lam_lai` / tổng yêu cầu > **48/982 = 4,89%**; hoặc trung bình `rework_duration_sec / 60` > **15,3 phút [simulated]**, ngưỡng tham chiếu từ toàn mẫu. | Trong 1 ngày sau cảnh báo, kiểm tra nguyên nhân và tăng xem lại có mục tiêu với `hang_nang`; đề xuất tối đa 2 lần chạy, căn cứ B3 cả hệ thống **6.901.220 đ [simulated]** trên toàn mẫu. | Kỹ sư trưởng agent |
| Xem lại 100% ở phạm vi `noi_dia` + `hang_nang` | B4: làm lại 9 phút/ca → **11.743 đ = 0,98× [simulated]**; làm lại **15,3 phút/ca [simulated]** → **12.415 đ = 1,03× [simulated]** so với 12.000 đ; chưa cộng cố định. | Theo tuần, trung bình `review_duration_sec / 60` > **4,8 phút [simulated]**; đây là ngưỡng hòa vốn thận trọng, khoảng **4,8–5,1 phút [simulated]** tùy thời gian làm lại. | Đơn giản hóa thao tác xem lại; nếu chi phí thực tế gồm cố định > **8.000 đ/việc trong 2 tuần liên tiếp**, thu hẹp về `noi_dia` và tối đa 2 lần chạy theo kế hoạch pilot. | PM trợ lý hoàn phí |
| Khối lượng chỉ đạt một nửa quy mô: 22.500 yêu cầu/tháng | A4: **40.000.000 / 16.875 = 2.370 đ cố định/việc**, so với 1.185 đ khi đủ quy mô; cộng chi phí biến đổi → **5.784 đ = 0,48× [simulated]** của 12.000 đ. | Theo tháng, số việc thành công trong phạm vi pilot < **17.000**, hoặc **40.000.000 / số việc thành công > 2.500 đ/việc**; tháng không có việc thành công thì cảnh báo ngay. | Giữ nguyên mức đầu tư cố định; trong 1 kỳ rà soát tháng, kiểm tra lượng yêu cầu thực nhận và tối ưu khoản cố định trước khi đề nghị mở rộng. | Giám đốc vận hành LogiX-VN |

Theo dõi bằng event: làm lại từ `request_closed` và `staff_rework_completed`; xem lại từ `staff_review_decision`; số việc thành công từ nhóm event Chính kèm đối soát sai tiền. Chi phí thực tế cộng token/tool, 2 loại thời gian nhân viên và cố định; kế toán xác nhận cố định mỗi tháng.
