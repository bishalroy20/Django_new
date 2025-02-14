from django.shortcuts import render
from datetime import datetime , timedelta

def home(request):
    current_datetime = datetime.now()
    multi_line_string = """ one.
                        two.
                        three."""
    
    blog_date = datetime.now() - timedelta(days=2)
    comment_date = datetime.now() - timedelta(hours=7)


    d = {
        'variable': 'phitron',
        'value': '50',
        'author': "I'm Bishal",
        'line': 'Cut The Spaces Of This Line',
        'date': current_datetime,
        'text' : '',
        'lst' : ['Banana', 'Mango', 'Orange'] ,
        'dd' : [
            {'name': 'zx', 'age': 19},
            {'name': 'def', 'age': 22},
            {'name': 'ghi', 'age': 31},
        ] ,
        'multiline' : multi_line_string ,

        'blog_date': blog_date,
        'comment_date': comment_date,

    }
    return render(request, 'index.html', d)

