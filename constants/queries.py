#define static queries
from constants.cleaners import *
import stringutils

#query posts no older than 7 days that have a downvote
#return the url, active votes, and pending payout of posts
def query_posts():
	q = '''
		SELECT
			url,
			CAST(active_votes AS NTEXT) as votes,
			total_pending_payout_value
		FROM
			Comments
			INNER JOIN TxVotes ON 
				TxVotes.author = Comments.author AND TxVotes.permlink = Comments.permlink
				AND TxVotes.voter IN (''' + '\''+ '\',\''.join(cleaners) + '\'' + ''')
				AND TxVotes.weight < 0
		WHERE
			Comments.depth = 0
			AND Comments.created > DATEADD(day, -7, GETUTCDATE())
		'''
	return q