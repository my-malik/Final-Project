from flask_testing import TestCase
from application import app, db
from application.models import Players, Teams
from flask import url_for


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):

        db.create_all() 

        new_player = Players(player_name="testing player", position="testing position")
        new_team = Teams(team_name="testing team")
        db.session.add(new_team)
        db.session.add(new_player)
        db.session.commit

    def tearDown(self):
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

    def test_create_player_get(self):
        response = self.client.get(url_for("create_player"))
        self.assert200(response)

    def test_update_players(self):
        response = self.client.get(url_for("update_player", id=1))
        self.assert200(response)
    

class TestRead(TestBase):

    def test_read_players(self):
        response = self.client.get(url_for("home"))
        self.assertIn("Player",str(response.data))

    # def test_read_team(self):
    #     response = self.client.get(url_for("home"))
    #     self.assertIn("Team",str(response.data))



# class TestCreate(TestBase):
       
#     def test_create_players(self):
#         response = self.client.post(
#             url_for("create_player"), 
#             data={"player_name":"Add a new player"},
#             follow_redirects=True
#         )
#         # self.assertIn(b"Add a new task", response.data)

#         self.assertEqual("Add a new player", str(response.data))

    # def test_create_player_redirect(self):
    #     response = self.client.post(
    #         url_for("create_player"),
    #         json={"player_name": "Add a new player"},
    #         follow_redirects=True
    #     )
    #     self.assertIn("Add a new player", str(response.data))


class TestUpdate(TestBase):

    def test_update_player(self):
        response = self.client.post(
            url_for("update_player", id=1),
            data = {"player_name":"testing update"},
            follow_redirects=True
        )
        self.assertIn("Football App", str(response.data))


class TestDelete(TestBase):

    def test_delete_player(self):
        response = self.client.get(
            url_for("delete_player", id=1),
            follow_redirects=True
        )
        self.assertNotIn("testing player", str(response.data))