from flask import Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app.posts.forms import PostForm,CommentsForm
from app.models import Posts,Comments,Subscribers
from app import db, mail
from flask_mail import  Message
from flask import render_template, url_for, flash, redirect, request
from app.users.utils import save_postsImage,save_picture
posts= Blueprint('posts',__name__)

@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    form = PostForm()
    sub=Subscribers.query.all()
    if form.validate_on_submit():
        if form.blog_image.data:
            picture=save_postsImage(form.blog_image.data)
            post = Posts(title=form.title.data,
                        content=form.content.data,description=form.description.data, user_id=current_user.id,category=form.category.data,
                        blog_image=picture,
                        )
            topic=post.title
        
            db.session.add(post)  
            db.session.commit()          


            for s in sub:
             msg=Message("Blog Update",sender="apollolibrary99@gmail.com",recipients=[s.email])
             msg.body = "Have you read our newly updated blog called "+ topic +', be sure to check it out'
             mail.send(msg)
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
        edites.description=form.description.data

        db.session.add(edites)
        db.session.commit()
        flash('Your Post Has been updated!','success')
        return redirect(url_for("main.home"))
    else:
        form.title.data=edites.title
        form.content.data=edites.content
        form.category.data=edites.category
        form.description.data=edites.description
    return render_template('edit.html',form=form)

@posts.route('/post/delete/<postid>')
def post_delete(postid):
    post = Posts.query.filter_by(id=postid).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.home'))

@posts.route('/post/<postid>')
def reads(postid):

    reads= Posts.query.filter_by(id=postid).first()

    image_file= url_for('static',filename='posts/'+reads.blog_image)

    return render_template('reads.html', reads=reads,image_file=image_file)
    

@posts.route('/comments/<id>',methods=['POST', 'GET'])
def comments(id):
    form = CommentsForm()
    posts = Posts.query.filter_by(id=id).first()
    if form.validate_on_submit():
        comment=Comments(comment=form.content.data,post_id=posts.id)
        # posts.comments+=form.content.data + '~'
        db.session.add(comment)
        db.session.commit()
        flash('Your comment was added successfully','success')
        
        return redirect(url_for('main.home'))
    form.content.data = "Your comment here"
    return render_template('comments.html', form=form , posts=posts)


@posts.route('/comment/delete/<id>')
def comment_delete(id):
    comm = Comments.query.filter_by(id=id).first()
    
    db.session.delete(comm)
    db.session.commit()
    flash('Your comment was deleted successfully','success')

    return redirect(url_for('main.home'))