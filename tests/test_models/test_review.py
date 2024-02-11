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
        """
        Tests the initialization and data type of class attribute - 'place_id'
        """
        review = Review()
        place = Place()
        review.place_id = place.id
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(type(review.place_id), str)

    def test_user_id(self):
        """
        Tests the initialization and data type of class attribute - 'user_id'
        """
        review = Review()
        user = User()
        review.user_id = user.id
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(type(review.user_id), str)

    def test_review_text(self):
        """
        Tests the initialization and data types of class attribute - 'text'
        """
        review = Review()
        self.assertEqual(type(review.text), str)
        self.assertRaises(TypeError, review.text, 3)

        review.text = "Excellent"
        self.assertEqual(review.text, 'Excellent')

    def test_inherited_attributes(self):
        """Tests the initialization and values of inherited attributes"""
        review = Review()
        review0 = Review()
        self.assertNotEqual(review.id, review0.id)
        self.assertGreaterEqual(datetime.now(), review.created_at)
        self.assertGreaterEqual(review.updated_at, review.created_at)

    def test_str_function(self):
        """Tests the output value of inherited function - '__str__'"""
        review = Review()
        place = Place()
        user = User()
        review.place_id = place.id
        review.user_id = user.id
        review.text = "Excellent"
        review_str = review.__str__()
        self.assertEqual(review_str,
                         f"[Review] ({review.id}) {review.__dict__}")

    def test_to_dict_function(self):
        """Tests the output value of inherited function - 'to_dict'"""
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

    def test_class_review_with_kwargs(self):
        """Tests initialization of Review class attributes using **kwargs"""
        user = User()
        place = Place()
        kwargs = {
                'id': '12121212',
                '__class__': 'MyModel',
                'created_at': '2019-06-27T09:17:08.031275',
                'updated_at': '2019-06-27T09:17:08.031275',
                'place_id': place.id,
                'user_id': user.id,
                'text': 'Excellent'
                }
        review = Review(**kwargs)
        self.assertEqual(review.id, '12121212')
        self.assertEqual(review.to_dict()['__class__'], 'Review')
        self.assertEqual(review.created_at,
                         datetime(2019, 6, 27, 9, 17, 8, 31275))
        self.assertEqual(review.updated_at,
                         datetime(2019, 6, 27, 9, 17, 8, 31275))
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, user.id)
        self.assertEqual(review.text, 'Excellent')


if __name__ == '__main__':
    unittest.main()
