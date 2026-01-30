import requests
from .models import Product, Category, Status
import hashlib
from email.utils import parsedate_to_datetime

def import_produk():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    response = requests.post(url)
    server_date = response.headers.get('Date')

    if not server_date:
        raise Exception("Gagal mendapatkan tanggal server")

    server_dt = parsedate_to_datetime(server_date)

    dd = f"{server_dt.day:02d}"
    mm = f"{server_dt.month:02d}"
    yy = str(server_dt.year)[-2:]

    username = response.headers.get("X-Credentials-Username", "").split("(")[0].strip()

    print("USERNAME FIXED:", username)
    raw_password = f"bisacoding-{dd}-{mm}-{yy}"
    password = hashlib.md5(raw_password.encode()).hexdigest()

    print("USERNAME:", username)
    print("RAW PASSWORD:", raw_password)
    print("MD5 PASSWORD:", password)

    response = requests.post(
        url,
        data={
            "username": username,
            "password": password
        }
    )

    result = response.json()
    print("API RESPONSE:", result)

    if 'data' not in result:
        raise Exception("Gagal autentikasi API Fastprint")

    for item in result['data']:
        kategori, _ = Category.objects.get_or_create(
            nama_kategori=item['kategori']
        )

        status, _ = Status.objects.get_or_create(
            nama_status=item['status']
        )

        Product.objects.create(
            nama_produk=item['nama_produk'],
            harga=item['harga'],
            kategori=kategori,
            status=status
        )
