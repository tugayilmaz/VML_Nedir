import base64

# XML dosyasını oku
with open("e_fatura.xml", "rb") as file:
    xml_data = file.read()

# XML verisini Base64 formatına çevir
base64_encoded = base64.b64encode(xml_data).decode("utf-8")

# Base64 formatındaki veriyi yeni bir dosyaya yaz
with open("e_fatura_base64.txt", "w") as file:
    file.write(base64_encoded)

print("✅ Base64 dönüşümü tamamlandı! 'e_fatura_base64.txt' dosyası oluşturuldu.")
