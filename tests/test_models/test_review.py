#!/usr/bin/python3
"""
Defines TestReview class that contains methods to test Review class
"""

from datetime import datetime
from models.place import Place
from models.review import Review
from models.user import User
import unittest


class TestReview(unittest.TestCase):
    """
    defines methods that test attributes and methods of object of class Review
    """

    def test_place_id(self):
        review = Review()
        place = Place()
        review.place_id = place.id
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(type(review.place_id), str)

    def test_user_id(self):
        review = Review()
        user = User()
        review.user_id = user.id
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(type(review.user_id), str)

    def test_review_text(self):
        review = Review()
        self.assertEqual(type(review.text), str)

        review.text = "Excellent"
        self.assertEqual(review.text, 'Excellent')

    def test_inherited_attributes(self):
        review = Review()
        review0 = Review()
        self.assertNotEqual(review.id, review0.id)
        self.assertGreaterEqual(datetime.now(), review.created_at)
        self.assertGreaterEqual(review.updated_at, review.created_at)

    def test_str_function(self):
        review = Review()
        place = Place()
        user = User()
        review.place_id = place.id
        review.user_id = user.id
        review.text = "Excellent"
        review_str = review.__str__()
        self.assertEqual(review_str, f"[Review] ({review.id}) {review.__dict__}")

    def test_to_dict_function(self):
        review = Review()
        place = Place()
        user = User()
        review.place_id = place.id
        review.user_id = user.id
        review.text = "Excellent"
        self.assertEqual(review.to_dict(),
                {
                    '__class__': 'Review',
                    'id': review.id,
                    'created_at': review.created_at.isoformat(),
                    'updated_at': review.updated_at.isoformat(),
                    'place_id': place.id,
                    'user_id': user.id,
                    'text': 'Excellent'
                    }
                )

if __name__ == '__main__':
    unittest.main()
