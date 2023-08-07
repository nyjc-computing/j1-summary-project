import game
class CodeError(Exception):
    pass
roomlist = []

'''def move_check(room) -> str:
    if room not in roomlist:
        raise SkillIssue('Player moved to a room that does not exist')

move_check('piss')'''

def boss_present():
    if boss not in maze:
        raise CodeError('You removed the end game method')

def player_present():
    if player not in maze:
        raise CodeError('How did you even make this happen')