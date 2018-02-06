from tigereye.extensions.validator import Validator
from tigereye.models.play import Play
from flask import request
from tigereye.api import ApiVIew
from tigereye.models.seat import PlaySeat,SeatType

class PlayView(ApiVIew):
    def all(self):
        return Play.query.all()


    @Validator(pid=int)
    def seats(self):
        pid = request.params['pid']
        return PlaySeat.query.filter(
            PlaySeat.pid==pid,
            PlaySeat.seat_type!=SeatType.road.value
        ).all()
        # if not movie:
        #     return Code.movie_dose_not_exist, request.arg




