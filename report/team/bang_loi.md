# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Bộ nhãn TV3 chọn sử dụng cho 20 ca

TV3, Lê Viết Khoa (2A202603737), chọn sử dụng bộ 20 nhãn dưới đây để so với TV4. Bộ nhãn có AI hỗ trợ, đã đối chiếu đề gốc và [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca); chưa xác nhận quy trình 8 phút gắn độc lập và chưa phải nhãn thống nhất của nhóm.

| Ca | Tình huống tóm tắt | Nhãn TV3 chọn | Lý do phân loại |
| --: | --- | --- | --- |
| 1 | Số tài khoản thiếu hai chữ số, ngân hàng từ chối lệnh hoàn | Do người dùng | Khách nhập sai thông tin tài khoản; bổ sung kiểm tra đầu vào là cách khắc phục. |
| 2 | Kiện 28 kg bị tra theo hàng thường, hoàn thiếu 45.000 đ | Hệ thống | Trợ lý gọi tool sai loại hàng, dẫn đến hoàn sai tiền và khách mở lại yêu cầu. |
| 3 | Hoàn về ví LogiX đúng thiết kế nhưng khách chờ tiền về ngân hàng | Ngữ cảnh | Nơi nhận tiền đúng thiết kế nhưng không khớp kỳ vọng của khách. |
| 4 | Không có dữ liệu chặng hãng nước ngoài, chuyển nhân viên | Giới hạn hệ thống | Thiếu dữ liệu cần thiết để xác định trạng thái chặng giao. |
| 5 | Kiểm tra mẫu phát hiện 14 đơn hoàn theo giá trước giảm | Ngầm | Hoàn thừa nhưng không khách nào báo và không cảnh báo nào kích hoạt; chỉ kiểm tra mẫu mới phát hiện. |
| 6 | Khách chọn giao trễ nhưng mô tả hàng bị vỡ | Do người dùng | Nguyên nhân gốc là khách chọn sai mục yêu cầu, dù trợ lý cần kiểm tra mâu thuẫn với mô tả. |
| 7 | Sổ cái lỗi 503 sau 3 lần thử, vẫn báo hoàn thành công | Hệ thống | Trợ lý báo thành công khi bước ghi hoàn tiền chưa thành công. |
| 8 | Dẫn điều 7.2 không tồn tại, số tiền vẫn đúng | Hệ thống | Trích dẫn chính sách sai là lỗi đầu ra nhìn thấy được, dù số tiền hoàn đúng. |
| 9 | Khách nhập mã đơn sàn thay vì mã vận đơn | Do người dùng | Khách cung cấp sai loại mã; việc không gợi ý cách sửa thuộc phần khắc phục. |
| 10 | Từ chối vì bão đúng chính sách nhưng ứng dụng cam kết giao 24 giờ | Ngữ cảnh | Quyết định đúng chính sách nhưng thông điệp trên ứng dụng tạo kỳ vọng khác cho khách. |
| 11 | Không xử lý được tin nhắn thoại 40 giây | Giới hạn hệ thống | Âm thanh là dạng đầu vào trợ lý chưa hỗ trợ. |
| 12 | Kết quả đúng nhưng token D05 gấp 3 lần suốt 3 tuần | Ngầm | Chi phí bất thường kéo dài mà không ai phát hiện; lỗi nằm ở chi phí dù câu trả lời đúng. |
| 13 | Hỏi phí bảo hiểm đối tác ngoài phạm vi, trợ lý trả lời chung chung | Giới hạn hệ thống | Yêu cầu nằm ngoài phạm vi trợ lý; cách thông báo giới hạn chưa rõ là việc cần sửa. |
| 14 | Khách bấm nhầm xác nhận đã nhận tiền, yêu cầu bị đóng | Do người dùng | Thao tác xác nhận nhầm của khách gây đóng yêu cầu. |
| 15 | Trễ 26 giờ phải hoàn 50% nhưng trợ lý tính 100%, nhân viên bắt được | Hệ thống | Trợ lý tính sai chính sách và lỗi đã được nhân viên phát hiện khi xem lại. |
| 16 | Gửi Zalo lúc 2:14 sáng theo thiết kế gửi ngay khi xong | Ngữ cảnh | Hành vi đúng thiết kế nhưng không phù hợp giờ nghỉ của khách. |
| 17 | Dùng bảng giá cũ cho 212 đơn trong 9 ngày, không ai mở lại | Ngầm | Sai tiền do bộ nhớ đệm cũ diễn ra kéo dài mà không ai nhận ra. |
| 18 | Hoàn đúng 15.000 đ nhưng không giải thích cách tính 50% | Ngữ cảnh | Số tiền đúng chính sách nhưng giả định khách tự hiểu cách tính không phù hợp. |
| 19 | Đơn từ 14 tháng trước, chỉ truy cập được dữ liệu 12 tháng | Giới hạn hệ thống | Yêu cầu vượt phạm vi dữ liệu có thể truy cập; trợ lý đã giải thích và chuyển nhân viên. |
| 20 | Khách gửi lại yêu cầu, trợ lý hoàn hai lần vì thiếu khóa chống trùng | Hệ thống | Hệ thống thiếu cơ chế chống xử lý trùng cho cùng một đơn; khách gửi lại không phải nguyên nhân gốc. |

**Phân bố nhãn:** Do người dùng 4 ca (1, 6, 9, 14); Hệ thống 5 ca (2, 7, 8, 15, 20); Ngữ cảnh 4 ca (3, 10, 16, 18); Giới hạn hệ thống 4 ca (4, 11, 13, 19); Ngầm 3 ca (5, 12, 17). Tổng: **20 ca**.

## Bảng so nhãn TV3–TV4

Người gắn nhãn 1: **Lê Viết Khoa (2A202603737)**, bộ 20 nhãn có AI hỗ trợ và đã đối chiếu tham khảo. Người gắn nhãn 2: **Nguyễn Ngọc Ninh (2A202603774)**, theo lời khai chưa xem nhãn người 1 trước khi gắn; có ảnh tờ nhãn viết tay (khớp 20/20 ca, gửi sau khi đã điền bảng), không có giờ làm, nên chưa chứng minh được tính độc lập.

| Ca | Nhãn người 1 (có AI hỗ trợ) | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận: 20 / 20 = 100%.** Bộ nhãn người 1 có AI hỗ trợ và đã đối chiếu bảng tham khảo, nên 20/20 không phải đồng thuận giữa hai bộ nhãn độc lập.

## Quy tắc phân biệt cho các ca không trùng

Đồng thuận 20/20, ngưỡng 16/20.

- Không có ca nào không trùng (0/20), nên không cần quy tắc phân biệt; đồng thuận trên mức 16/20 nên không viết lại định nghĩa.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò. Các ngưỡng là đề xuất cho pilot, chưa đo.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `request_reopened` có `reopen_reason = sai_tai_khoan_nhan` (nối `trace_id`): ≥ 3 ca/tuần thì cảnh báo, rà 1 lần/tuần. | Form chặn số tài khoản sai độ dài theo ngân hàng trước khi tạo lệnh; hiện lại số để khách xác nhận 1 lần; lệnh bị trả về thì nhắn khách sửa trong 1 giờ. | PM trợ lý hoàn phí |
| 20 | Hệ thống | `refund_audit_completed` có `duplicate_refund_flag = true` (nối `trace_id`): ≥ 1 ca thì cảnh báo ngay, đối soát 1 lần/ngày. | Thêm khoá chống trùng theo mã vận đơn cho lệnh hoàn (gửi lại tạo `request_id` mới nên không khoá theo trường này); có 1 ca thì áp dụng luật dừng an toàn (tắt trợ lý trong 30 phút) và thu hồi khoản thừa. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | `request_reopened` có `reopen_reason = khong_hieu_cach_tinh` (nối `trace_id`): > 10% số ca mở lại trong tuần, rà 1 lần/tuần. | Mẫu tin nhắn bắt buộc đủ 3 phần: phí giao 30.000 đ, tỉ lệ 50%, số hoàn 15.000 đ; kèm liên kết điều khoản. | PM trợ lý hoàn phí |
| 19 | Giới hạn hệ thống | `request_closed` có `ket_qua = chuyen_nhan_vien` (nối `trace_id`), lý do đơn quá 12 tháng: > 2% yêu cầu/tuần, rà 1 lần/tuần. | Kiểm tra ngày đơn khi tiếp nhận; đơn quá 12 tháng chuyển thẳng nhân viên kèm tóm tắt, 0 lần chạy agent; báo khách hạn xử lý 24 giờ. | Trưởng nhóm CSKH |
| 17 | Ngầm | `refund_audit_completed` có `wrong_amount_flag = true` hoặc `policy_version` khác bản hiện hành (nối `trace_id`): ≥ 1 ca/ngày, đối soát 1 lần/ngày. | Xoá bộ nhớ đệm bảng giá ngay khi đổi bản và đặt hạn lưu 24 giờ; rà lại 212 đơn trong 9 ngày, hoàn bù chênh 1.000–2.000 đ/đơn. | Kế toán trưởng |
