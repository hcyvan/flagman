from model.db import Flag, db


def create(title, content, address, people_number, start_time, lat, lng):
    flag = {
        'title': title,
        'content': content,
        'address': address,
        'people_number': people_number,
        'start_time': start_time,
        'lat': lat,
        'lng': lng
    }
    db.session.add(Flag(**flag))
    db.session.commit()


def get_flag_by_id(flag_id):
    return Flag.query.get(flag_id)


def delete(flag):
    db.session.delete(flag)
    db.session.commit()

