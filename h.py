from drawio import Diagram

# Create a new diagram for Flask Forum workflow
diagram = Diagram()

# Add the necessary elements and their relations
diagram.add_element('User', 'Start')
diagram.add_element('Login', 'User', position=(300, 150))
diagram.add_element('Registration', 'User', position=(300, 250))
diagram.add_element('HomePage', 'Login', position=(500, 150))
diagram.add_element('Topics', 'HomePage', position=(700, 150))
diagram.add_element('CreateTopic', 'Topics', position=(900, 150))
diagram.add_element('Post', 'Topic', position=(500, 300))
diagram.add_element('Reply', 'Post', position=(700, 300))
diagram.add_element('Admin', 'HomePage', position=(500, 400))

# Add connections
diagram.add_connection('Start', 'User')
diagram.add_connection('User', 'Login')
diagram.add_connection('User', 'Registration')
diagram.add_connection('Login', 'HomePage')
diagram.add_connection('HomePage', 'Topics')
diagram.add_connection('Topics', 'CreateTopic')
diagram.add_connection('HomePage', 'Admin')
diagram.add_connection('Topic', 'Post')
diagram.add_connection('Post', 'Reply')

# Save the diagram to a .drawio file
file_path = "/mnt/data/Flask_Forum_Workflow.drawio"
diagram.save(file_path)

file_path
