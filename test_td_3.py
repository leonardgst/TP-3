l_1 = [1,1,1]

from unittest import TestCase
from bibliotheque import fonction2
class MoyenneTestCase(TestCase):

  def test_exemple(self):
    assert 1 ==1 

  def test_moyenne_111(self):
    assert moyenne([1,1,1]) == 1

  def test_moyenne_012(self):
    assert moyenne([0,1,2]) == 1



def moyenne(it):
  return sum(it)/len(it)