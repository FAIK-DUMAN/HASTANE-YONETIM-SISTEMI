import pandas as pd
from personel import Personel
from doktor import Doktor
from hemsire import Hemsire
from hasta import Hasta

try:
    # Personel sınıfından örnekler oluşturuluyor
    personel1 = Personel(1, "Eren", "Erkut", "Yönetim", 5000)
    personel2 = Personel(2, "Mirza", "Millet", "Maliye", 5500)

    # Doktor sınıfından örnekler oluşturuluyor
    doktor1 = Doktor(3, "Dr. Semih", "Ertan", "Cerrahi", 10000, "Genel Cerrah", 6, "Uşak Devlet Hastanesi")
    doktor2 = Doktor(4, "Dr. Faik", "Duman", "Kardiyoloji", 12000, "Kardiyolog", 8, "Öztan Hastanesi")
    doktor3 = Doktor(5, "Dr. Metehan", "Adıgüzel", "Pediatri", 11000, "Çocuk Doktoru", 3, "Uşak Üniversitesi Eğitim ve Araştırma Hastanesi")

    # Hemşire sınıfından örnekler oluşturuluyor
    hemsire1 = Hemsire(6, "Nurse Mustafa", "Pişkin", "Yoğun Bakım", 7000, 40, "Yoğun Bakım Sertifikası", "Uşak Devlet Hastanesi")
    hemsire2 = Hemsire(7, "Nurse Büşra", "Kaya", "Genel Servis", 6500, 38, "Genel Hemşirelik Sertifikası", "Öztan Hastanesi")
    hemsire3 = Hemsire(8, "Nurse Cemile", "Deniz", "Acil", 6800, 42, "Acil Sertifikası", "Uşak Üniversitesi Eğitim ve Araştırma Hastanesi")

    # Hasta sınıfından örnekler oluşturuluyor
    hasta1 = Hasta(1, "Mehmet efe", "Demirel", "1992-05-12", "Covid-19", "Aşı Tedavisi")
    hasta2 = Hasta(2, "Akif", "Duman", "1988-09-20", "Kalp Rahatsızlığı", "Cerrahi Müdahale")
    hasta3 = Hasta(3, "Ömer", "Demir", "2000-01-01", "Soğuk Algınlığı", "Dinlenme ve İlaç")

    # Tüm personel ve hasta verileri bir DataFrame'e aktarılıyor
    personel_data = [
        [personel1.get_ad(), personel1.get_soyad(), personel1.get_departman(), personel1.get_maas(), None, None, None, None, None],
        [personel2.get_ad(), personel2.get_soyad(), personel2.get_departman(), personel2.get_maas(), None, None, None, None, None],
        [doktor1.get_ad(), doktor1.get_soyad(), doktor1.get_departman(), doktor1.get_maas(), doktor1.get_uzmanlik(), doktor1.get_deneyim_yili(), doktor1.get_hastane(), None, None],
        [doktor2.get_ad(), doktor2.get_soyad(), doktor2.get_departman(), doktor2.get_maas(), doktor2.get_uzmanlik(), doktor2.get_deneyim_yili(), doktor2.get_hastane(), None, None],
        [doktor3.get_ad(), doktor3.get_soyad(), doktor3.get_departman(), doktor3.get_maas(), doktor3.get_uzmanlik(), doktor3.get_deneyim_yili(), doktor3.get_hastane(), None, None],
        [hemsire1.get_ad(), hemsire1.get_soyad(), hemsire1.get_departman(), hemsire1.get_maas(), None, None, hemsire1.get_hastane(), hemsire1.get_calisma_saati(), hemsire1.get_sertifika()],
        [hemsire2.get_ad(), hemsire2.get_soyad(), hemsire2.get_departman(), hemsire2.get_maas(), None, None, hemsire2.get_hastane(), hemsire2.get_calisma_saati(), hemsire2.get_sertifika()],
        [hemsire3.get_ad(), hemsire3.get_soyad(), hemsire3.get_departman(), hemsire3.get_maas(), None, None, hemsire3.get_hastane(), hemsire3.get_calisma_saati(), hemsire3.get_sertifika()]
    ]

    patient_data = [
        [hasta1.get_ad(), hasta1.get_soyad(), hasta1.get_hastalik(), hasta1.get_tedavi(), hasta1.get_dogum_tarihi()],
        [hasta2.get_ad(), hasta2.get_soyad(), hasta2.get_hastalik(), hasta2.get_tedavi(), hasta2.get_dogum_tarihi()],
        [hasta3.get_ad(), hasta3.get_soyad(), hasta3.get_hastalik(), hasta3.get_tedavi(), hasta3.get_dogum_tarihi()]
    ]

    personel_columns = ["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastane", "Çalışma Saati", "Sertifika"]
    patient_columns = ["Hasta Adı", "Hasta Soyadı", "Hastalık", "Tedavi", "Doğum Tarihi"]

    # Veriler DataFrame'e aktarılıyor
    df_personel = pd.DataFrame(personel_data, columns=personel_columns)
    df_patient = pd.DataFrame(patient_data, columns=patient_columns)

    # Eksik (NA/NaN) değerler dolduruluyor ve uygun veri tiplerine dönüştürülüyor
    df_personel.fillna(0, inplace=True)
    df_personel["Deneyim Yılı"] = pd.to_numeric(df_personel["Deneyim Yılı"], errors='coerce').fillna(0).astype(int)
    df_personel["Çalışma Saati"] = pd.to_numeric(df_personel["Çalışma Saati"], errors='coerce').fillna(0).astype(int)
    df_personel["Maaş"] = pd.to_numeric(df_personel["Maaş"], errors='coerce').fillna(0).astype(int)

    # Uzmanlık alanlarına göre doktor sayısı gösteriliyor
    print("========================================================================================")
    print("Uzmanlık Alanlarına Göre Doktor Sayısı:")
    doktor_grup = df_personel[df_personel["Uzmanlık"] != 0].groupby('Uzmanlık').size()
    for uzmanlik, sayi in doktor_grup.items():
        print(f"{uzmanlik}: {sayi}")
    print("========================================================================================\n")

    # 5 yıldan fazla deneyime sahip doktor sayısı gösteriliyor
    deneyim_fazla_5 = df_personel[df_personel['Deneyim Yılı'] > 5]['Ad'].count()
    print(f"5 Yıldan Fazla Deneyime Sahip Doktor Sayısı: {deneyim_fazla_5}")
    print("========================================================================================\n")

    # Hastalar alfabetik olarak sıralanıyor ve gösteriliyor
    print("Alfabetik Olarak Sıralanmış Hastalar:")
    df_patient_sorted = df_patient.sort_values(by=["Hasta Adı"])
    print(df_patient_sorted.to_string(index=False))
    print("========================================================================================\n")

    # Maaşı 7000 TL üzerinde olan personeller gösteriliyor
    print("Maaşı 7000 TL Üzerinde Olan Personeller:")
    maasi_7000_ust = df_personel[df_personel['Maaş'] > 7000]
    print(maasi_7000_ust.to_string(index=False))
    print("========================================================================================\n")

    # Doğum tarihi 1990 ve sonrası olan hastalar gösteriliyor
    print("Doğum Tarihi 1990 ve Sonrası Olan Hastalar:")
    df_patient['Doğum Tarihi'] = pd.to_datetime(df_patient['Doğum Tarihi'], errors='coerce')
    dogum_1990_sonrasi = df_patient[df_patient['Doğum Tarihi'] >= '1990-01-01']
    print(dogum_1990_sonrasi.to_string(index=False))
    print("========================================================================================\n")

    # Seçilen sütunlarla yeni DataFrame'ler oluşturuluyor
    print("Yeni Personel DataFrame:")
    yeni_df_personel = df_personel[['Ad', 'Soyad', 'Departman', 'Maaş', 'Uzmanlık', 'Deneyim Yılı']]
    print(yeni_df_personel.to_string(index=False))
    print("========================================================================================\n")

    print("Yeni Hasta DataFrame:")
    yeni_df_patient = df_patient[['Hasta Adı', 'Hasta Soyadı', 'Hastalık', 'Tedavi']]
    print(yeni_df_patient.to_string(index=False))
    print("========================================================================================\n")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
