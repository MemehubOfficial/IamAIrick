query_posts = '''
SELECT
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