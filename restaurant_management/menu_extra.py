from django import template
 register=template.Libary()

 @register.filter
 def availability_label(item):
    if hasattr(item,"availabile")and not item.availabile:
        return "comming soon"
    return f"${ item.price}"