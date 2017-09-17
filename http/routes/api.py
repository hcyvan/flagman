from kernel import route

# User
route.post('/register', 'User@register')
route.post('/login', 'User@login')


# Flag
route.post('/flags', 'Flag@create')
# route.delete('/flags/:id', 'Flag@delete')
# route.put('/flags/:id', 'Flag@update')
# route.get('/flags', 'Flag@index')
# route.get('/flags/:id', 'Flag@show')
