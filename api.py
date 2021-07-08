from flask_restplus import Api


api = Api(
    version='1.0',
    title='University API',
    contact_email='matijannello@gmail.com',
    description=(
        'API to manage university users, subjects and grades'
    ),
    validate=True
)



