先cmd到目录，直接运行Scripts\activate，和conda activate是一样的，这里用的是venv

如何access database？
from flaskblog import create_app, db
from flaskblog.models import User,Post

app=create_app()
app.app_context().push()
User.query.all()
...

若要删除所有：
db.drop_all()
db.create_all()
记住create_all()很重要！是初始化db的重要一步

youtube原网址：https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2

