class Lesson:
    def __init__(self, code, name, grade_level, hours_per_week):
        self.code = code
        self.name = name
        self.grade_level = grade_level
        self.hours_per_week = hours_per_week

class Teacher:
    def __init__(self, code, name, courses, max_daily_hours, max_weekly_hours):
        self.code = code
        self.name = name
        self.courses = courses
        self.max_daily_hours = max_daily_hours
        self.max_weekly_hours = max_weekly_hours
