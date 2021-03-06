#define static queries
import pandas as pd
import config
from constants.bidbots import bidbots

#updates array of bidbot acct names and loads it
bidbots = bidbots()

#query posts no older than 7 days that have a downvote
#approx min 6 query run time
def posts_cleaner_downvoted():
	q = '''
		SELECT
			url,
			Comments.author,
			Comments.permlink,
			category,
			title,
			body,
			CAST(json_metadata AS NTEXT) as json_metadata,
			created,
			total_payout_value,
			total_pending_payout_value,
			CAST(active_votes AS NTEXT) as votes,
			CONVERT(int,(SELECT MAX(v) FROM (VALUES(log10(ABS(CONVERT(bigint,author_reputation)-1)) - 9),(0)) T(v)) * SIGN(author_reputation) * 9 + 25) as rep,
			body_length,
			TxVotes.weight as weight,
		FROM
			Comments
			INNER JOIN TxVotes ON 
				TxVotes.author = Comments.author AND TxVotes.permlink = Comments.permlink
				AND TxVotes.voter IN (''' + '\''+ '\',\''.join(config.cleaners) + '\'' + ''')
				AND TxVotes.weight < 0
		WHERE
			Comments.depth = 0
			AND Comments.created > DATEADD(day, -14, GETUTCDATE())
		'''
	return q


def memes_bidbotted():
	q = '''
		SELECT DISTINCT
			Comments.author,
			Comments.permlink,
			pending_payout_value,
			total_pending_payout_value,
			CONVERT(int,(SELECT MAX(v) FROM (VALUES(log10(ABS(CONVERT(bigint,author_reputation)-1)) - 9),(0)) T(v)) * SIGN(author_reputation) * 9 + 25) as rep,
			body_length
		FROM
			Comments
			INNER JOIN TxVotes ON
				TxVotes.author = Comments.author
				AND TxVotes.permlink = Comments.permlink
				AND TxVotes.voter IN (''' + '\''+ '\',\''.join(bidbots) + '\'' + ''')
		WHERE
			Comments.depth = 0
			AND Comments.created < DATEADD(minute, -15, GETUTCDATE())
			AND Comments.created > DATEADD(day, -7, GETUTCDATE())
			AND Comments.category IN (''' + '\''+ '\',\''.join(config.meme_tags) + '\'' + ''')
			AND pending_payout_value > 5
		ORDER BY pending_payout_value DESC
		'''
	print(q)
	return q

def posts_by_voter(voter):
	q = '''
		SELECT
			url,
			Comments.author,
			Comments.permlink,
			category,
			title,
			body,
			CAST(json_metadata AS NTEXT) as json_metadata,
			created,
			total_payout_value,
			total_pending_payout_value,
			CAST(active_votes AS NTEXT) as votes,
			CONVERT(int,(SELECT MAX(v) FROM (VALUES(log10(ABS(CONVERT(bigint,author_reputation)-1)) - 9),(0)) T(v)) * SIGN(author_reputation) * 9 + 25) as rep,
			body_length,
			TxVotes.weight as weight
		FROM
			Comments
			INNER JOIN TxVotes ON 
				TxVotes.author = Comments.author AND TxVotes.permlink = Comments.permlink
				AND TxVotes.voter = '''+'\''+voter+'\''+'''
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
			CAST(json_metadata AS NTEXT) as json_metadata,
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
			AND Comments.author IN (''' + '\''+ '\',\''.join(config.cleaners) + '\'' + ''')
		'''
	return q