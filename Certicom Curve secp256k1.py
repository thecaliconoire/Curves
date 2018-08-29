# Certicom Curve SEC P-256 (secp256k1)
from random import SystemRandom
from hashlib import sha512, sha256
from sys import argv, exit

import binascii
import hashlib
import hmac
import struct
def get_secp256k1_curve(curve=secp256k1):
  # From: http://www.secg.org/sec2-v2.pdf

  # Certicom SEC P-256
  p=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F # 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 - 1
  r=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
  a=0
  b=7

  Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
  Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

  G = point(Gx, Gy)

  return curve(a, b, p, r, G)

secp256k1 = get_secp256k1_curve()
