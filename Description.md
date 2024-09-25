**Task: Event Management API**

**Objective:**

You are required to build a simple API for an event management system using Django and Django Rest Framework (DRF). This task will assess your understanding of database relations, the Django ORM, viewsets, and data validation.

**Requirements:**

1. **Models**:
    - Create the following models:
        - **Event**: Fields should include title, date, location, and max_attendees.
        - **Attendee**: Fields should include name and email.
        - **Ticket**: Fields should include event (ForeignKey to Event) and attendee (ForeignKey to Attendee).
    - Establish appropriate relationships between these models:
        - An event can have many attendees.
        - Each ticket is associated with one event and one attendee.
2. **API Endpoints**:
    - Create a viewset for the Event model with the following functionalities:
        - **POST**: Create a new event. Ensure that max_attendees is greater than zero.
        - **GET**: Retrieve a list of events. Use select_related to fetch associated attendees and prefetch_related to fetch associated tickets efficiently.
3. **Data Validation**:
    - Implement validation to ensure that no event can have more attendees than the specified max_attendees.
    - Ensure that the email field in the Attendee model is unique.
4. **Documentation**:
    - Provide a brief README file explaining your design choices and how to set up and test your API.

**Time Limit:**

You have 2 hours to complete this task.

**Submission:**

Please submit your code in a Git repository, along with the README file, once you finish.
