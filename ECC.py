#Elliptic Curve function

from random import SystemRandom
from hashlib import sha512, sha256
from sys import argv, exit

import binascii
import hashlib
import hmac
import struct

def __init__(self, a, b, p, r, g):
  self.a = a
  self.b = b
  self.p = p
  self.r = r
  self.g = g

def mod_inv(self, x):
  return pow(x, self.p - 2, self.p)

def add_points(self, p, q):
  s = (p.y - q.y) * self.mod_inv(p.x - q.x) % self.p
  x = (s*s - (p.x + q.x)) % self.p
  y = (s * (p.x - x) - p.y) % self.p
  return point(x, y)

def point_double(self, p):
  s = (3 * p.x * p.x + self.a) * self.mod_inv(2 * p.y) % self.p
  x = (s*s - 2 * p.x) % self.p
  y = (s * (p.x - x) - p.y) % self.p
  return point(x, y)

def multiply_point(self, c, n):
  r = None
  cpow2 = c
  while (n > 0):
      if (n & 1 == 1):
        if (r is None):
          r = cpow2
        else:
          r = self.add_points(r, cpow2)
      n = (n >> 1)
      cpow2 = self.point_double(cpow2)
  return r

  # Checks if a is a "perfect square" modulo p
def is_quad_residue(self, a):
  inv2 = self.mod_inv(2)
  e = ((self.p - 1) * inv2) % self.p
  return (pow(a, e, self.p) == 1)
    
  # Computes square root
def sqr_root(self, a):
    if (not ((self.p % 4) == 3)):
      raise Exception("Curve can't use this method")
    inv4 = self.mod_inv(4)
    e = ((self.p + 1) * inv4) % self.p
    return pow(a, e, self.p)

def x_to_point(self, x):
  yy = (pow(x, 3, self.p) + (self.a * x) + self.b) % self.p
  if self.is_quad_residue(yy):
    y = self.sqr_root(yy)
  return point(x, y)

class point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def __eq__(self, other):
  if isinstance(other, self.__class__):
    return self.__dict__ == other.__dict__
  else:
    return False

def __ne__(self, other):
  return not self.__eq__(other)

def __str__(self):
  return "(" + str(self.x) + ", " + str(self.y) + ")"

def as_hex(self):
  prefix = "04"
  x_data=int_to_hex(self.x, 256)
  y_data=int_to_hex(self.y, 256)
  return prefix + x_data + y_data

def as_bin(self):
  hex = self.as_hex()
  return binascii.unhexlify(hex)
