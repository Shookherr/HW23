# Домашняя работа №23. Шумихин Алексей. 08.02.23
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=25000)
