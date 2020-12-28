from tornado_swagger.components import components


@components.schemas.register
class UserModel(object):
    """
    ---
    type: object
    description: User model representation
    properties:
        id:
            type: integer
            format: int64
        name:
            type: string
        is_visible:
            type: boolean
            default: true
    """