from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts

client = Client('http://34.83.90.210/xmlrpc.php', '772051431@qq.com', 'm4+vAjCB')



post = WordPressPost()



def publish(title, description, content):
    post.title = title
    post.content = content
    post.custom_fields = []
    post.custom_fields.append({
            'key': '_yoast_wpseo_metadesc',
            'value': description
    })
    post.id = client.call(posts.NewPost(post))

    post.post_status = 'publish'
    r = client.call(posts.EditPost(post.id, post))
    return r