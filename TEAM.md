# Team

## Thông tin nhóm

- Tên nhóm: 4ChangLinhNguLam
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-4ChangLinhNguLam-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/Neronmen/K5-L3B-DAY13-4ChangLinhNguLam-LaunchEconomics · nhánh `main` · commit chốt: `1b7c730` (nội dung bài nộp; commit sau chỉ ghi mã này)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Nguyên Khoa | 2A202603795 | pnkvlog1508@gmail.com | Neronmen | Người viết code (trước giải lao) |
|   2 | Nguyễn Trọng Lâm | 2A202603817 | 26ai.lamnt6@vinuni.edu.vn | NTLam108 | Người kiểm số, viết code sau giải lao |
|   3 | Lê Viết Khoa | 2A202603737 | minfh26ai.khoalv2@vinuni.edu.vn | khoa-asta  | Người gắn nhãn 1 |
|   4 | Nguyễn Ngọc Ninh | 2A202603774 | sevenminutes2311@gmail.com | sevenminutes2311-creator | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## PhamNguyenKhoa-2A202603795

### Phần việc phụ trách

- Người viết code trước giải lao: nhiệm vụ A (CP1), B (CP2) và phần tính D1 trong `src/lab13.py`.
- Chia việc nhóm, tổng hợp `TEAM.md`, `report/team/group_report.md`, push bài.

### Đóng góp cụ thể

- Viết ba hàm A1 (ba phép thử ĐẠT), hàm `mo_hinh`, A3 theo loại, A4 chi phí cố định, 9 kịch bản B1, B2, B3, B4.
- Viết `co_mau`, `he_so_thiet_ke` và in năm câu D1, tỉ lệ mở lại 7 ngày, ba chỉ số E1 cho các thành viên khác dùng.
- Điền `report/team/bang_chi_phi.md`.

### Bằng chứng

- `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/2A202603795_PhamNguyenKhoa.md`.
- Commit của tài khoản Neronmen trên nhánh `main`.

## NguyenTrongLam-2A202603817

### Phần việc phụ trách

- Người kiểm số, viết code sau giải lao: nhiệm vụ D (`report/team/pilot_plan.yaml`).

### Đóng góp cụ thể

- Chạy lại `src/lab13.py` trên máy riêng (Windows, `.venv` mới): ĐẠT; statsmodels đối chiếu n = 1.250, power 0,64.
- Tính tay đối chiếu: cps = (245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.472 đ [simulated]; D1e m ≥ 299, DE 6,96.
- Điền `report/team/pilot_plan.yaml`: chia theo staff 20 + 20, mde 0,06, n 859/nhóm, phạm vi noi_dia + hang_nang, ba luật dừng (an toàn, chi phí, sử dụng) đủ bốn vế.

### Bằng chứng

- `report/team/pilot_plan.yaml` (đọc được bằng `yaml.safe_load`, không còn `?`), `report/team/2A202603817_NguyenTrongLam.md`.

## LeVietKhoa-2A202603737

### Phần việc phụ trách

- Người gắn nhãn 1: nhiệm vụ C (bộ nhãn 1), nhiệm vụ E1, E2 (`report/team/chi_so.md`).

### Đóng góp cụ thể

- `chi_so.md`: ba chỉ số tính thử khớp output `lab13.py` (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất, 8 event có `trace_id`, kiểm tra chéo chỉ số với event, 3 dòng rủi ro kinh tế có nhãn simulated.
- `bang_loi.md`: điền bộ nhãn người 1 cho 20 ca. Bộ nhãn có AI hỗ trợ và đã đối chiếu nhãn tham khảo, không phải gắn độc lập 8 phút (đã ghi rõ trong file và báo cáo cá nhân).

### Bằng chứng

- `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/2A202603737_LeVietKhoa.md`; commit trên nhánh `feature/gannhan1`, đã merge vào `main`.

## NguyenNgocNinh-2A202603774

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: nhiệm vụ C (bộ nhãn 2, tổng hợp `report/team/bang_loi.md`), E3 (`report/team/ho_so_launch_v0.md`), chủ trì `report/team/phieu_cham.md`.

### Đóng góp cụ thể

- `ho_so_launch_v0.md`: đủ 7 mục, mỗi mục có con số chính, trạng thái và một vai trò phụ trách; nêu ba con số bất lợi kèm cách xử lý; đề xuất Go có điều kiện với 4 điều kiện có người phụ trách và ngày kiểm tra.
- Nhiệm vụ C: bộ nhãn người 2 (20 ca, gắn tay), so nhãn 20/20, bảng khắc phục 5 ca đủ 5 loại; cập nhật mục 5 hồ sơ.

### Bằng chứng

- `report/team/ho_so_launch_v0.md`, `report/team/2A202603774_NguyenNgocNinh.md`; commit `f04fffd`, `464cace` trên `main`.
