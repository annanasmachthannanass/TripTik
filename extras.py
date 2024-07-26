# @app.route('/bucketlist', methods=['GET', 'POST'])
# def bucketlist_clicked():
#     return render_template('bucketlist.html')

# @app.route('/quizzes', methods=['GET','POST'])
# def quizzes_clicked():
#     return render_template('quizzes.html')

# # Albanien Quiz-Seite
# @app.route('/albanien', methods=['GET', 'POST'])
# def albanien():
    
#    ## if request.method == 'GET':
#     q1_answer = request.form.get('q1')
#     q2_answer = request.form.get('q2')
#     q3_answer = request.form.get('q3')

#     score = 0
#     if q1_answer == 'a':
#         score += 1
#     if q2_answer == 'c':
#         score += 1
#     if q3_answer == 'a':
#         score += 1

#     return render_template('quiz_seiten/albanien.html')
#     ##return render_template('quiz_results.html', score=score)

# @app.route('/quizresults', methods=['POST'])
# def quiz_result():
#     return render_template('quiz_results.html')

# @app.route('/deutschland', methods=['POST'])
# def deutschland():
#     return render_template('quiz_seiten/deutschland.html')

# @app.route('/finnland', methods=['POST'])
# def finnland():
#     return render_template('quiz_seiten/finnland.html')

# @app.route('/frankreich', methods=['POST'])
# def frankreich():
#     return render_template('quiz_seiten/frankreich.html')

# @app.route('/grossbritannien', methods=['POST'])
# def grossbritannien():
#     return render_template('quiz_seiten/grossbritannien.html')

# @app.route('/italien', methods=['POST'])
# def italien():
#     return render_template('quiz_seiten/italien.html')

# @app.route('/norwegen', methods=['POST'])
# def norwegen():
#     return render_template('quiz_seiten/norwegen.html')

# @app.route('/oesterreich', methods=['POST'])
# def oesterreich():
#     return render_template('quiz_seiten/oesterreich.html')

# @app.route('/polen', methods=['POST'])
# def polen():
#     return render_template('quiz_seiten/polen.html')

# @app.route('/portugal', methods=['POST'])
# def portugal():
#     return render_template('quiz_seiten/portugal.html')

# @app.route('/spanien', methods=['POST'])
# def spanien():
#     return render_template('quiz_seiten/spanien.html')

# @app.route('/schweiz', methods=['POST'])
# def schweiz():
#     return render_template('quiz_seiten/schweiz.html')

# @app.route('/schweden', methods=['POST'])
# def schweden():
#     return render_template('quiz_seiten/schweden.html')


# @app.route('/stickerbuch', methods=['GET', 'POST'])
# def stickerbuch():
#     return render_template('stickerbuch.html')
