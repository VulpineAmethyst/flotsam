from django.db import models

class User(models.Model):
    email = models.EmailField(blank=False, unique=True)
    name = models.CharField(max_length=30, blank=False)
    tombstone = models.BooleanField(default=False)
    tombstone_reason = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    bio = models.TextField()

class Contact(models.Model):
    user = models.ForeignKey(User)
    service = models.CharField(60, blank=False)
    name = models.CharField(60, blank=False)
    visible = models.BooleanField(default=True)

class Folder(models.Model):
    user = models.ForeignKey(User)
    tombstone = models.BooleanField(default=False)
    tombstone_reason = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    name = models.CharField(120, blank=False)
    blurb = models.TextField(blank=False)
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Post(models.Model):
    user = models.ForeignKey(User)
    tombstone = models.BooleanField(default=False)
    tombstone_reason = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    title = models.CharField(120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

class Report(models.Model):
    user = models.ForeignKey(User)
    reason = models.TextField(blank=False)
    post = models.ForeignKey(Post, null=True)
    folder = models.ForeignKey(Folder, null=True)

class Role(models.Model):
    """General permissions as assignable roles."""
    name = models.CharField(30)
    # ability to view the site
    site_view  = models.BooleanField(default=True)

    # Content
    # add posts
    post_add             = models.BooleanField(default=True)
    # delete posts
    post_tombstone       = models.BooleanField(default=True)
    post_tombstone_other = models.BooleanField(default=True)
    # add folders
    folder_add           = models.BooleanField(default=True)
    # delete folders
    folder_tombstone     = models.BooleanField(default=True)

    # User
    user_tombstone      = models.BooleanField(default=False)
    # manipulate contact info
    contactable         = models.BooleanField(default=True)
    contactable_others  = models.BooleanField(default=False)
    profile_visible     = models.BooleanField(default=True)
    # editable
    profile_locked      = models.BooleanField(default=False)
    profile_lock_others = models.BooleanField(default=False)
    # can bypass email verification
    email_verify_bypass = models.BooleanField(default=False)
    # create users; does not bypass email verification
    user_add            = models.BooleanField(default=False)

    # Report
    report_add  = models.BooleanField(default=True)
    # can view reports
    report_view = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
