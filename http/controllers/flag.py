from kernel.controller import Controller
from repo import flag_repo


class Flag(Controller):
    def create(self):
        title = self.json('title')
        content = self.json('content')
        address = self.json('address')
        people_number = self.json('people_number')
        start_time = self.json('start_time')
        lat = self.json('lat')
        lng = self.json('lng')

        if not title:
            return self.echo(201)
        if not content:
            return self.echo(202)
        if not address:
            return self.echo(203)
        if not people_number:
            return self.echo(204)
        if not start_time:
            return self.echo(205)
        if not lat:
            return self.echo(206)
        if not lng:
            return self.echo(207)

        flag_repo.create(title, content, address, people_number, start_time, lat, lng)

        return self.echo()

    def update(self, flag_id):
        title = self.json('title')
        content = self.json('content')
        address = self.json('address')
        people_number = self.json('people_number')
        start_time = self.json('start_time')
        lat = self.json('lat')
        lng = self.json('lng')

        flag = flag_repo.get_flag_by_id(flag_id)
        if not flag:
            return self.echo(208)
        flag_repo.update(flag, title, content, address, people_number, start_time, lat, lng)

        return self.echo()

    def delete(self, flag_id):
        flag = flag_repo.get_flag_by_id(flag_id)
        if not flag:
            return self.echo(208)

        flag_repo.delete(flag)

        return self.echo(0)

    def show(self, flag_id):
        flag = flag_repo.get_flag_by_id(flag_id)
        if not flag:
            return self.echo(208)

        return self.echo(0, flag.to_dict())

    def index(self):
        page = self.args_int('page')
        per_page = self.args_int('per_page')

        flags, pages, total = flag_repo.index(page, per_page)
        return self.echo(0, {'data': flags, 'pages': pages, 'total': total, 'per_page': per_page, 'page': page})

