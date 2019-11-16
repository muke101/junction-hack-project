from flask_swagger_ui import get_swaggerui_blueprint

def initSwagger(app):
    swagger_url = '/swagger'
    api_url = '/static/swagger.json'
    blueprint = get_swaggerui_blueprint(
        swagger_url,
        api_url,
        config={
            'app_name': 'test name'
        }
    )
    app.register_blueprint(blueprint,url_prefix=swagger_url)

