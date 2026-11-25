"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

# In tiếng Việt không lỗi trên Windows console (cp1252)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý mỗi tháng
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']   # phạm vi pilot đề xuất


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print(f'  so_lan_chay_ky_vong(0.8, 2)               = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  so_lan_chay_ky_vong(0.8)                  = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi là chuyển nhân viên, 0 phút xem lại/làm lại
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
                so_yc=len(reqs))


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (z chính xác)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=0.02):
    return 1 + (m - 1) * icc


def tieu_de(s):
    print(f'\n=== {s} ===')


def vnd(x):
    return f'{x:,.0f}'.replace(',', '.')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    # ---------- A1 ----------
    tieu_de('A1 · Ba phép thử')
    kiem_tra_dap_an_biet_truoc()

    # ---------- A2 ----------
    tieu_de('A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps = simulated)')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    goc = ket_qua['cps']
    print(f'Số lần gọi tool: {runs.tool_calls.sum():,}; phút xem lại: {reqs.phut_xem_lai_simulated.sum():,}; '
          f'phút làm lại: {reqs.phut_lam_lai_simulated.sum():,}')
    print(f'cps / hoá đơn mỗi yêu cầu = {goc / ket_qua["hoa_don_moi_yc"]:.1f} lần')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s} {ket_qua[k] / ket_qua["tong"] * 100:5.1f}%')
    gio_nv = (ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong']
    print(f'  giờ nhân viên chiếm {gio_nv * 100:.1f}% tổng chi phí')
    khong_tc = ket_qua['so_yc'] - ket_qua['thanh_cong']
    he_thong = (ket_qua['tong'] + khong_tc * BASELINE) / ket_qua['so_yc']
    print(f'Chi phí cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca không thành công × 12.000 đ) = '
          f'{vnd(he_thong)} đ = {he_thong / BASELINE:.2f}× [simulated]')

    # ---------- A3 ----------
    tieu_de('A3 · Tách theo loại yêu cầu (cps = simulated)')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"so_12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        kq = mo_hinh(runs, r)
        lan = runs[runs.request_id.isin(r.request_id)].shape[0] / len(r)
        print(f'{loai:10s} {len(r):6d} {kq["thanh_cong"] / len(r) * 100:8.1f}% {lan:7.2f} '
              f'{vnd(kq["cps"]):>9s} {kq["cps"] / BASELINE:6.2f}×')
    print('Tỉ lệ ok theo từng lần thử (đo từ trace):')
    rl = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    rl['ok'] = (rl.status == 'ok').astype(float)
    bang_ok = rl.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    print((bang_ok * 100).round(1).to_string())

    # ---------- A4 ----------
    tieu_de('A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated)')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    kq_pv = mo_hinh(runs, pv)
    print(f'Phạm vi: {len(pv)} yêu cầu, {kq_pv["thanh_cong"]} thành công, tổng {vnd(kq_pv["tong"])} đ, '
          f'cps {vnd(kq_pv["cps"])} đ')
    for nhan, kl in [('45.000 yc/tháng', YC_THANG), ('một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = kl * kq_pv['thanh_cong'] / len(reqs)
        cd = CO_DINH_THANG / tc_thang
        print(f'{nhan:20s} việc TC/tháng {tc_thang:9,.0f} · cố định/việc {vnd(cd)} đ · '
              f'cps + cố định {vnd(kq_pv["cps"] + cd)} đ = {(kq_pv["cps"] + cd) / BASELINE:.2f}×')

    # ---------- B1 ----------
    tieu_de('B1 · Đổi từng yếu tố (simulated)')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":25s} {vnd(goc):>8s}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {vnd(cps):>8s} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- B2 ----------
    tieu_de('B2 · Đổi một cặp (simulated)')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Giá token ×2 + xem lại ×2: {vnd(cap)} đ ({(cap / goc - 1) * 100:+.1f}%)')

    # ---------- B3 ----------
    tieu_de('B3 · Giới hạn chạy lại và chi phí cả hệ thống (simulated)')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        ktc = kq['so_yc'] - kq['thanh_cong']
        print(f'{k} lần: trợ lý {vnd(kq["tong"])} đ · không TC {ktc} · cả hệ thống '
              f'{vnd(kq["tong"] + ktc * BASELINE)} đ · cps {vnd(kq["cps"])} đ')

    # ---------- B4 ----------
    tieu_de('B4 · Xem lại 100% cho noi_dia + hang_nang (simulated)')
    runs_pv = runs[runs.request_id.isin(pv.request_id)]
    co_ok = runs_pv[runs_pv.status == 'ok'].request_id.nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    tien_ai = (runs_pv.tokens_in / 1000 * GIA_VAO + runs_pv.tokens_out / 1000 * GIA_RA
               + runs_pv.tool_calls * GIA_TOOL).sum()
    phut_lam_lai_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for phut_ll in [9, phut_lam_lai_tb]:
        tong_b4 = co_ok * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + tien_ai
        cps_b4 = tong_b4 / kq_pv['thanh_cong']
        # hoà vốn: số phút xem lại x sao cho cps = 12.000
        hoa_von = (BASELINE * kq_pv['thanh_cong'] - so_lam_lai * phut_ll * LUONG_PHUT - tien_ai) / (co_ok * LUONG_PHUT)
        print(f'Làm lại {phut_ll:.1f} phút/ca: {co_ok} yc có ok × 5 phút, {so_lam_lai} ca làm lại, AI {vnd(tien_ai)} đ '
              f'→ tổng {vnd(tong_b4)} đ / {kq_pv["thanh_cong"]} = {vnd(cps_b4)} đ = {cps_b4 / BASELINE:.2f}× '
              f'· hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')
    print(f'phut_lam_lai_simulated trung bình trên ca lam_lai: {phut_lam_lai_tb:.1f} '
          f'(trung vị {reqs.loc[reqs.ket_qua == "lam_lai", "phut_lam_lai_simulated"].median():.1f})')

    # ---------- D1 ----------
    tieu_de('D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    ICC = 0.02
    n_a = co_mau(0.70, 0.75)
    print(f'a) Chia theo yêu cầu: {n_a} yêu cầu mỗi nhóm')
    de_b = he_so_thiet_ke(75, ICC)
    n_b = math.ceil(n_a * de_b)
    print(f'b) Theo nhân viên m=75: DE = {de_b:.2f}; n = {n_b:,.0f} mỗi nhóm → '
          f'{math.ceil(n_b / 75)} người mỗi nhóm, tổng {2 * math.ceil(n_b / 75)} > 40: không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: tối đa c/ICC = {20 / ICC:,.0f} < {n_a}: không đạt')
    print(f'd) 6 depot mỗi nhóm: tối đa {6 / ICC:,.0f}')
    n_6 = co_mau(0.70, 0.76)
    m_e = math.ceil(n_6 * (1 - ICC) / (20 - n_6 * ICC))
    print(f'e) Mức chênh 6 điểm: {n_6} mỗi nhóm; 20 người mỗi nhóm → m ≥ {m_e} yêu cầu mỗi người '
          f'(DE {he_so_thiet_ke(m_e, ICC):.2f}; hiệu dụng {20 * m_e / he_so_thiet_ke(m_e, ICC):,.0f})')
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        es5 = proportion_effectsize(0.75, 0.70)
        print(f'   statsmodels: n (5 điểm) = {NormalIndPower().solve_power(es5, alpha=0.05, power=0.8):,.0f}; '
              f'power ở 5 điểm với n=859 = {NormalIndPower().power(es5, nobs1=859, alpha=0.05):.2f}')
    except ImportError:
        print('   (chưa cài statsmodels: bỏ qua phần đối chiếu)')

    # ---------- D3 · tỉ lệ mở lại hiện tại ----------
    tieu_de('D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại')
    print(f'Toàn mẫu: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)}); '
          f'phạm vi noi_dia + hang_nang: {pv.mo_lai_trong_7_ngay.mean() * 100:.2f}% '
          f'({pv.mo_lai_trong_7_ngay.sum()}/{len(pv)})')
    print(f'Tỉ lệ lam_lai trong phạm vi: {(pv.ket_qua == "lam_lai").mean() * 100:.1f}%')

    # ---------- E1 · ba chỉ số tính thử ----------
    tieu_de('E1 · Ba chỉ số tính thử trên 1.200 yêu cầu')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    print(f'Chính  : {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng   : {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f'An toàn: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)})')
