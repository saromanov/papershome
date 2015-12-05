from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import FormActions

from .models import Paper, CodeLink

class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'author', 'description', 'breif_description', 'version', 'category', 'link', 'repo', 'links']
    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
        print("NEW FORM")
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Create a new paper',
                'title',
                'author',
                'category',
                'link',
                'breif_description',
                'description',
                'version',
            ),
            FormActions(
                  Submit('save_changes', 'Add', css_class="btn-primary"),
                  Submit('cancel', 'Cancel'),
           )
            )

class CodeForm(ModelForm):
    class Meta:
        model = CodeLink
        fields = ['title', 'repolink', 'usage']
    def __init__(self, *args, **kwargs):
        super(CodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Add a information about code',
                'title',
                'repolink',
            ),
                   )


