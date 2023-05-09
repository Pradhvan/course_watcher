# course_watcher

* FastAPI based api server to serve course info from MongoDB.

### Endpoints

1. `/courses`:
    - Method: GET
        -Get a list of all courses.

    - Sorting : `/courses?sort_by=title,date,raiting`
        - Alphabetical (based on course title, ascending)
        - date (descending)
        - rating (descending)

    - Filter: `/courses?domain=domainname1,domainname2`
        - Group courses bases on domain

2. `/course/<courseid>/overview`
    - Method: GET
        - Get the course overview.

3. `/course/<courseid>/chapter/<chapternumber>`
    - Method: GET
        - Get specific chapter infomation

4. `/course/<courseid>/raiting`

    - Method: GET
        - Retrive rating of the course.
    
    - Method: POST
        - Submit rating of the course.
        - Request
        ```Python
        {
            "user_id": id,
            "course_id": id,
            "raiting": float
        }
        ```