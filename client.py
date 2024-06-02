def getDataPoint(quote):
    """ Calculates price and returns it.
    :param quote: A dictionary containing the quote data
    :return: The calculated price
    """
    stock = quote['stock']
    bid_price = quote['top_bid']['price']
    ask_price = quote['top_ask']['price']
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price
