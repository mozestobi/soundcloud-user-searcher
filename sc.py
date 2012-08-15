import soundcloud
import sys

client = soundcloud.Client(client_id='f3b669e6e4509690939aed943c56dc99',
                           client_secret='52a199768a2a6b4eebb4457b945e8725',
                           redirect_uri='https://soundcloud.com/connect')
						   

try:
 users = client.get('/users', q = raw_input())
except:
	print 'There is no match'
	sys.exit()
for user in users:
    
	followerscore = user.followers_count;
	#print 'followers: '+str(followerscore);
 	followers = client.get('/users/'+str(user.id)+'/followers');
	for follower in followers:
		followerscore += follower.followers_count - follower.followings_count;
		#print 'followers_of_followerscount: '+str(follower.followers_count);
		#print 'followees_of_followerscount: '+str(follower.followings_count)
	print 'Followerscore of '+user.username+': '+str(followerscore)
	

