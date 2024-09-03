"""Describing admin and the privileges."""

from module4 import Admin, Users, Privileges

recent_user = Admin("linda",
                    "aime",
                    "laime25",
                    25,
                    "lani@email",
                    ("delete", "ban user","post")
                    )
recent_user.privileges.show_privileges()
another_user = Privileges(("eat pizza", "drink coffee"))
another_user.show_privileges()