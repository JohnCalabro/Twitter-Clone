def test_message_model(self):
        """Does basic model work?"""
        
        m = Message(
            text="a warble",
            user_id=self.uid
        )

        db.session.add(m)
        db.session.commit()

        # User should have 1 message
        self.assertEqual(len(self.u.messages), 1)
        self.assertEqual(self.u.messages[0].text, "a warble")


# (venv) johncalabro@Johns-MacBook-Pro warbler % FLASK_ENV=production python -m unittest test_message_model.py

# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s

# OK