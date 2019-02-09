import random

def test_del_group(app):
    old_list=app.groups.get_group_list()
    if len(old_list) < 2:
        app.groups.add_new_group("test")
        old_list.append("test")
    ind = random.choice(range(len(old_list)))
    app.groups.dell_group_by_number(ind)
    new_list = app.groups.get_group_list()
    old_list.__delitem__(ind)
    assert sorted(old_list) == sorted(new_list)
