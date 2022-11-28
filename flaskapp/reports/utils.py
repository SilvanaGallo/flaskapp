from flaskapp import db
from flaskapp.models import Report, Item


def json_from_db():
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def json_to_db():
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
                    sender='noreply@demo.com', 
                    recipients=[user.email])
    msg.body= f'''To reset your password, visit the following link:
                {url_for('users.reset_token', token=token, external=True)}
                If you did not make this request, simply ignore this message.'''
    mail.send(msg)