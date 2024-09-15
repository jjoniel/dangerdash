from flask import Flask, render_template, redirect, url_for
from parser import Parser  # Assuming Parser is the same as in your original code

app = Flask(__name__)

# Initialize parser
parser = Parser()

@app.route('/')
def home():
    # Main menu
    return render_template('index.html')

@app.route('/fire')
def fire_emergency():
    # Parse the fire scenario
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
                           img="fire.png")

@app.route('/earthquake')
def earthquake_emergency():
    # Parse the earthquake scenario
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
                           img="earthquake.png")

@app.route('/stranger')
def stranger_danger():
    # Parse the stranger danger scenario
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
                           img="stranger.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
