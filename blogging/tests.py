from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post, Category
import datetime
from django.utils.timezone import utc
# import pysnooper


class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setUp(self):
        self.users = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    """test views provided in the front-end"""
    fixtures = ['blogging_test_fixture.json', ]

    # @pysnooper.snoop(depth=2)
    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)  # spaces out the test posts by 15 seconds
        author = User.objects.get(pk=1)  # this uses the pre-setup users in the test_fixture file where primary key = 1
        for count in range(1, 11):
            post = Post(title=f"Post {count} Title",  # creating an instance of the Post table
                        text="foo",
                        author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()


    def test_list_only_published(self):
        resp = self.client.get('/')
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("My Cool BLog Posts" in resp_text)
        for count in range(1, 11):
            title = f"Post {count} Title"
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    # @pysnooper.snoop(depth=3)
    def test_details_only_published(self):
        for count in range(1, 11):
            title = f"Post {count} Title"
            post = Post.objects.get(title=title)
            resp = self.client.get(f'/posts/{post.pk}/')
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)
