import os

def image_validation_extension(value):
    from django.core.exceptions import ValidationError
    img_extention = os.path.splitext(value.name)[1]#return path file name
    valid_img_extentions = ['.jpg', '.png', 'gif','jpeg','webp']
    if not img_extention.lower() in valid_img_extentions:
        raise ValidationError(u'Unsupported file extention.')

def video_validation_extention(value):
    from django.core.exceptions import ValidationError
    vid_extention = os.path.splitext(value.name)[1] #return name of if file from the path
    valid_vid_extentions = ['.mp4', '.ogg', '.webm', '.mp3']
    if not vid_extention.lower() in valid_vid_extentions:
        raise ValidationError(u'Unsupported video extention.')


