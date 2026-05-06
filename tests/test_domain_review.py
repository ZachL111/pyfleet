import unittest

from src.pyfleet.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(61, 29, 19, 89)
        self.assertEqual(review_score(item), 183)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
