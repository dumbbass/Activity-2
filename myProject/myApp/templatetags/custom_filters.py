from django import template
import locale

register = template.Library()

@register.filter
def currency_format(value):
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        if isinstance(value, str):
            value = float(value)
        return f"${locale.format_string('%.2f', value, grouping=True)}"
    except:
        return value 