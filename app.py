from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from tomb_routes import simple_route as route


def get_listings():
    return [
        {
            'id': 'L1', 'name': 'Best listing ever', 'rooms': 3, 'price': 15,
            'street address': '111 Haunted Way', 'city': 'Savannah',
            'state': 'GA', 'zipcode': 31401, 'owner': 'U1',
            'reservations': ['R1'],
            'images': ['http://scoopotp.com/wp-content/uploads/2013/02/Historic-Savannah-and-Your-BluegreenTimeshare-Vacation.jpg'],
            'description': 'Stay here, Yo!'
        }
    ]

def get_users():
    return [
        {
            'id': 'U1', 'email': 'fake@gmail.com', 'name': 'User Number1',
            'listings': ['L1'], 'reservations': [],
            'password digest': 'abcdef1234'
        },
        {
            'id': 'U2', 'email': '2fake2@gmail.com', 'name': 'User Number2',
            'listings': [], 'reservations': ['R1'],
            'password digest': 'wdcdef1234'
        }
    ]

def get_reservations():
    return [
        {
            'id': 'R1', 'requester': 'U2', 'listing': 'L1', 'guests count': 3,
            'start day': '2016-01-01', 'end day': '2016-01-15', 'message': 'Hi'
        }
    ]

@route('/listings', renderer='json', accept='application/json')
#@route('/listings', renderer='__main__:listings.mako', accept='text/html')
def listings(request):
    data = get_listings()

    return {
        'listings': data
    }


if __name__ == '__main__':
    config = Configurator()
    config.include('tomb_routes')
#    config.include('pyramid_mako')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print('http://localhost:8080')
    server.serve_forever()
