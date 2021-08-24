from flask import Flask, request, jsonify
from similarity import Similarity

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/similarity", methods = ['GET', 'POST'])
def cal_similarity():
    if request.method == 'GET':
        return jsonify(message="please do post request")

    elif request.method == 'POST':
        request_data = request.get_json()
        # print(request_data)
        sim = Similarity()
        sim_score = sim.calculate(request_data['student_answer'], request_data['answer'])[0][0]
        # sim_score = 0
        return jsonify(similarity=str(sim_score))

if __name__ == '__main__':
  app.run()