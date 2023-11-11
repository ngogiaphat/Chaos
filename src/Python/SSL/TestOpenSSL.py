import OpenSSL
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from OpenSSL import crypto
#Gerenate a new private key
key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048,
    backend = default_backend()
)
#Create a self-signed cert SSL certificate
subject = issuer = x509.Name([
    x509.NameAttribute(x509.NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
    x509.NameAttribute(x509.NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(x509.NameOID.COMMON_NAME, u"localhost"),
])
cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(
    datetime.utcnow()
).not_valid_after(datetime.utcnow() + timedelta(days = 365)).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical = False,
).sign(key, hashes.SHA256(), default_backend())
#Save the key and certifcate to a file
with open ("key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding = crypto.FILETYPE_PEM,
        format = crypto.PKCS8_PRIVATE_KEY
    ))
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(encoding = serialization.Encoding.PEM))