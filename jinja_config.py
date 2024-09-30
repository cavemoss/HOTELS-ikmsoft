from fastapi.templating import Jinja2Templates
from markupsafe import Markup

templates = Jinja2Templates(directory='templates')

def set_vars(template_name, **kwargs):
    template = templates.env.get_template(template_name)
    rendered = template.render(**kwargs)
    return  Markup(rendered)

templates.env.filters['set_vars'] = set_vars
