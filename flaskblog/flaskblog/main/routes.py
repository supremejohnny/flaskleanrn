from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

# app.app_context().push()

    
# posts = [
#     {
#         'author': 'Corey ss',
#         'title': 'Blog Post 1',
#         'content': 'this is 1 page',
#         'date-posteed': '2020.1.2'
#     },
#     {
#         'author': 'Author 2',
#         'title': 'Blog post 2',
#         'content': 'this is 2 page',
#         'date-posteed': '2020.1.3'
#     }
    
# ]

@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title="About page")