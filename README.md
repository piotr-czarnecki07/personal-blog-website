# personal-blog-website

Personal blog website implemented with Django.  
The website serves as a blog wall for a single user (admin).  
It uses Basic HTTP Authentication for authenticating the admin.  
There is no bot protection for the comment section, as the project's goal is to demonstrate skills in the Django framework, Basic HTTP Authentication, and implementing admin-user roles in the application.

If the website is to be hosted, the `ALLOWED_HOSTS` variable should be updated to match the domain.

#### Admin Capabilities
- Add new posts for website visitors.
- Update and delete existing posts.
- Delete comments made by users under posts.

#### Visitor Capabilities
- Read posts.
- Leave comments.

## Table of Contents
- [Setting up the Enviroment](#setting-up-the-enviroment)
- [How to Use](#how-to-use)
- [License](#license)
- [Credits](#credits)

## Setting up the Enviroment

1. Ensure Python 3.10+ is installed.
2. Create a virtual environment in the project's root directory, for example, by running `py -m venv venv`.
3. Activate the created environment.
4. Install dependencies from `requirements.txt`.
5. Create a `.env` file based on the `.env.example` file in the `./personal_blog/` directory.
6. Create your local `db.sqlite3` database in the `./personal_blog/` directory. It will serve as storage for the posts.
7. Navigate to the `./personal_blog/` directory using `cd`.
8. Run `manage.py runserver` and open the browser on the provided host.

<br>

> [!NOTE]
> If the project is hosted on a domain, the following steps are not needed.

## How to Use

As a visitor, you can read posts created by the admin and leave comments.  
Posts are listed on the main page, and you can click on a post's title to view it.  
At the bottom of the post page, there's a comment section where you can leave a comment without logging in (no bot protection).  
As an admin, you can log in to create, delete, and update posts for visitors to read.  
You can also delete comments made by visitors.

## License

This project is licensed under the MIT License.  
See [LICENSE](./LICENSE) for more information.

## Credits

- Idea: [https://roadmap.sh/projects/personal-blog](https://roadmap.sh/projects/personal-blog)  
