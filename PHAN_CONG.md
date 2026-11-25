# Phân công Lab 13 · Nhóm 4ChangLinhNguLam

File nội bộ để cả nhóm làm nối tiếp nhau. Số liệu lấy từ output `cd src && python lab13.py` (đã chạy, khớp đáp án tham khảo).

## Thứ tự làm (ai xong thì báo người kế)

Thứ tự trong đề: **A → B → C (bảng lỗi) → D (pilot) → E (chỉ số, hồ sơ)**. A, B đã xong. C và D **không phụ thuộc nhau** (D chỉ cần số D1 đã tính sẵn), nên TV2 làm D song song lúc TV3 + TV4 gắn nhãn C. E (chi_so) chỉ cần số của A, B; riêng `ho_so_launch_v0.md` phải chờ C và D xong mới chốt.

```
TV1 code A·B·D1 (XONG) ──► TV2 pilot_plan.yaml (D)
                       ├─► TV3 + TV4 gắn nhãn 20 ca ĐỘC LẬP (C) ──► TV4 tổng hợp bang_loi.md
                       └─► TV3 chi_so.md (E1, E2)
                                    └─► TV4 ho_so_launch_v0.md (E3) ──► cả nhóm phieu_cham.md
                                                                     └─► TV1 TEAM.md, group_report.md, push
Mỗi người: copy report/team/MSSV_HoTen.md → report/team/<MSSV>_<HoTenKhongDau>.md và tự điền.
```

## TV1 · Người viết code (trước giải lao) — ĐÃ LÀM

- [x] `src/lab13.py`: A1 (3 phép thử ĐẠT), A2, A3, A4, B1–B4, D1, tỉ lệ mở lại, 3 chỉ số E1.
- [x] `report/team/bang_chi_phi.md`: đủ A1–A4, B1–B4, có nhãn simulated.
- [ ] Cuối buổi: điền `TEAM.md` (tên nhóm, lớp L3B, URL repo, commit chốt, bảng 4 thành viên + vai + đóng góp), `report/team/group_report.md`, chạy checklist trong `SUBMISSION.md`, commit + push.
- [ ] Báo cáo cá nhân của mình.

## TV2 · Người kiểm số + viết code sau giải lao — ĐÃ LÀM

- [x] Clone repo, cài môi trường (xem `src/README.md`), chạy `python lab13.py` trên **máy của mình** → phải in ĐẠT (checklist yêu cầu chạy được trên máy khác).
- [x] Tính tay **một** con số để đối chiếu, ghi cách tính vào báo cáo cá nhân. Gợi ý: (245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.472 đ.
- [x] Điền `report/team/pilot_plan.yaml` (nhiệm vụ D), dùng số D1 bên dưới. Không còn dấu `?` ngoài comment; ≥ 3 luật dừng (an toàn, chi phí, sử dụng) đủ 4 vế **NẾU – TRONG – THÌ – KHÔNG THÌ**.
- [x] Kiểm tra: `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"`.

Số D1 (đã tính):

| Câu | Kết quả |
|---|---|
| a · theo yêu cầu | 1.251 yêu cầu/nhóm |
| b · nhân viên, m = 75 | DE = 2,48 → 3.103/nhóm → 42 người/nhóm, tổng 84 > 40: không đủ người |
| c · 20 nhân viên/nhóm | tối đa 20/0,02 = 1.000 < 1.251: không đạt |
| d · 6 depot/nhóm | tối đa 300 |
| e · chênh 6 điểm (859/nhóm), 20 người/nhóm | m ≥ 299 yêu cầu/người (DE 6,96) |
| power ở 5 điểm nếu n = 859 | 0,64 (con số bất lợi, phải nêu) |
| Mở lại 7 ngày hiện tại | 4,25% (51/1.200); trong phạm vi noi_dia + hang_nang 3,97% (39/982) → đừng đặt ngưỡng tuyệt đối 3% |

Gợi ý chọn: chia theo **staff**, 20 + 20, mde 0,06, n_per_arm 859, design_effect 6,96, clusters_per_arm 20; scope noi_dia + hang_nang.

## TV3 · Người gắn nhãn 1

- [ ] **CP3 (15:35):** đọc 20 ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (mục "Hai mươi ca lỗi"), gắn nhãn **một mình trong 8 phút**, không trao đổi, **không xem bảng nhãn tham khảo trong docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md trước khi gắn**. Ghi nhãn ra giấy/ảnh chụp để làm bằng chứng.
- [ ] Điền `report/team/chi_so.md`:
  - E1: Chính 82,83% (994/1.200) · Dùng 27,12% (48/177) · An toàn 4,25% (51/1.200); tự đề xuất thêm 1 chỉ số dùng + 1 chỉ số an toàn.
  - ≥ 6 event, mỗi event có `trace_id`; phần kiểm tra chéo chỉ số ↔ event.
  - E2: ≥ 2 dòng rủi ro lấy số từ `bang_chi_phi.md` (ví dụ: làm lại ×2 → 6.787 đ +51,8%; xem lại 100% → 11.743 đ 0,98× / 12.415 đ 1,03×; khối lượng giảm một nửa → cố định 2.370 đ/việc). Ghi `[simulated]`.

## TV4 · Người gắn nhãn 2, kiêm giữ hồ sơ

- [ ] Từ đầu buổi: điền dần `report/team/ho_so_launch_v0.md` bằng số của TV1 (mục 1, 2, 3, 7 trạng thái **Giả lập**).
- [ ] **CP3:** gắn nhãn 20 ca **độc lập** với TV3 (ngồi tách, 8 phút). Sau đó cùng TV3 so nhãn → `report/team/bang_loi.md`: hai bộ nhãn, tỉ lệ đồng thuận (cần ≥ 16/20), quy tắc cho ca không trùng, bảng khắc phục 5 ca (mỗi loại 1 ca, phát hiện đo được, 1 vai trò phụ trách). **Không sửa bộ nhãn độc lập sau khi đã so.**
- [ ] 17:00: chốt hồ sơ đủ 7 mục, dòng cuối là **Go / Go có điều kiện / No-go**; gửi nhóm hội đồng.
- [ ] Chủ trì `report/team/phieu_cham.md` khi nhóm mình chấm nhóm n + 1.

## Lưu ý chung (dễ mất điểm)

1. Số nào tính từ cột `_simulated` (xem lại, làm lại, tổng, chi phí mỗi việc thành công, B1–B4, A4) → ghi **simulated**.
2. **Không** có chữ "production" trong `report/team/` → kiểm tra: `grep -rni production report/team`.
3. Người phụ trách luôn là **một vai trò** (PM trợ lý hoàn phí, Giám đốc vận hành, Trưởng nhóm CSKH, Kỹ sư trưởng agent, Kế toán trưởng…), không ghi "cả đội".
4. Viết "chỉ số trong đợt chạy thử là 82,83%", **không** viết "trợ lý đã nâng chỉ số" (chưa có đối chứng).
5. Mỗi câu trả lời ≤ 3 dòng, có ít nhất một con số.
6. Không sửa 2 file CSV; không commit `.venv/`, `.env`; không force-push.
7. Đề xuất No-go có lý do bằng số được điểm cao hơn Go bỏ qua con số bất lợi → luôn nêu số bất lợi (power 0,64; xem lại 100% = 0,98–1,03×) và cách xử lý.
8. Deadline 23h59 GMT+7 ngày lab; **mỗi người tự nộp link repo trên LMS**, ai không nộp thì không có điểm.
9. Repo phải public (hoặc mời giảng viên).
