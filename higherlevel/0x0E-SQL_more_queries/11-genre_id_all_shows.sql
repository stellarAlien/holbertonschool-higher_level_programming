-- lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_show.title, tv_show_genres.genre_id
FROM tv_shows 
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_show.title, tv_shows.genre_id
