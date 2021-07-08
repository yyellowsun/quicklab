# venv\Scripts\activate
# .\app.py
#yarn serve
#npm run lint 查看有没有错误
#python manage.py db migrate
#python manage.py db upgrade
#python manage.py db history
#python manage.py db downgrade
if __name__ == '__main__':
    from serverapi.application import create_app
    app=create_app()
    app.run()