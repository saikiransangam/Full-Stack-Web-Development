import media
import netflix_shows


def run():
    """ Generate and open the movies listing html page """
    netflix_shows.open_movies_page(
            get_movie_list(),
            "Netflix TV Shows")


def get_movie_list():
    """ Retrieve a list of movies """
    return [media.Movie(
                "Ozark",
                "https://www.gstatic.com/tv/thumb/tvbanners/15668760/p15668760_b_v8_aa.jpg",
                "https://www.youtube.com/watch?v=5hAXVqrljbs"),
            media.Movie(
                "D A R K",
                "https://qph.fs.quoracdn.net/main-qimg-2c762cdf2a89543fb4993ae02387a50e",
                "https://www.youtube.com/watch?v=cq2iTHoLrt0"),
            media.Movie(
                "Breaking Bad",
                "https://m.media-amazon.com/images/M/MV5BMjhiMzgxZTctNDc1Ni00OTIxLTlhMTYtZTA3ZWFkODRkNmE2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
                "https://www.youtube.com/watch?v=HhesaQXLuRY"),
            media.Movie(
                "Money Heist",
                "https://m.media-amazon.com/images/M/MV5BZDcxOGI0MDYtNTc5NS00NDUzLWFkOTItNDIxZjI0OTllNTljXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                "https://www.youtube.com/watch?v=p_PJbmrX4uk"),
            media.Movie(
                "Stranger Things",
                "https://m.media-amazon.com/images/M/MV5BZGExYjQzNTQtNGNhMi00YmY1LTlhY2MtMTRjODg3MjU4YTAyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                "https://www.youtube.com/watch?v=mnd7sFt5c3A"),
            media.Movie(
                "13 reasons why",
                "https://cdn.shopify.com/s/files/1/0747/3829/products/mL0908_426c10fb-2c3f-4fc6-b0f6-e6101ee18c80.jpg?v=1571445243",
                "https://www.youtube.com/watch?v=poUq9ypynKs"),
            media.Movie(
                "The Stranger",
                "https://d2e111jq13me73.cloudfront.net/sites/default/files/styles/product_image_aspect_switcher_170w/public/product-images/csm-tv/thestranger-tv-poster-image.jpg?itok=q5cm4fgP",
                "https://www.youtube.com/watch?v=fwUWlxAQj-o"),
            media.Movie(
                "You",
                "https://upload.wikimedia.org/wikipedia/en/thumb/c/c6/You_Season_1.jpg/220px-You_Season_1.jpg",
                "https://www.youtube.com/watch?v=ga1m0wjzscU"),
            media.Movie(
                "Unbelievable",
                "https://www.gstatic.com/tv/thumb/tvbanners/17173880/p17173880_b_v8_ab.jpg",
                "https://www.youtube.com/watch?v=QTIkUzkbzQk"),
            media.Movie(
                "The Witcher",
                "https://www.gstatic.com/tv/thumb/tvbanners/17580215/p17580215_b_v8_ac.jpg",
                "https://www.youtube.com/watch?v=cSqi-8kAMmM"),
            media.Movie(
                "orange is the new black",
                "https://images-na.ssl-images-amazon.com/images/I/61X1hp%2BOtZL._SL1100_.jpg",
                "https://www.youtube.com/watch?v=vY0qzXi5oJg"),
            media.Movie(
                "Mindhunter",
                "https://www.gstatic.com/tv/thumb/tvbanners/17153590/p17153590_b_v8_ab.jpg",
                "https://www.youtube.com/watch?v=LR3G1lWbnUU")]


run()
