import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1) VERİYİ OKU
# =========================
df = pd.read_csv("fiyatlar.csv")

# =========================
# 2) ARTIŞ YÜZDESİNİ HESAPLA
# =========================
df["Artis_Yuzdesi"] = (
    (df["Aralik_Fiyati"] - df["Kasim_Fiyati"]) / df["Kasim_Fiyati"]
) * 100

# =========================
# 3) GÖRSEL 1
# TÜİK vs TEMEL TÜKETİM SEPETİ
# =========================
labels = ["TÜİK (Aylık)", "Temel Tüketim Sepeti"]
values = [0.89, 8.10]

plt.figure(figsize=(6,4))
bars = plt.bar(labels, values)
plt.ylabel("Aylık Enflasyon (%)")
plt.title("Kasım–Aralık 2025 Enflasyon Karşılaştırması")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"%{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("01_tuik_vs_sepet.png", dpi=300)
plt.show()

# =========================
# 4) GÖRSEL 2
# SEPET TOPLAM TUTARI
# =========================
kasim_toplam = df["Kasim_Fiyati"].sum()
aralik_toplam = df["Aralik_Fiyati"].sum()

plt.figure(figsize=(6,4))
bars = plt.bar(["Kasım", "Aralık"], [kasim_toplam, aralik_toplam])
plt.ylabel("Toplam Sepet Tutarı (TL)")
plt.title("Temel Tüketim Sepeti Toplam Tutarı")

plt.text(0, kasim_toplam, f"{kasim_toplam:,.2f} TL", ha="center", va="bottom")
plt.text(1, aralik_toplam, f"{aralik_toplam:,.2f} TL", ha="center", va="bottom")

plt.tight_layout()
plt.savefig("02_sepet_toplami.png", dpi=300)
plt.show()

# =========================
# 5) GÖRSEL 3
# ÜRÜN BAZLI FİYAT DEĞİŞİMİ
# =========================
df_sorted = df.sort_values(by="Artis_Yuzdesi")

plt.figure(figsize=(10,8))
plt.barh(df_sorted["Urun"], df_sorted["Artis_Yuzdesi"])
plt.xlabel("Aylık Fiyat Değişimi (%)")
plt.title("Kasım–Aralık 2025 | Ürün Bazlı Fiyat Değişimi")

plt.axvline(0)  # sıfır çizgisi = artmayanlar da dahil
plt.tight_layout()
plt.savefig("03_urun_bazli_degisim.png", dpi=300)
plt.show()

# =========================
# 6) GÖRSEL 4
# METODOLOJİ (GÖRSEL KUTU)
# =========================
fig, ax = plt.subplots(figsize=(8,4))
ax.axis("off")

metin = (
    "Metodoloji\n\n"
    "- Aynı ürün, aynı marka, aynı gramaj\n"
    "- Kasım ve Aralık 2025 fiyatları\n"
    "- Zincir market ve kamu tarifeleri\n"
    "- Artmayan ürünler dahil\n\n"
    "Amaç: his değil, ölçüm"
)

ax.text(0.01, 0.5, metin, fontsize=11, va="center")
plt.tight_layout()
plt.savefig("04_metodoloji.png", dpi=300)
plt.show()

# =========================
# 7) KISA ÖZET (LOG)
# =========================
genel_artis = ((aralik_toplam - kasim_toplam) / kasim_toplam) * 100

print("===== ÖZET =====")
print(f"Kasım Sepeti : {kasim_toplam:.2f} TL")
print(f"Aralık Sepeti: {aralik_toplam:.2f} TL")
print(f"Aylık Artış  : %{genel_artis:.2f}")
print("================")
# =========================
# KOD SONU
# =========================

