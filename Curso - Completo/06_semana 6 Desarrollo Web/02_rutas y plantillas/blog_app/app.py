from flask import Flask, render_template, request
from data import posts  # 👈 Importamos desde data.py

app = Flask(__name__)

@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    per_page = 3

    start = (page - 1) * per_page
    end = start + per_page

    paginated_posts = posts[start:end]
    total_pages = (len(posts) + per_page - 1) // per_page

    return render_template(
        'index.html',
        posts=paginated_posts,
        page=page,
        total_pages=total_pages
    )

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return render_template('post.html', post= post)
    return "<h1>Post Not Found</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)