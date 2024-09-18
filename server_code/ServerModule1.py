import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

import anvil.email
import anvil.server
@anvil.server.callable
def send_feedback(name, email, feedback):
  anvil. email.send(to="noreply@anvil.works",
                   subject=f"Feedback from {name}",
                   text=f"""

                    A new person has filled out the feedback form!

  Name: {name}
  Email address: {email}
  Feedback:
  {feedback}
  """)
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )

def submit_button_click(self, **event_args):
  name = self.name_box.text
  email = self.email_box.text
  feedback = self.feedback_box.text
  # Call your 'send_feedback' server function
  # pass in name, email and feedback as arguments
  anvil.server.call('send_feedback', name, email, feedback)

def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    anvil.server.call('send_feedback', name, email, feedback)
    # Show a popup that says 'Feedback submitted!'
    Notification("Feedback submitted!").show()

 def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""

def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    anvil.server.call('send_feedback', name, email, feedback)
    Notification("Feedback submitted!").show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()


