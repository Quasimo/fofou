'''
Configuration File

Setup this file according to your application Models as to map their
attributes to the equivalent atom elements.
'''

'''
gae-rest needs to import the files containing your Models since it is
unable to dynamic infer what are all the available entity kinds
(content types) in your application
Example: models = ['my_models.py', 'my_expandos.py']
'''
models = ['main.py']

'''
which attribute on each Entity can be used as atom <author> element
Example: author = {'Entry': 'author'}
'''
author = {'FofouUser':'user', 'Topic':'created_by', 'Post':'user_email'}

'''
<title>
Example: title = {'Entry': 'title'}
'''
title = {'FofouUser':'name', 'Forum':'title', 'Topic':'subject', 'Post':'sha1_digest'}

'''
<content>
Example: content = {'Entry': 'body_html'}
'''
content = {'Post':'message'}

'''
<summary>
Example: summary = {'Entry': 'excerpt'}
'''
summary = {'Forum':'tagline', 'Post':'message'}

'''
<published>
Example: published = {'Entry': 'published'}
'''
published = {'Forum':'created_on', 'Topic':'created_on', 'Post':'created_on'}

'''
<updated>
Example: updated = {'Entry': 'updated'}
'''
updated = {'Topic':'updated_on'}