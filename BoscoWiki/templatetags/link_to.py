from django import template

register = template.Library()

@register.inclusion_tag('customtags/link_to.html', )
def link_to(namesp, view='', id_link=None, name='', cl='', icon=''):
	'''
	link_to(namespace, view, id(optional), name or value, class(optional), icon(optionl))
	'''
	return {
		'link': '/'+str(namesp)+'/'+(str(view)),
		'id':  id_link,
		'name': name,
		'class': cl,
		'icon': icon,
	}