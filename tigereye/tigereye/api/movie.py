from flask import request
from tigereye.extensions.validator import Validator
from tigereye.models.movie import Movie
from tigereye.api import ApiVIew




class MovieView(ApiVIew):

    def all(self):
        return Movie.query.all()

    @Validator(mid = int)

    def get(self):
        mid = request.params['mid']
        print(repr(mid))
        print(type(mid))
        movie = Movie.get(mid)
        return movie




