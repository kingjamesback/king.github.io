from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

# 업로드된 파일이 저장될 경로
app.config['UPLOAD_FOLDER'] = 'uploads'

# 업로드된 파일이 저장될 경로가 존재하지 않으면 디렉토리 생성
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # 업로드된 파일 가져오기
    file = request.files['file']

    # 파일 저장 경로 생성
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # 파일 저장
    file.save(filepath)

    # 업로드된 파일을 보여줄 HTML 페이지로 리다이렉트
    return redirect(url_for('show_image', filename=file.filename))

@app.route('/uploads/<filename>')
def show_image(filename):
    # 저장된 파일 경로
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # 저장된 파일을 읽어서 보내주기
    return send_file(filepath, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
