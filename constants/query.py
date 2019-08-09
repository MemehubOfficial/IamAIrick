#define static queries
from constants.cleaners import *

#query posts no older than 7 days that have a downvote
#approx min 6 query run time
def posts_cleaner_vote():
	q = '''
		SELECT
			url,
			Comments.author,
			Comments.permlink,
			category,
			title,
			body,
			json_metadata,
			created,
			total_payout_value,
			total_pending_payout_value,
			CAST(active_votes AS NTEXT) as votes,
			CONVERT(int,(SELECT MAX(v) FROM (VALUES(log10(ABS(CONVERT(bigint,author_reputation)-1)) - 9),(0)) T(v)) * SIGN(author_reputation) * 9 + 25) as rep,
			body_length
		FROM
			Comments
			INNER JOIN TxVotes ON 
				TxVotes.author = Comments.author AND TxVotes.permlink = Comments.permlink
				AND TxVotes.voter IN ('steemflagrewards')
		WHERE
			Comments.depth = 0
			AND Comments.created > DATEADD(day, -14, GETUTCDATE())
		'''
	return q

#query comments on a post
def cleaner_comments_on_post(parent_author, parent_permlink):
	q = '''
		SELECT
			Comments.author,
			Comments.permlink,
			url,
			body,
			json_metadata,
			created,
			total_payout_value,
			total_pending_payout_value,
			CAST(active_votes AS NTEXT) as votes,
			replies,
			body_length
		FROM
			Comments
		WHERE
			Comments.parent_author = '''+'\'' +parent_author+'\'' +'''
			AND Comments.parent_permlink = '''+'\'' +parent_permlink+'\'' +'''
			AND Comments.author IN (''' + '\''+ '\',\''.join(cleaners) + '\'' + ''')
		'''
	return q