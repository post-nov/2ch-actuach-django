from django.db import models
from posts.models import Post


def counter(files, types):
    c = 0
    for file in files:
        if any(obj in file for obj in types):
            c += 1
    return c


class Media(Post):

    class Meta:
        proxy = True

    imgs_types = ['.jpg', '.png']
    video_types = ['.webm', '.mp4']
    post_files = Post.files

    def count_images(self):
        return counter(self.post_files, self.imgs_types)

    def count_videos(self):
        return counter(self.post_files, self.video_types)
