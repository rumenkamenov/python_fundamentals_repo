class Exersice:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = self.set_topic(topic)
        self.course_name = self.set_course_name(course_name)
        self.judge_contest_link = self.set_judge_contest_link(judge_contest_link)
        self.problems = problems.split(', ')

    def set_topic(self, topic):

        if isinstance(topic, str):
            return topic
        raise Exception

    def set_course_name(self, course_name):

        if isinstance(course_name, str):
            return course_name
        raise Exception

    def set_judge_contest_link(self, judge_contest_link):

        if isinstance(judge_contest_link, str):
            return judge_contest_link
        raise Exception


collection_of_exercises = []

data = input()

while data != "go go go":

    topic, course_name, judge_contest_link, problems = list(data.split(' -> '))
    exersice = Exersice(topic, course_name, judge_contest_link, problems)
    collection_of_exercises.append(exersice)
    data = input()

#print(f"Exercises: {topic}")
#print(f"Problems for exercises and homework for the {course_name} course @ SoftUni.")
#print(f"Check your solutions here: {judge_contest_link}")



for colection in collection_of_exercises:
    print(f'Exercises: {colection.topic}')
    print(f'Problems for exercises and homework for the "{colection.course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {colection.judge_contest_link}')

    for i in range(len(colection.problems)):
        print(f'{i + 1}. {colection.problems[i]}')







