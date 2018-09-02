'''

To generate a Auth-token:
curl -X POST -d "username=your_username&password=your_password" http://localhost:8000/api/auth/token/

To create a post, you must be authenticated. So do like this:

curl -H "Authorization: JWT <your_token>" http://localhost:8000/api/posts/create

To post a comment, you have to pass the following parameters:
1. slug
2. type (ex. post)
3. parent_id (optional. But if you post a reply to a comment, it's required.)

To post a comment:
Example: curl -X POST -H "Authorization: JWT <your_token_here>" -H "Content-Type: application/json" -d '{"content":"This is a comment."}' 'http://localhost:8000/api/comments/create/?slug=the-slug-of-the-post&type=post'

To post a reply:
Example: curl -X POST -H "Authorization: JWT <your_token_here>" -H "Content-Type: application/json" -d '{"content":"This is a comment."}' 'http://localhost:8000/api/comments/create/?slug=the-slug-of-the-post&type=post&parent_id=id_of_the_comment'


'''

