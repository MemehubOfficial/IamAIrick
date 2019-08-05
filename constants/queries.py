#define static queries

#query posts no older than 7 days that have a downvote
#return the url, active votes, and pending payout of posts
query_posts = '''
SELECT TOP 10
	url,
    CAST(active_votes AS NTEXT) as votes,
    total_pending_payout_value
FROM
	Comments
	INNER JOIN TxVotes ON 
		TxVotes.author = Comments.author AND TxVotes.permlink = Comments.permlink
        AND TxVotes.weight < 0
WHERE
	Comments.depth = 0
	AND Comments.created > DATEADD(day, -7, GETUTCDATE())
'''