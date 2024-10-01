import requests

class Data:
    def __init__(self):
        self.question = self.get_question_data()

    @staticmethod
    def get_question_data():
        url = "https://opentdb.com/api.php?amount=1&category=9&type=boolean"
        response = requests.get(url)
        data = response.json()
        question = data['results'][0]["question"]
        answer = data['results'][0]["correct_answer"]
        return {"question": question, "answer": answer}


