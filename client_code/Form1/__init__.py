from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

def submit_button_click(self, **event_args):
  # Set 'name' to the text in the 'name_box'
  name = self.name_box.text
  # Set 'email' to the text in the 'email_box'
  email = self.email_box.text
  # Set 'feedback' to the text in the 'feedback_box'
  feedback = self.feedback_box.text
