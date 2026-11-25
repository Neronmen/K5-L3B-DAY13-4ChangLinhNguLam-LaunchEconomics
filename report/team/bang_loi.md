# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Nhãn tham khảo cho 20 ca

Đối chiếu mô tả tại mục **Hai mươi ca lỗi** trong đề gốc với mục **Nhãn tham khảo cho 20 ca** trong [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md#nhãn-tham-khảo-cho-20-ca). Đây là bộ nhãn tham khảo do AI hỗ trợ tổng hợp, chưa phải kết quả hai người gắn độc lập hay nhãn thống nhất của nhóm.

| Ca | Tình huống tóm tắt | Nhãn tham khảo | Lý do phân loại |
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

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| ... | Do người dùng | ... | ... | ... |
| ... | Hệ thống | ... | ... | ... |
| ... | Ngữ cảnh | ... | ... | ... |
| ... | Giới hạn hệ thống | ... | ... | ... |
| ... | Ngầm | ... | ... | ... |
