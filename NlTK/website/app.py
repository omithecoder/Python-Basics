import base64
from io import BytesIO

import matplotlib.pyplot as plt
from flask import Flask, render_template, request

app = Flask(__name__)

# Define a dictionary to map question numbers to their corresponding strengths.
strengths_map = {
    "q1": "Effective Communication",
    "q2": "Problem-Solving",
    "q3": "Leadership",
    "q4": "Creativity",
    "q5": "Adaptability",
    "q6": "Attention to Detail",
    "q7": "Handling Pressure",
    "q8": "Continuous Learning",
}

# Dummy career profiles data
career_profiles = [
    {
        'career_name': 'Software Developer',
        'required_qualifications': ['Bachelor of Science in Computer Science', 'Programming skills'],
        'required_skills': ['Problem-solving', 'Coding', 'Teamwork', 'Effective Communication', 'Continuous Learning'],
        'industry': 'Information Technology'
    },
    {
        'career_name': 'Marketing Manager',
        'required_qualifications': ['Bachelor of Business Administration', 'Marketing knowledge'],
        'required_skills': ['Marketing strategy', 'Data analysis', 'Communication', 'Leadership', 'Adaptability'],
        'industry': 'Marketing'
    },
    {
        'career_name': 'Registered Nurse',
        'required_qualifications': ['Bachelor of Science in Nursing'],
        'required_skills': ['Patient care', 'Medical knowledge', 'Empathy', 'Effective Communication',
                            'Handling Pressure'],
        'industry': 'Healthcare'
    },
    {
        'career_name': 'Financial Analyst',
        'required_qualifications': ['Bachelor of Finance', 'Analytical skills'],
        'required_skills': ['Financial modeling', 'Data analysis', 'Risk assessment', 'Attention to Detail',
                            'Continuous Learning'],
        'industry': 'Finance'
    },
    {
        'career_name': 'Data Scientist',
        'required_qualifications': ['Master of Data Science', 'Data analysis skills'],
        'required_skills': ['Data mining', 'Machine learning', 'Statistical analysis', 'Problem-Solving',
                            'Continuous Learning'],
        'industry': 'Information Technology'
    },
    {
        'career_name': 'Graphic Designer',
        'required_qualifications': ['Bachelor of Fine Arts in Graphic Design', 'Design software skills'],
        'required_skills': ['Graphic design', 'Creativity', 'Attention to Detail', 'Continuous Learning'],
        'industry': 'Design'
    },
    {
        'career_name': 'Civil Engineer',
        'required_qualifications': ['Bachelor of Science in Civil Engineering'],
        'required_skills': ['Structural design', 'Project management', 'Mathematics', 'Problem-Solving',
                            'Continuous Learning'],
        'industry': 'Engineering'
    },
    {
        'career_name': 'Dental Hygienist',
        'required_qualifications': ['Associate degree in Dental Hygiene'],
        'required_skills': ['Dental cleaning', 'Patient education', 'Oral health assessment', 'Problem-Solving',
                            'Continuous Learning'],
        'industry': 'Healthcare'
    },
    {
        'career_name': 'Digital Marketing Specialist',
        'required_qualifications': ['Bachelor of Business Administration', 'Digital marketing knowledge'],
        'required_skills': ['SEO', 'Social media marketing', 'Content creation', 'Effective Communication',
                            'Continuous Learning'],
        'industry': 'Marketing'
    },
    {
        'career_name': 'Mechanical Engineer',
        'required_qualifications': ['Bachelor of Science in Mechanical Engineering'],
        'required_skills': ['Mechanical design', 'Thermodynamics', 'CAD software', 'Problem-Solving',
                            'Continuous Learning'],
        'industry': 'Engineering'
    },
    {
        'career_name': 'Psychologist',
        'required_qualifications': ['Doctorate in Psychology'],
        'required_skills': ['Counseling', 'Psychological assessment', 'Research', 'Effective Communication',
                            'Continuous Learning'],
        'industry': 'Healthcare'
    },
    {
        'career_name': 'Financial Planner',
        'required_qualifications': ['Certified Financial Planner (CFP)', 'Financial knowledge'],
        'required_skills': ['Financial planning', 'Investment management', 'Risk assessment', 'Attention to Detail',
                            'Continuous Learning'],
        'industry': 'Finance'
    },
    {
        'career_name': 'Elementary School Teacher',
        'required_qualifications': ['Bachelor of Education', 'Teaching certification'],
        'required_skills': ['Classroom management', 'Curriculum planning', 'Patience', 'Effective Communication',
                            'Continuous Learning'],
        'industry': 'Education'
    },
    {
        'career_name': 'Mechatronics Engineer',
        'required_qualifications': ['Bachelor of Science in Mechatronics Engineering'],
        'required_skills': ['Robotics', 'Electronics', 'Control systems', 'Problem-Solving', 'Continuous Learning'],
        'industry': 'Engineering'
    },
    {
        'career_name': 'Physiotherapist',
        'required_qualifications': ['Master of Physiotherapy', 'Physical therapy skills'],
        'required_skills': ['Rehabilitation', 'Pain management', 'Patient assessment', 'Effective Communication',
                            'Continuous Learning'],
        'industry': 'Healthcare'
    },
    {
        'career_name': 'Accountant',
        'required_qualifications': ['Bachelor of Accountancy', 'Accounting knowledge'],
        'required_skills': ['Financial reporting', 'Taxation', 'Auditing', 'Attention to Detail',
                            'Continuous Learning'],
        'industry': 'Finance'
    },
    {
        'career_name': 'Art Director',
        'required_qualifications': ['Bachelor of Fine Arts in Design', 'Artistic skills'],
        'required_skills': ['Creative direction', 'Visual design', 'Team leadership', 'Continuous Learning'],
        'industry': 'Design'
    },
    {
        'career_name': 'Environmental Scientist',
        'required_qualifications': ['Bachelor of Science in Environmental Science', 'Environmental knowledge'],
        'required_skills': ['Environmental research', 'Data analysis', 'Environmental impact assessment',
                            'Problem-Solving', 'Continuous Learning'],
        'industry': 'Environmental Science'
    },
    {
        'career_name': 'Pharmacist',
        'required_qualifications': ['Doctor of Pharmacy', 'Pharmacy knowledge'],
        'required_skills': ['Medication dispensing', 'Patient consultation', 'Pharmaceutical care',
                            'Effective Communication', 'Continuous Learning'],
        'industry': 'Healthcare'
    },
]


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form['user_name']
    return render_template('options.html', UN=user_name)


@app.route('/options', methods=['POST'])
def options():
    user_name = request.form['user_name']
    user_choice = request.form['choice']
    if user_choice == '1':
        return render_template('education.html', UN=user_name)
    elif user_choice == '2':
        return render_template('career_path_counseling.html', UN=user_name)
    elif user_choice == '3':
        return render_template('career_related_topics.html', UN=user_name)
    else:
        return "Invalid choice."


@app.route('/test', methods=['POST'])
def show_test():
    # Retrieve and process academic scores
    education_level = request.form.get('education_level')
    academic_scores = {}

    if education_level == 'SSC':
        academic_scores['Math'] = int(request.form.get('math_score'))
        academic_scores['Science'] = int(request.form.get('science_score'))
        academic_scores['English'] = int(request.form.get('english_score'))
    elif education_level == 'HSC':
        hsc_percentage = int(request.form.get('hsc_percentage'))
        academic_scores['HSC Percentage'] = int(hsc_percentage)
        # else:
        #     # Handle the case when hsc_percentage is not provided or empty
        #     academic_scores['HSC Percentage'] = 0.0  # You can set a default value or handle it differently

        academic_scores['Rest'] = int(100) - int(hsc_percentage)

    elif education_level == 'Graduation':
        cgpa = int(request.form.get('graduation_cgpa'))
        academic_scores['CGPA'] = cgpa
        academic_scores['Rest'] = int(10) - int(cgpa)

    # Generate the pie chart for academic scores
    academic_labels, academic_values = zip(*academic_scores.items())
    plt.figure(figsize=(6, 6))
    plt.pie(academic_values, labels=academic_labels, autopct='%1.1f%%', startangle=140)
    plt.title('Academic Scores Distribution')
    academic_img = BytesIO()
    plt.savefig(academic_img, format='png')
    academic_img.seek(0)
    academic_img_base64 = base64.b64encode(academic_img.read()).decode()

    return render_template('test.html', academic_img_base64=academic_img_base64)


@app.route('/submit_test', methods=['POST'])
def submit_test():
    # Retrieve and process the test answers
    strengths = {}

    academic_img_base64 = request.form.get('academic_img_base64')

    for question, strength in strengths_map.items():
        answer = int(request.form.get(question))
        strengths[strength] = answer

    # Sort all strengths by their scores
    sorted_strengths = sorted(strengths.items(), key=lambda x: x[1], reverse=True)

    # Get the top 3 strengths
    top_strengths = sorted_strengths[:3]

    # match the top 3 strengths with the career profiles
    # if two or more strengths are matched, prioritize career options based on the number of matched skills
    matched_careers = []

    for career in career_profiles:
        count = 0
        for strength in top_strengths:
            if strength[0] in career['required_skills']:
                count += 1
                matched_careers.append((career['career_name'], count))

    # Sort the matched careers by the number of matched skills in descending order
    matched_careers.sort(key=lambda x: x[1], reverse=True)

    # Extract the career names from the sorted list
    sorted_careers = [career[0] for career in matched_careers]

    print(sorted_careers, count)
    # # remove duplicate careers
    # matched_careers = list(dict.fromkeys(matched_careers))

    # Calculate the scores for the other strengths
    # other_strengths = sorted_strengths[3:]

    # Generate the pie chart for strengths
    labels, values = zip(*sorted_strengths)
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Strengths Distribution')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.read()).decode()



    # Pass the results, pie charts, other strengths, and academic scores to the results template
    return render_template('results.html', top_strengths=top_strengths, img_base64=img_base64,
                           academic_img_base64=academic_img_base64, matched_careers=sorted_careers
                           )

@app.route('/GetInfo', methods=['POST'])
def GetInfo():
    Career_info = request.form.get('career_option')
    # now check the career info and display the career info
    career_Name = None
    required_qualifications = None
    required_skills = None
    industry = None

    for career in career_profiles:
        if Career_info == career['career_name']:
            career_Name = career['career_name']
            required_qualifications = career['required_qualifications']
            required_skills = career['required_skills']
            industry = career['industry']
            break

    print(career_Name, required_qualifications, required_skills, industry)
    return render_template('career_info.html', career_Name=career_Name, required_qualifications=required_qualifications, required_skills=required_skills, industry=industry)


if __name__ == '__main__':
    app.run(debug=True)
