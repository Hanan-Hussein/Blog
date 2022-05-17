from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app.posts.forms import PostForm
from app.models import Posts
from app import db
from flask import render_template, url_for, flash, redirect, request
from app.users.utils import save_postsImage,save_picture

posts= Blueprint('posts',__name__)



@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        if form.blog_image.data:
            picture=save_postsImage(form.blog_image.data)
            post = Posts(title=form.title.data,
                        content=form.content.data,description=form.description.data, user_id=current_user.id,category=form.category.data,
                        blog_image=picture,
                        )
        
            db.session.add(post)  
            db.session.commit()
            flash('Your pitch was successfully added','success')

            return redirect(url_for('main.home'))


        else:
          flash('Your pitch image was not added','danger')
          


    return render_template('create.html', form=form, title='New Post')




@posts.route('/categories/<category>')
def categories(category):
    posts = Posts.query.filter_by(category=category)
    for post in posts:
        image_file= url_for('static',filename='posts/'+post.blog_image)

        post.blog_image= image_file
    return render_template('categories.html', posts=posts)

@login_required
@posts.route('/post/edit/<postid>',methods=['POST', 'GET'])
def post_edit(postid):
    form = PostForm()

    edites= Posts.query.filter_by(id=postid).first()
    
    if form.validate_on_submit():
        edites.title = form.title.data
        edites.content=form.content.data
        edites.category=form.category.data
        
        db.session.add(edites)
        db.session.commit()
        flash('Your Pitch Has been updated!','success')
        return redirect(url_for("main.home"))
    else:
        form.title.data=edites.title
        form.content.data=edites.content
        form.category.data=edites.category
        
    return render_template('post_edit.html',form=form)

@posts.route('/post/delete/<pitchid>')
def post_delete(pitchid):
    pitch = Posts.query.filter_by(id=pitchid).first()
    db.session.delete(pitch)
    db.session.commit()
    return redirect(url_for('main.home'))

