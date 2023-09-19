class MoodAnalyser():
    def mood_analyser(self, msg: str) -> str:
        dict_moods = {'весел':'веселое', 'груст': 'грустное', 'счаст': 'счастливое'}
        for key, value in dict_moods.items():
            if key in msg:
                return value
        return('Я не разобрал Ваше настроение')
