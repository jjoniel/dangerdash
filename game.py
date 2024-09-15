from flask import Flask, render_template, redirect, url_for
from parser import Parser 

app = Flask(__name__)

parser = Parser()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fire')
def fire_emergency():
    parser.parse("FIRE")
    return render_template('emergency.html',
                           title="Fire Emergency",
                           story=parser.story,
                           option1=parser.option1.get('op1'),
                           option1res=parser.option1.get('op1_res'),
                           option2=parser.option2.get('op2'),
                           option2res=parser.option2.get('op2_res'),
                           option11=parser.option1.get('op1a'),
                           option12=parser.option1.get('op1b'),
                           option21=parser.option2.get('op2a'),
                           option22=parser.option2.get('op2b'),
                           option11res=parser.option1.get('op1a_res'),
                           option12res=parser.option1.get('op1b_res'),
                           option21res=parser.option2.get('op2a_res'),
                           option22res=parser.option2.get('op2b_res'),
                           option11val=parser.option1.get('op1ao'),
                           option12val=parser.option1.get('op1bo'),
                           option21val=parser.option2.get('op2ao'),
                           option22val=parser.option2.get('op2bo'),
                           img="fire.png")

@app.route('/earthquake')
def earthquake_emergency():
    parser.parse("EARTHQUAKE")
    return render_template('emergency.html',
                           title="Earthquake Emergency",
                           story=parser.story,
                           option1=parser.option1.get('op1'),
                           option1res=parser.option1.get('op1_res'),
                           option2=parser.option2.get('op2'),
                           option2res=parser.option2.get('op2_res'),
                           option11=parser.option1.get('op1a'),
                           option12=parser.option1.get('op1b'),
                           option21=parser.option2.get('op2a'),
                           option22=parser.option2.get('op2b'),
                           option11res=parser.option1.get('op1a_res'),
                           option12res=parser.option1.get('op1b_res'),
                           option21res=parser.option2.get('op2a_res'),
                           option22res=parser.option2.get('op2b_res'),
                           option11val=parser.option1.get('op1ao'),
                           option12val=parser.option1.get('op1bo'),
                           option21val=parser.option2.get('op2ao'),
                           option22val=parser.option2.get('op2bo'),
                           img="earthquake.png")

@app.route('/epidemic')
def epidemic_emergency():
    parser.parse("EPIDEMIC")
    return render_template('emergency.html',
                           title="Epidemic Emergency",
                           story=parser.story,
                           option1=parser.option1.get('op1'),
                           option1res=parser.option1.get('op1_res'),
                           option2=parser.option2.get('op2'),
                           option2res=parser.option2.get('op2_res'),
                           option11=parser.option1.get('op1a'),
                           option12=parser.option1.get('op1b'),
                           option21=parser.option2.get('op2a'),
                           option22=parser.option2.get('op2b'),
                           option11res=parser.option1.get('op1a_res'),
                           option12res=parser.option1.get('op1b_res'),
                           option21res=parser.option2.get('op2a_res'),
                           option22res=parser.option2.get('op2b_res'),
                           option11val=parser.option1.get('op1ao'),
                           option12val=parser.option1.get('op1bo'),
                           option21val=parser.option2.get('op2ao'),
                           option22val=parser.option2.get('op2bo'),
                           img="epidemic.png")

@app.route('/stranger')
def stranger_danger():
    parser.parse("STRANGER")
    return render_template('emergency.html',
                           title="Stranger Danger",
                           story=parser.story,
                           option1=parser.option1.get('op1'),
                           option1res=parser.option1.get('op1_res'),
                           option2=parser.option2.get('op2'),
                           option2res=parser.option2.get('op2_res'),
                           option11=parser.option1.get('op1a'),
                           option12=parser.option1.get('op1b'),
                           option21=parser.option2.get('op2a'),
                           option22=parser.option2.get('op2b'),
                           option11res=parser.option1.get('op1a_res'),
                           option12res=parser.option1.get('op1b_res'),
                           option21res=parser.option2.get('op2a_res'),
                           option22res=parser.option2.get('op2b_res'),
                           option11val=parser.option1.get('op1ao'),
                           option12val=parser.option1.get('op1bo'),
                           option21val=parser.option2.get('op2ao'),
                           option22val=parser.option2.get('op2bo'),
                           img="stranger.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
