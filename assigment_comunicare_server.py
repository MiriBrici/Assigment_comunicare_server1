from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')
app.static_folder = 'static'
students = {}
current_student_id = 1

@app.route('/add_student', methods=['POST'])
def add_student():
    global current_student_id

    data = request.get_json()

    student = {
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'average_grade': data['average_grade']
    }

    students[current_student_id] = student
    current_student_id += 1

    return jsonify({'message': 'Student added successfully'})

@app.route('/get_student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)

    if student:
        return jsonify(student)
    else:
        return jsonify({'message': 'Student not found'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
