"""Check Chinese New Year boundaries against known Gregorian dates."""
import unittest
from datetime import date

from chinese_zodiac_gui_frames import zodiac_sign


class ZodiacTests(unittest.TestCase):
    def test_new_year_boundaries(self):
        for before, new_year, old_animal, new_animal in [
            ('2000-02-04', '2000-02-05', 'Rabbit', 'Dragon'),
            ('2023-01-21', '2023-01-22', 'Tiger', 'Rabbit'),
            ('2024-02-09', '2024-02-10', 'Rabbit', 'Dragon'),
            ('2025-01-28', '2025-01-29', 'Dragon', 'Snake'),
            ('2026-02-16', '2026-02-17', 'Snake', 'Horse'),
        ]:
            with self.subTest(new_year=new_year):
                self.assertEqual(zodiac_sign(date.fromisoformat(before)), old_animal)
                self.assertEqual(zodiac_sign(date.fromisoformat(new_year)), new_animal)

    def test_leap_day(self):
        self.assertEqual(zodiac_sign(date(2024, 2, 29)), 'Dragon')

    def test_supported_range(self):
        self.assertEqual(zodiac_sign(date(1900, 1, 31)), 'Rat')
        self.assertEqual(zodiac_sign(date(2099, 12, 31)), 'Goat')
        for birth_date in (date(1900, 1, 30), date(2100, 1, 1)):
            with self.subTest(birth_date=birth_date), self.assertRaises(ValueError):
                zodiac_sign(birth_date)


if __name__ == '__main__':
    unittest.main()
