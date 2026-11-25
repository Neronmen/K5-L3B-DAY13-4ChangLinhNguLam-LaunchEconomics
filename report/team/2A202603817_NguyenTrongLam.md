# Báo cáo cá nhân — NguyenTrongLam-2A202603817

## 1. Thông tin thành viên

- Họ tên: Nguyễn Trọng Lâm
- MSSV: 2A202603817
- Email: 26ai.lamnt6@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số, viết code sau giải lao (TV2)

## 2. Phần việc phụ trách

- Chạy lại `src/lab13.py` trên máy riêng để kiểm tra code của TV1 chạy được trên máy khác.
- Tính tay một con số để đối chiếu với output của code.
- Nhiệm vụ D (CP4): điền `report/team/pilot_plan.yaml` (D1, D2, đánh đổi, tỉ lệ mở lại, ba luật dừng).

## 3. Đóng góp cụ thể

- Tạo `src/.venv` trên Windows, cài `requirements.txt`; `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`, statsmodels đối chiếu n = 1.250 (code 1.251, lệch < 2%) và power 0,64.
- Tính tay chi phí mỗi việc thành công (A2): (245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.373.585 / 978 = **4.472 đ** [simulated], khớp `cps 4,472.0`.
- Tính tay câu D1e: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 298,5 → **299**; DE = 1 + 298 × 0,02 = **6,96**; kiểm lại 20 × 299 / 6,96 = 859,2 ≥ 859.
- Tính lại power ở 5 điểm với n = 859 bằng Cohen h = 2·asin(√0,75) − 2·asin(√0,70) = 0,112 → power = Φ(0,112 × √(859/2) − 1,96) = **0,64**.
- `pilot_plan.yaml`: chọn chia theo **staff** 20 + 20, mde 0,06, n_per_arm 859, DE 6,96, 20 cụm mỗi nhóm; phạm vi noi_dia + hang_nang; ngưỡng an toàn so đối chứng +2 điểm kèm trần 6% (vì mở lại hiện tại đã 4,25%, phạm vi 3,97%, nên ngưỡng 3% sẽ dừng pilot ngay tuần đầu); ba luật dừng an toàn, chi phí, sử dụng đủ NẾU – TRONG – THÌ – KHÔNG THÌ.
- Ước lượng ngày quyết định: phạm vi ≈ 82% × 1.500 ≈ 1.230 yc/ngày ≈ 31 yc/người/ngày → cần khoảng 10 ngày làm việc ở bước 0.50 để đạt 299 yc/người → decision_date 2027-01-11.

## 4. Bằng chứng

- File: `report/team/pilot_plan.yaml`, báo cáo này.
- Kiểm tra: `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"` chạy không lỗi; `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì; lệnh grep kiểm tra từ cấm trong `report/team` không in gì.
- Output `cd src && python lab13.py` trên máy TV2: `ĐẠT`, `cps 4,472.0`, `statsmodels: n (5 điểm) = 1,250; power ở 5 điểm với n=859 = 0.64`.

## 5. Công cụ AI đã dùng

- Claude Code: chạy lại `lab13.py`, gợi ý cách viết các trường của `pilot_plan.yaml` theo hướng dẫn trong `docs/`, kiểm tra cú pháp YAML.
- Cách tự kiểm tra: mọi số trong `pilot_plan.yaml` lấy từ output `lab13.py` hoặc bảng D1 trong `PHAN_CONG.md`; tính tay lại 4.472 đ, m ≥ 299, DE 6,96 và power 0,64 (khớp output statsmodels).

## 6. Tự đánh giá

- Hiểu vì sao với 40 nhân viên không cách chia theo cụm nào đủ mẫu cho 5 điểm (tối đa 20 / 0,02 = 1.000 < 1.251), và vì sao vẫn chọn chia theo nhân viên thay vì theo yêu cầu (tách được tác động).
- Con số bất lợi phải nêu với hội đồng: power chỉ 0,64 nếu tác động thật là 5 điểm; các số chi phí trong luật dừng (8.000 đ) dựa trên phút xem lại / làm lại simulated, cần thay bằng phút đo thật trong pilot.
