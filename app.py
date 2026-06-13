from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # File ka full path batate hain
    file_path = os.path.join(os.path.dirname(__file__), 'templates', 'snake.html')
    with open(file_path, 'r') as f:
        return f.read()

if __name__ == '__main__':
    app.run()