from kernel import route

# User
route.post('/register', 'User@register')
route.post('/login', 'User@login')
route.get('/hello', 'User@hello')


# Flag
route.post('/flags', 'Flag@create')
route.delete('/flags/<flag_id>', 'Flag@delete')
route.put('/flags/<flag_id>', 'Flag@update')
route.get('/flags', 'Flag@index')
route.get('/flags/<flag_id>', 'Flag@show')
