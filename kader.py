#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ninenin Duaları Simülatörü
Evrenin en ciddi kader hesaplayıcısı.
Gerçekten çalışır. (Biraz yavaş, ama dualar aceleye gelmez.)
"""

import random
import time
import sys

# Gizli not: Özgürce düşünmek, sormak ve gülmek her zaman izne tabi değildir.
# Bazı şeyler dualardan daha önemlidir. Ama bunu kimse duymasın.

def yavas_yaz(metin, gecikme=0.05):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def kader_hesapla():
    print("=" * 50)
    yavas_yaz("NİNENİN DUALARI SİMÜLATÖRÜ v1.0 başlatılıyor...", 0.03)
    print("=" * 50)
    print()
    
    isim = input("Adını söyle (veya boş bırak, kader bilir): ").strip()
    if not isim:
        isim = random.choice(["Sevgili Kullanıcı", "Komşunun Oğlu", "Çay Sever", "Dua Bekleyen"])
    
    print()
    yavas_yaz(f"Tamam {isim}, derinlemesine analiz başlıyor...", 0.04)
    print()
    
    asamalar = [
        "Ninenin duaları taranıyor...",
        "Komşunun kapı arkası bakışları analiz ediliyor...",
        "Çayın demlenme süresi (3.7 dakika) hesaplanıyor...",
        "'Inşallah' kelimesinin bugünkü frekansı ölçülüyor...",
        "Hava durumu ile duaların uyumu kontrol ediliyor...",
        "Rastgele bir kedi mıyavlıyor, bu da hesaba katılıyor...",
        "Evrenin derinliklerinden bir fısıltı geliyor..."
    ]
    
    for asama in asamalar:
        yavas_yaz(f"  → {asama}", 0.02)
        time.sleep(random.uniform(0.8, 1.8))
        if random.random() < 0.3:
            yavas_yaz("     (Bu aşama biraz uzun sürdü, dualar yoğun.)", 0.01)
    
    print()
    yavas_yaz("Analiz tamamlandı. Kader raporu hazırlanıyor...", 0.03)
    time.sleep(1.5)
    print()
    
    kaderler = [
        f"{isim}, bu yıl çok çay içeceksin. Ama doğru çayı içersen her şey yoluna girecek. Inşallah.",
        f"Kaderin, yarın sabah erkenden uyanmana bağlı. Uyanmazsan ninen kızar, komşun duyar.",
        f"{isim}, evren sana diyor ki: 'Biraz daha beklesen olur mu?' Ama sen dinleme, git bir şeyler yap.",
        "Büyük bir fırsat geliyor. Ama önce çayı demle, duaları oku, sonra düşün.",
        f"{isim}, sen aslında şanslısın. Sadece henüz fark etmedin. (Komşu fark etti ama.)",
        "Kaderin, bugün 'tamam' demene bağlı. Ama 'inşallah' da demeyi unutma.",
        "Analiz sonucu: Her şey güzel olacak. Ama önce bir fincan çay. Sonra bir tane daha."
    ]
    
    sonuc = random.choice(kaderler)
    print("\n" + "*" * 40)
    yavas_yaz(sonuc, 0.04)
    print("*" * 40)
    print()
    yavas_yaz("Not: Bu kader %100 doğru değildir. Ama %100 dualıdır.", 0.02)
    print()
    yavas_yaz("Teşekkürler. Nineni ara.", 0.03)

if __name__ == "__main__":
    try:
        kader_hesapla()
    except KeyboardInterrupt:
        print("\n\nKader yarıda kaldı. Dualar devam ediyor...")
