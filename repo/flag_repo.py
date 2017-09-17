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
