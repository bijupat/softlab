# utils.py (fingerprinting and QR code generation)

import hashlib
from ipaddress import ip_address
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile


def hash_ip(ip):
    # Hash IP with SHA256 for GDPR compliance
    return hashlib.sha256(ip.encode('utf-8')).hexdigest()


def generate_fingerprint(ip, user_agent, accept_headers):
    data = f"{hash_ip(ip)}|{user_agent}|{accept_headers}"
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def create_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue())