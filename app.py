from flask import Flask, request, render_template
import json
import os
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def question_form():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')

        qa_dict = {
            'question': question,
            'answer': answer
        }

        if os.path.isfile('data.json'):
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
                data.append(qa_dict)
        else:
            data = [qa_dict]

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
            
        # To push the changes to the Github repo, please use a Github action or a similar CI/CD pipeline.

        return 'Thank you for your submission.'

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
