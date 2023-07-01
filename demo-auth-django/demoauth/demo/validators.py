import emoji
from django import forms


class CharacterValidator:
    def validate(self, password, user=None):
        if emoji.emoji_count(password):
            raise forms.ValidationError('Your password can not contain emoji.')

    def get_help_text(self):
        return 'Your password can not contain emoji.'
