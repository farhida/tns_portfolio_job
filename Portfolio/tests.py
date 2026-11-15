from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegistrationTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="ExistingUser", password="safe-test-password")

    def test_existing_username_returns_form_error(self):
        for username in ("ExistingUser", "existinguser"):
            with self.subTest(username=username):
                response = self.client.post(
                    reverse("register"),
                    {
                        "username": username,
                        "email": f"{username}@example.com",
                        "password": "another-safe-password",
                        "confirm_password": "another-safe-password",
                    },
                )

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "This username is already taken.")

        self.assertEqual(User.objects.count(), 1)

    def test_registration_redirects_non_staff_user_home(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "new-portfolio-user",
                "email": "new-portfolio-user@example.com",
                "password": "another-safe-password",
                "confirm_password": "another-safe-password",
            },
        )

        self.assertRedirects(response, reverse("home"), fetch_redirect_response=False)
        self.assertTrue(self.client.session.get("_auth_user_id"))
