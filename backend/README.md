# Fast-API-app

## creating fastapi appliction

# CRUD opertations
- create
- Read
- update
- delete

# Rest API
- Get
- POST
- PUT
- DELETE

# status codes
- 200 codes
- 201 created
- 204 No Content 
- 400 Bad request
- 403 Forbidden
- 402 Method Not Allowed
- 499 Conflict
- 500 Internal server error

# Architecture of fastapi application
- Model -- tables creation
- Router -- routes requests to controllers
- controller -- controller logic
- service -- business logic
- Repository -- data access layer
- Middleware -- request processing pipeline

# database
## relational database\
- mysql
- postgresql
- splite
- sql server

## non-relational database
- mongodb
- dynamodb
- redis
- cassandra

# constraits in database
- primary key -- eg: student_id,staff_id
- foriegn key -- eg: department_id in student table
- unique --eg: email,phonenumber
- not null --eg: name
- check --  eg: salary > 0
- default -- eg:timestamp: func.now()
