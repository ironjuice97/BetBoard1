import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


load_dotenv()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)