--  list all genres not linked to the show Dexte
SELECT tv_genres.name  FROM tv_genres
LEFT JOIN (SELECT show_id
	FROM tv_shows
	tv_shows
	WHERE ``)
AS dexter_shows ON tv_genres.id = dexter_shows.show_id
WHERE dexter_shows.show_id IS NULL
ORDER BY tv_genres.name ASC;
