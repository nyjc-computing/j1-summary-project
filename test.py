import game
class CodeError(Exception):
    pass
roomlist = []


def boss_present():
    if boss not in maze:
        raise CodeError('You removed the end game method')

def player_present():
    if player not in maze:
        raise CodeError('How did you even make this happen')

how write test without data structure