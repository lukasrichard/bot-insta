from inspect import findsource
from instapy import InstaPy
from instapy import smart_run

insta_username = '@anais_chrd'
insta_password = findsource

session = InstaPy(
    username=insta_username,
	password=insta_password,
	headless_browser=True)  

with smart_run(session):
    
    session.set_relationship_bounds(
	    enabled=True,
		delimit_by_numbers=True,
		max_followers=5000,
		min_followers=50,
		min_following=100)


    

    
    session.set_do_follow(True, percentage=20)

    
    session.set_do_comment(enabled=True, percentage=80)

