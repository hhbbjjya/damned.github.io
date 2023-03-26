from flask import Flask,render_template,request,redirect,url_for
import openai

openai.api_key = "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"

app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method =='POST':
        if request.values['send']=='送出':
            model = "text-davinci-003" #模組
            # prompt = request.values['user'] #問題
            completions = openai.Completion.create(
                engine=model,
                prompt=request.values['user'],
                max_tokens=1024,
                temperature=1,
                top_p=0.75,                   
                n=1,
            )
            message = completions.choices[0].text
        return render_template('index.html',name=message)
    return render_template('index.html',name="")

if __name__ == '__main__':
	app.run(debug=True)
