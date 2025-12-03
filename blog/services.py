from .models import Post


# Service functions for blog operations

# Get all posts, ordered by creation date descending
def get_all_posts():
    objects = Post.objects.all()
    return objects.order_by('-created_at')

# Create a new post
def create_post(title, author, content):
    post = Post(title = title, author = author, content = content)
    post.save()
    return post

# Update an existing post
def update_post(post_id, title=None, author=None, content=None):
    try:
        post = Post.objects.get(id=post_id)
        if title is not None:
            post.title = title
        if author is not None:
            post.author = author
        if content is not None:
            post.content = content
        post.save()
        return post
    except Post.DoesNotExist:
        return None
    
# Delete a post
def delete_post(post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return True
    except Post.DoesNotExist:
        return False