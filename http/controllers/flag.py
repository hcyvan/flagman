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

    def delete(self, flag_id):
        flag = flag_repo.get_flag_by_id(flag_id)
        if not flag:
            return self.echo(208)

        flag_repo.delete(flag)

        return self.echo(0)
