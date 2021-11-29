import unittest

from hamcrest import *

from Monster import KingSkull, Bat, Zombie, Spider


class TestMonster(unittest.TestCase):

    def testKingSkull(self):
        king_skull = KingSkull()
        assert_that(king_skull, instance_of(KingSkull))
        # vérifie si c'est un objet de type Kingskull
        self.assertEqual(king_skull.level, 3)
        # vérifie le niveau du monstre
        assert_that(king_skull.name, matches_regexp("King Skull"))
        # vérifie le nom du monstre

    def testBat(self):
        bat = Bat()
        assert_that(bat, instance_of(Bat))
        # vérifie si c'est un objet de type Kingskull
        self.assertEqual(bat.level, 1)
        # vérifie le niveau du monstre
        assert_that(bat.name, matches_regexp("Bat"))
        # vérifie le nom du monstre
    
    def testZombie(self):
        zombie = Zombie()
        assert_that(zombie, instance_of(Zombie))
        # vérifie si c'est un objet de type Kingskull
        self.assertEqual(zombie.level, 1)
        # vérifie le niveau du monstre
        assert_that(zombie.name, matches_regexp("Zombie"))
        # vérifie le nom du monstre
    
    def testSpider(self):
        spider = Spider()
        assert_that(spider, instance_of(Spider))
        # vérifie si c'est un objet de type Kingskull
        self.assertEqual(spider.level, 2)
        # vérifie le niveau du monstre
        assert_that(spider.name, matches_regexp("Spider"))
        # vérifie le nom du monstre
