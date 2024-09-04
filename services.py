from typing import List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import and_
import models

class MatchMaker:
    def __init__(self, user_id: int, db: Session) -> None:
        self.user_id = user_id
        self.db = db
        self.user = None
        self.weights = {
            'interests_weight': 10,
        }
        self.preferences = {
            'age_difference': 3,
            # 'partner_gender': 'Female' #could add more like this
        }

    def get_user_profile(self):
        if not self.user:
            self.user = self.db.query(models.User).filter(models.User.id == self.user_id).first()
        if not self.user:
            raise Exception("User not found")

    def get_potential_matches(self, offset: int = 0, limit: int = 20) -> List[models.User]:
        self.get_user_profile()

        min_age = self.user.age - self.preferences['age_difference']
        max_age = self.user.age + self.preferences['age_difference']
        city = self.user.city

        best_matches = self.db.query(models.User).filter(
            and_(
                models.User.id != self.user_id,
                models.User.age.between(min_age, max_age),
                models.User.city == city,
                models.User.gender != self.user.gender # Male matches with female and vice-versa
            )
        ).offset(offset).limit(limit).all()
        
        return best_matches

    def calculate_match_score(self, user_to_match):
        interests_weight = self.weights['interests_weight']
        common_interests = set(self.user.interests).intersection(set(user_to_match.interests))
        score = len(common_interests) * interests_weight
        return score

    def find_matches(self, offset: int = 0, limit: int = 20) -> List[models.User]:
        best_matches = self.get_potential_matches(offset=offset, limit=limit)

        matches_with_scores: List[Tuple[models.User, float]] = []
        for match in best_matches:
            score = self.calculate_match_score(match)
            matches_with_scores.append((match, score))

        sorted_matches = sorted(matches_with_scores, key=lambda x: x[1], reverse=True)
        print('sorted_matches: ', [(match.name, score) for match, score in sorted_matches])

        return [match for match, _ in sorted_matches]
