from flask import Flask, render_template, request
import os
import cv2
import numpy as np
from tensorflow.python.ops.gen_math_ops import select
from predict import predict
app = Flask(__name__)

'''
모델에 넣기 위해
이미지 255*255 로 만들고 넣어야 함 
'''
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET','POST'])
def prediction():
    # if request.method == 'POST':
    # img = request.form.get('image')
    # print(img)
    file = request.files["image"] # 여기에 우리 업로드 되는 이름 넣으면 됨
    if 'file' not in request.files:
        return render_template('predict.html', label='No file')
    # if not file: return render_template('index.html', label="No Files")
    # img = cv2.imread(file).reshape(256,256,3)
    # # img = np.array(img.reshape(256,256,3))
    # label = predict(img)
    # print(label) label=label[0][1], prime=label[0][0]
    return render_template('predict.html' ,label=file)



if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)