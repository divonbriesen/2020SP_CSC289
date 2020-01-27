from flask import Blueprint

from .auth import login_required

bp = Blueprint('stocks', __name__, url_prefix='/stocks')


# route example -- domain.tld/stocks/AAPL
@bp.route('/<string:id>')
def get_stock(id):
    """
    Display details for a stock.

    :param id: the stock symbol
    :return: a template for displaying the details of a stock.
    """
    pass


@bp.route('/<string:id>/buy', methods=('POST',))
@login_required
def buy_stock(id):
    """
    The API endpoint to buy stock.

    throw errors on
        incorrect symbol
        insufficient funds

    :param id: the stock symbol
    :return: a template for displaying the details of a stock.
    """

    # verify correct params

    # check for insufficient funds

    pass


@bp.route('/<string:id>/sell', methods=('POST',))
@login_required
def sell_stock(id):
    """
    The API endpoint to sell stock.

    throw error on
        invalid quantity (i.e trying to sell more than owns)
        market closed

    """

    pass
