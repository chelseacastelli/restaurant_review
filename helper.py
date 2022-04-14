from math import ceil

def calculate_average_rating(restaurant):
    ratings = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0
    }
    
    for review in restaurant.reviews:
        ratings[review.rating] += 1
    
    avg = ((1 * ratings[1]) + (2 * ratings[2]) + (3 * ratings[3]) + (4 * ratings[4]) + (5 * ratings[5])) / restaurant.num_reviews
    return ceil(avg * 10) / 10
